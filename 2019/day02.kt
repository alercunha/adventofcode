import java.io.File

fun part1(input: String): List<Int> {
    var c = input.split(",").map{ it.toInt() } as MutableList<Int>
    return _part1(c)
}

fun _part1(c: MutableList<Int>): List<Int> {
    var i = 0
    while (c[i].toInt() != 99) {
        var r = when (c[i]) {
            1 -> c[c[i + 1]] + c[c[i + 2]]
            2 -> c[c[i + 1]] * c[c[i + 2]]
            else -> 0
        }
        c[c[i + 3]] = r
        i = i + 4
    }
    return c
}

fun main() {
    assert(part1("1,9,10,3,2,3,11,0,99,30,40,50")[0] == 3500)
    assert(part1("1,0,0,0,99")[0] == 2)
    assert(part1("2,3,0,3,99")[3] == 6)
    assert(part1("2,4,4,5,99,0")[5] == 9801)
    assert(part1("1,1,1,4,99,5,6,0,99")[0] == 30)

    var lines = File("day02-1.in").readLines()
    var c = lines[0].split(",").map{ it.toInt() } as MutableList<Int>
    c[1] = 12
    c[2] = 2
    var result = _part1(c)
    println(result[0])
}
