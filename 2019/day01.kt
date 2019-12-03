import java.io.File

fun part1(mass: Int): Int {
    return Math.floorDiv(mass, 3) - 2
}

fun part2(mass: Int, sum: Int = 0): Int {
    var r = part1(mass)
    return if (r < 0) sum else part2(r, sum + r)
}

fun main() {
    assert(part1(12) == 2)
    assert(part1(14) == 2)
    assert(part1(1969) == 654)
    assert(part1(100756) == 33583)

    var result = File("day01-1.in").readLines().sumBy{ part1(it.toInt()) }
    println(result)

    assert(part2(12) == 2)
    assert(part2(1969) == 966)
    assert(part2(100756) == 50346)

    result = File("day01-2.in").readLines().sumBy{ part2(it.toInt()) }
    println(result)
}
