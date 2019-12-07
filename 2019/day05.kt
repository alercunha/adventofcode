import java.io.File
import java.util.ArrayDeque
import java.util.Queue

fun split(input: String): MutableList<Int> {
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

fun intCode(c: MutableList<Int>, inputs: List<Int> = ArrayList<Int>()): List<Int> {
    var p = 0
    var o = ArrayList<Int>()
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
                c[c[p + 1]] = inputQueue.poll()
                jump = 2
            }
            4 -> {
                o.add(c[c[p + 1]])
                jump = 2
            }
            else -> {
            }
        }
        p = p + jump
    }
    return o
}

fun main() {
    assert(intCode(split("1,11,12,3,2,3,13,0,4,0,99,30,40,50"))[0] == 3500)
    assert(intCode(split("1,0,0,0,4,0,99"))[0] == 2)
    assert(intCode(split("2,3,0,3,4,3,99"))[0] == 6)
    assert(intCode(split("2,6,6,7,4,7,99,0"))[0] == 9801)
    assert(intCode(split("1,1,1,4,99,5,6,0,4,0,99"))[0] == 30)

    assert(intCode(split("3,0,4,0,99"), listOf(2))[0] == 2)
    assert(intCode(split("3,0,4,0,99"), listOf(278))[0] == 278)
    assert(intCode(split("1101,100,-1,6,4,6,0"))[0] == 99)
    assert(intCode(split("1002,4,3,4,33,4,0")).size == 0)

    var lines = File("day05.in").readLines()
    var result = intCode(split(lines[0]), listOf(1))
    println(result)
}
