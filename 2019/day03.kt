import java.io.File

fun calculatePaths(input: List<String>): Array<ArrayList<Triple<Int, Int, Int>>> {
	var paths = Array(input.size){ _ -> ArrayList<Triple<Int, Int, Int>>()}
    var commands = input.map{ it -> it.split(",") }

	(0..commands.size-1).forEach { c ->
		var x = 0
		var y = 0
		commands[c].forEach { dir ->
			var n = dir.substring(1).toInt()
			if (dir[0] == 'R') {
				(0..n-1).forEach {
					paths[c].add(Triple(x, y, paths[c].size))
					x = x + 1
				}
			}
			if (dir[0] == 'L') {
				(0..n-1).forEach {
					paths[c].add(Triple(x, y, paths[c].size))
					x = x - 1
				}
			}
			if (dir[0] == 'U') {
				(0..n-1).forEach {
					paths[c].add(Triple(x, y, paths[c].size))
					y = y - 1
				}
			}
			if (dir[0] == 'D') {
				(0..n-1).forEach {
					paths[c].add(Triple(x, y, paths[c].size))
					y = y + 1
				}
			}
		}
	}
	return paths
}

fun komp(a: Triple<Int, Int, Int>, b: Triple<Int, Int, Int>): Int {
    return when {
        a.first > b.first -> 1
        a.first < b.first -> -1
        a.second > b.second -> 1
        a.second < b.second -> -1
        else -> 0
    }
}

fun part1(input: List<String>): Int {
	var paths = calculatePaths(input)
	var match = ArrayList<Int>()
	var comp = Comparator<Triple<Int, Int, Int>>{a, b -> komp(a, b)}
	var firstPath = paths[0].sortedWith(comp)
	var secondPath = paths[1].sortedWith(comp)
	firstPath.forEach { pair ->
		if (pair.first != 0 && pair.second != 0) {
			var found = secondPath.binarySearch(pair, comp)
			if (found >= 0) {
				var dist = Math.abs(pair.first) + Math.abs(pair.second)
				match.add(dist)
			}
		}
	}
	return match.min()!!
}

fun part2(input: List<String>): Int {
	var paths = calculatePaths(input)
	var match = ArrayList<Int>()
	var comp = Comparator<Triple<Int, Int, Int>>{a, b -> komp(a, b)}
	var firstPath = paths[0].sortedWith(comp)
	var secondPath = paths[1].sortedWith(comp)
	firstPath.forEach { pair ->
		if (pair.first != 0 && pair.second != 0) {
			var found = secondPath.binarySearch(pair, comp)
			if (found >= 0) {
				match.add(pair.third + secondPath[found].third)
			}
		}
	}
	return match.min()!!
}

fun main() {
    assert(part1(listOf("R8,U5,L5,D3", "U7,R6,D4,L4")) == 6)
    assert(part1(listOf("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83")) == 159)
    assert(part1(listOf("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")) == 135)

    var lines = File("day03.in").readLines()
    println(part1(lines))

    assert(part2(listOf("R8,U5,L5,D3", "U7,R6,D4,L4")) == 30)
	assert(part2(listOf("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83")) == 610)
    assert(part2(listOf("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")) == 410)

    println(part2(lines))
}
