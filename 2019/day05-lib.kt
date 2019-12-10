package day05lib

import java.util.ArrayDeque
import java.util.Queue

public fun split(input: String): MutableList<Int> {
    return input.split(",").map{ it.toInt() } as MutableList<Int>
}

public fun splitLong(input: String): MutableList<Long> {
    return input.split(",").map{ it.toLong() } as MutableList<Long>
}

public fun intCode(c: MutableList<Int>, inputs: List<Int> = ArrayList<Int>()): List<Int> {
    var p = Program(c.map{it.toLong()} as MutableList)
    p.runLong(inputs.map{it.toLong()})
    return p.output.map{it.toInt()}
}

public fun longCode(c: MutableList<Long>, inputs: List<Long> = ArrayList<Long>()): List<Long> {
    var p = Program(c)
    p.runLong(inputs)
    return p.output
}

public class Program {
    var output = ArrayList<Long>()
    var p: Int = 0
    var c: LongArray
    var b: Int = 0

    constructor(input: MutableList<Long>) {
        c = LongArray(10000)
        (0..input.size-1).forEach {
            c[it] = input[it]
        }
    }

    fun readParam(position: Int, mode: Char): Long {
        if (mode == '0')
            return c[c[position].toInt()]
        else if (mode == '1')
            return c[position]
        else if (mode == '2')
            return c[c[position].toInt() + b]
        else
            return -1
    }

    fun writePosition(position: Int, mode: Char): Int {
        if (mode == '0')
            return c[position].toInt()
        else if (mode == '2')
            return c[position].toInt() + b
        else
            return -1
    }

    fun lastOutputInt(): Int {
        return output.last().toInt()
    }

    fun run(inputs: List<Int> = ArrayList<Int>()): Boolean {
        return runLong(inputs.map{it.toLong()})
    }

    fun runLong(inputs: List<Long> = ArrayList<Long>()): Boolean {
        var inputQueue = ArrayDeque<Long>(inputs)
        while (c[p] != 99L) {
            var code = c[p].toString()
            var opcode = code.takeLast(2).toLong()
            var modes = if (code.length <= 2) "" else code.slice(0..code.length-3)
            modes = modes.padStart(3, '0').reversed()
            var jump = 0
            when (opcode) {
                1L -> {
                    c[writePosition(p + 3, modes[2])] = readParam(p + 1, modes[0]) + readParam(p + 2, modes[1])
                    jump = 4
                }
                2L -> { 
                    c[writePosition(p + 3, modes[2])] = readParam(p + 1, modes[0]) * readParam(p + 2, modes[1])
                    jump = 4
                }
                3L -> {
                    if (inputQueue.peek() == null) {
                        return false
                    }
                    c[writePosition(p + 1, modes[0])] = inputQueue.poll()
                    jump = 2
                }
                4L -> {
                    output.add(readParam(p + 1, modes[0]))
                    jump = 2
                }
                5L -> {
                    if (readParam(p + 1, modes[0]) != 0L) {
                        p = readParam(p + 2, modes[1]).toInt()
                    } else {
                        jump = 3
                    }
                }
                6L -> {
                    if (readParam(p + 1, modes[0]) == 0L) {
                        p = readParam(p + 2, modes[1]).toInt()
                    } else {
                        jump = 3
                    }
                }
                7L -> {
                    c[writePosition(p + 3, modes[2])] = if (readParam(p + 1, modes[0]) < readParam(p + 2, modes[1])) 1 else 0
                    jump = 4
                }
                8L -> {
                    c[writePosition(p + 3, modes[2])] = if (readParam(p + 1, modes[0]) == readParam(p + 2, modes[1])) 1 else 0
                    jump = 4
                }
                9L -> {
                    b = b + readParam(p + 1, modes[0]).toInt()
                    jump = 2
                }
                else -> {
                }
            }
            p = p + jump
        }
        return true
    }
}
