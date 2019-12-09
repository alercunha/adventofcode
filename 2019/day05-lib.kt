package day05lib

import java.util.ArrayDeque
import java.util.Queue

public fun split(input: String): MutableList<Int> {
    return input.split(",").map{ it.toInt() } as MutableList<Int>
}

fun readParam(c: List<Int>, position: Int, mode: Char): Int {
    if (mode == '0')
        return c[c[position]]
    else if (mode == '1')
        return c[position]
    else
        return -1
}

public fun intCode(c: MutableList<Int>, inputs: List<Int> = ArrayList<Int>()): List<Int> {
    var p = Program(c)
    p.run(inputs)
    return p.output
}

public class Program(c: MutableList<Int>) {
    var output = ArrayList<Int>()
    var p = 0
    var c = c

    fun run(inputs: List<Int> = ArrayList<Int>()): Boolean {
        var inputQueue = ArrayDeque<Int>(inputs)
        while (c[p] != 99) {
            var code = c[p].toString()
            var opcode = code.takeLast(2).toInt()
            var modes = if (code.length <= 2) "" else code.slice(0..code.length-3)
            modes = modes.padStart(3, '0').reversed()
            var jump = 0
            when (opcode) {
                1 -> {
                    c[c[p + 3]] = readParam(c, p + 1, modes[0]) + readParam(c, p + 2, modes[1])
                    jump = 4
                }
                2 -> { 
                    c[c[p + 3]] = readParam(c, p + 1, modes[0]) * readParam(c, p + 2, modes[1])
                    jump = 4
                }
                3 -> {
                    if (inputQueue.peek() == null) {
                        return false
                    }
                    c[c[p + 1]] = inputQueue.poll()
                    jump = 2
                }
                4 -> {
                    output.add(readParam(c, p + 1, modes[0]))
                    jump = 2
                }
                5 -> {
                    if (readParam(c, p + 1, modes[0]) != 0) {
                        p = readParam(c, p + 2, modes[1])
                    } else {
                        jump = 3
                    }
                }
                6 -> {
                    if (readParam(c, p + 1, modes[0]) == 0) {
                        p = readParam(c, p + 2, modes[1])
                    } else {
                        jump = 3
                    }
                }
                7 -> {
                    c[c[p + 3]] = if (readParam(c, p + 1, modes[0]) < readParam(c, p + 2, modes[1])) 1 else 0
                    jump = 4
                }
                8 -> {
                    c[c[p + 3]] = if (readParam(c, p + 1, modes[0]) == readParam(c, p + 2, modes[1])) 1 else 0
                    jump = 4
                }
                else -> {
                }
            }
            p = p + jump
        }
        return true
    }
}
