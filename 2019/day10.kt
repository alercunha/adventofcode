import java.util.ArrayDeque
import java.util.Queue

// https://stackoverflow.com/a/27481611
fun angle(a: Pair<Int, Int>, b: Pair<Int, Int>): Double {
    var deltaY = (a.second - b.second).toDouble()
    var deltaX = (b.first - a.first).toDouble()
    var angle = Math.toDegrees(Math.atan2(deltaY, deltaX)) 
    return if (angle < 0) 360.0 + angle else angle
}

fun detect(station: Pair<Int, Int>, asteroids: List<Pair<Int, Int>>): Int {
    var angles = HashSet<Double>()
    var detected = 0
    asteroids.forEach {
        var angle = angle(station, it)
        if (station != it && !angles.contains(angle)) {
            detected++
            angles.add(angle)
        }
    }
    return detected
}

fun toAsteroids(lines: List<String>): List<Pair<Int, Int>> {
    var asteroids = ArrayList<Pair<Int, Int>>()
    (0..lines.size-1).forEach { y ->
        (0..lines[y].length-1).forEach { x ->
            if (lines[y][x] == '#') {
                asteroids.add(Pair(x, y))
            }
        }
    }
    return asteroids
}

fun bestSight(asteroids: List<Pair<Int, Int>>): Pair<Int, Int> {
    var station = asteroids.maxBy{ detect(it, asteroids) }!!
    return station
}

fun part1(lines: List<String>): Int {
    var asteroids = toAsteroids(lines)
    var station = bestSight(asteroids)
    return detect(station, asteroids)
}

fun distance(a: Pair<Int, Int>, b: Pair<Int, Int>): Double {
    return Math.pow((b.second - a.second).toDouble(), 2.0) + Math.pow((b.first - a.first).toDouble(), 2.0)
}

fun laserKill(station: Pair<Int, Int>, asteroids: List<Pair<Int, Int>>): List<Pair<Int, Int>> {
    var aiming = asteroids.map({
        var angle = (angle(station, it) - 90) * -1 // normalize to start shooting up
        angle = if (angle < 0) 360.0 + angle else angle
        Triple(angle, distance(station, it), it) 
    })

    // group by angle and sort by distance to station
    var reach = aiming.groupBy { it.first }
                       .values.map { ArrayDeque(it.sortedWith(compareBy({it.second}))) }
                       .sortedWith(compareBy({it.getFirst().first}))

    // kill one by one starting at 90 degrees clockwise
    var killed = ArrayList<Pair<Int, Int>>()
    var vaporized = false
    while (!vaporized) {
        vaporized = true
        reach.filter { !it.isEmpty() }.forEach { g ->
            killed.add(g.pop().third)
            vaporized = false
        }
    }
    return killed
}

fun part2(lines: List<String>): List<Pair<Int, Int>> {
    var asteroids = toAsteroids(lines)
    var station = bestSight(asteroids)
    return laserKill(station, asteroids.filter({it != station}))
}

fun main() {
    var input = 
        """
            .#..#
            .....
            #####
            ....#
            ...##
        """.trimIndent()
    assert(part1(input.lines()) == 8)
    input =
        """
            ......#.#.
            #..#.#....
            ..#######.
            .#.#.###..
            .#..#.....
            ..#....#.#
            #..#....#.
            .##.#..###
            ##...#..#.
            .#....####        
        """.trimIndent()
    assert(part1(input.lines()) == 33)
    input =
        """
            #.#...#.#.
            .###....#.
            .#....#...
            ##.#.#.#.#
            ....#.#.#.
            .##..###.#
            ..#...##..
            ..##....##
            ......#...
            .####.###.
        """.trimIndent()
    assert(part1(input.lines()) == 35)
    input =
        """
            .#..#..###
            ####.###.#
            ....###.#.
            ..###.##.#
            ##.##.#.#.
            ....###..#
            ..#.#..#.#
            #..#.#.###
            .##...##.#
            .....#.#..        
        """.trimIndent()
    assert(part1(input.lines()) == 41)
    var input2 =
        """
            .#..##.###...#######
            ##.############..##.
            .#.######.########.#
            .###.#######.####.#.
            #####.##.#.##.###.##
            ..#####..#.#########
            ####################
            #.####....###.#.#.##
            ##.#################
            #####.##.###..####..
            ..######..##.#######
            ####.##.####...##..#
            .#####..#.######.###
            ##...#.##########...
            #.##########.#######
            .####.#.###.###.#.##
            ....##.##.###..#####
            .#.#.###########.###
            #.#.#.#####.####.###
            ###.##.####.##.#..##        
        """.trimIndent()
    assert(part1(input2.lines()) == 210)

    var day10input =
        """
            #..#.#.###.#...##.##....
            .#.#####.#.#.##.....##.#
            ##..#.###..###..#####..#
            ####.#.#..#....#..##.##.
            .#######.#####...#.###..
            .##...#.#.###..###.#.#.#
            .######.....#.###..#....
            .##..##.#..#####...###.#
            #######.#..#####..#.#.#.
            .###.###...##.##....##.#
            ##.###.##.#.#..####.....
            #.#..##..#..#.#..#####.#
            #####.##.#.#.#.#.#.#..##
            #...##.##.###.##.#.###..
            ####.##.#.#.####.#####.#
            .#..##...##..##..#.#.##.
            ###...####.###.#.###.#.#
            ..####.#####..#####.#.##
            ..###..###..#..##...#.#.
            ##.####...##....####.##.
            ####..#..##.#.#....#..#.
            .#..........#..#.#.####.
            ###..###.###.#.#.#....##
            ########.#######.#.##.##
        """.trimIndent()
    println(part1(day10input.lines()))

    input =
        """
            .#....#####...#..
            ##...##.#####..##
            ##...#...#.#####.
            ..#.....#...###..
            ..#.#.....#....##
        """.trimIndent()
    assert(part1(input.lines()) == 30)
    assert(part2(input.lines()).last() == Pair(14, 3))

    var result = part2(input2.lines())
    assert(result[0] == Pair(11, 12))
    assert(result[1] == Pair(12, 1))
    assert(result[2] == Pair(12, 2))
    assert(result[9] == Pair(12, 8))
    assert(result[19] == Pair(16, 0))
    assert(result[49] == Pair(16, 9))
    assert(result[99] == Pair(10, 16))
    assert(result[198] == Pair(9, 6))
    assert(result[199] == Pair(8, 2))
    assert(result[200] == Pair(10, 9))
    assert(result[298] == Pair(11, 1))

    result = part2(day10input.lines())
    println(result[199].first * 100 + result[199].second)
}