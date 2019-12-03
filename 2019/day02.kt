import java.io.File

fun part1(input: String): List<Int> {
    var c = input.split(",").map{ it.toInt() } as MutableList<Int>
    return _part1(c)
}

fun _part1(c: MutableList<Int>): List<Int> {
    var p = 0
    while (c[p].toInt() != 99) {
        var jump = 0
        when (c[p]) {
            1 -> {
                c[c[p + 3]] = c[c[p + 1]] + c[c[p + 2]]
                jump = 4
            }
            2 -> { 
                c[c[p + 3]] = c[c[p + 1]] * c[c[p + 2]]
                jump = 4
            }
            else -> {
            }
        }
        p = p + jump
    }
    return c
}

fun main() {
    assert(part1("1,9,10,3,2,3,11,0,99,30,40,50")[0] == 3500)
    assert(part1("1,0,0,0,99")[0] == 2)
    assert(part1("2,3,0,3,99")[3] == 6)
    assert(part1("2,4,4,5,99,0")[5] == 9801)
    assert(part1("1,1,1,4,99,5,6,0,99")[0] == 30)

    var lines = File("day02.in").readLines()
    var c = lines[0].split(",").map{ it.toInt() } as MutableList<Int>
    c[1] = 12
    c[2] = 2
    var result = _part1(c)
    println(result[0])

    for (noun in 0..99) {
        for (verb in 0..99) {
            c = lines[0].split(",").map{ it.toInt() } as MutableList<Int>
            c[1] = noun
            c[2] = verb
            if (_part1(c)[0] == 19690720) {
                println(100 * noun + verb)
                return
            }
        }
    }
}
