import java.io.File
import day05lib.Program
import day05lib.splitLong

fun paint(code: String, start: Long=0L): Map<Pair<Int, Int>, Long> {
    var p = Program(splitLong(code))
    var inputs = listOf(start)
    var colors = HashMap<Pair<Int, Int>, Long>()
    var position = Pair(0, 0)
    var directions = listOf('<', '^', '>', 'v')
    var direction = 1
    var halted = false
    while (!halted) {
        halted = p.runLong(inputs)
        (0..p.output.size/2-1).forEach {
            colors.put(position, p.output[it])
            var move = if (p.output[it + 1] == 0L) -1 else 1
            direction = direction + move
            if (direction < 0)
                direction = directions.size - 1
            if (direction >= directions.size)
                direction = 0
            when (direction) {
                0 -> position = Pair(position.first - 1, position.second)
                1 -> position = Pair(position.first, position.second + 1)
                2 -> position = Pair(position.first + 1, position.second)
                3 -> position = Pair(position.first, position.second - 1)
                else -> throw Exception("error: ${directions.size} - ${direction}")
            }
        }
        inputs = listOf(colors.get(position) ?: start)
        p.clearOutput()
    }
    return colors
}

fun part1(code: String): Int {
    return paint(code).size
}

fun part2(code: String) {
    var colors = paint(code, 1L)
    var maxX = colors.keys.map{it.first}.max()!!
    var minX = colors.keys.map{it.first}.min()!!

    var maxY = colors.keys.map{it.second}.max()!!
    var minY = colors.keys.map{it.second}.min()!!

    (maxY downTo minY).forEach { y ->
        (minX..maxX).forEach { x ->
            var z = colors.get(Pair(x, y))
            if (z != null && z == 1L)
                print("#")
            else
                print(" ")
        }
        println("")
    }
}

fun main() {
    var lines = File("day11.in").readLines()
    println(part1(lines[0]))

    part2(lines[0])
}
