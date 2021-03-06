import java.io.File

class Space(positions: List<List<Int>>, velocities: List<List<Int>>? = null) {
    var positions = positions
    var dimensions = positions[0].size
    var velocities = if (velocities == null) positions.map{ (0..dimensions-1).map{ 0 } } else velocities

    fun energy(): Int {
        return (0..positions.size-1).map {
            positions[it].map{Math.abs(it)}.sum() * velocities[it].map{Math.abs(it)}.sum()
        }.sum()
    }

    fun moveStep(): Space {
        var velocities = (0..positions.size-1).map {
            var j = positions[it]
            var vel = positions.filter{j != it}.map { i ->
                (0..i.size-1).map{velocity(i[it], j[it])}
            }.reduce{a, b -> sumPos(a, b)}
            sumPos(vel, velocities[it])
        }
        var positions = (0..velocities.size-1).map {
            sumPos(positions[it], velocities[it])
        }
        return Space(positions, velocities)
    }

    fun equals(other: Space): Boolean {
        (0..positions.size-1).forEach{
            if (positions[it] != other.positions[it])
                return false
        }
        return true
    }

    fun print() {
        println(positions)
        println(velocities)
        println("energy: ${energy()}")
        println("")
    }
}

fun velocity(a: Int, b: Int): Int {
    return if (a > b) +1 else if (a < b) -1 else 0
}

fun sumPos(a: List<Int>, b: List<Int>): List<Int> {
    return (0..a.size-1).map{a[it] + b[it]}
}

fun parse(input: List<String>): List<List<Int>> {
    return input.map {
        var values = it.trim().drop(1).dropLast(1).split(",")
        values.map{it.trim().drop(2).toInt()}
    }
}

fun part1(input: List<String>, steps: Int): Int {
    var space = Space(parse(input))
    (0..steps-1).forEach{space = space.moveStep()}
    return space.energy()
}

fun part2(input: List<String>): Long {
    var initial = Space(parse(input))
    var space = initial
    var step = 0L
    space.print()
    do {
        step++
        space = space.moveStep()
        //space.print()
        //println("step: ${step}")
    } while (space.energy() != 0)
    return step * 2
}

fun main() {
    var input1 =
        """
            <x=-1, y=0, z=2>
            <x=2, y=-10, z=-7>
            <x=4, y=-8, z=8>
            <x=3, y=5, z=-1>    
        """.trimIndent()
    assert(part1(input1.lines(), 10) == 179)

    var input2 =
        """
            <x=-8, y=-10, z=0>
            <x=5, y=5, z=10>
            <x=2, y=-7, z=3>
            <x=9, y=-8, z=-3>        
        """.trimIndent()
    assert(part1(input2.lines(), 100) == 1940)

    var day12input =
        """
            <x=-6, y=-5, z=-8>
            <x=0, y=-3, z=-13>
            <x=-15, y=10, z=-11>
            <x=-3, y=-8, z=3>
        """.trimIndent()
    println(part1(day12input.lines(), 1000))

    assert(part2(input1.lines()) == 2772L)

    var input3 =
        """
            <x=1, y=1, z=10>
            <x=10, y=10, z=10>
            <x=20, y=20, z=10>
        """.trimIndent()
    assert(part2(input3.lines()) == 12L)
    //assert(part2(input2.lines()) == 4686774924L)
}
