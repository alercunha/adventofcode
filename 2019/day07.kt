import java.io.File
import day05lib.intCode
import day05lib.split

fun thruster(program: String, size: Int, input: Int, phases: List<Int>): Int {
	var signal = input
	(0..size-1).forEach{
		var out = intCode(split(program), listOf(phases[it], signal))[0]
		signal = out
	}
	return signal	
}

var combination = sequence {
	(0..4).forEach{i0 -> 
		(0..4).forEach{i1 -> 
			(0..4).forEach{i2 -> 
				(0..4).forEach{i3 -> 
					(0..4).forEach{i4 -> 
						var all = setOf(i0, i1, i2, i3, i4)
						if (all.size == 5)
							yield(listOf(i0, i1, i2, i3, i4))
					}
				}
			}
		}
	}
}

fun part1(program: String): Int? {
	return combination.map{ thruster(program, 5, 0, it) }.max()
}

fun main() {
    assert(thruster("3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0", 5, 0, listOf(4,3,2,1,0)) == 43210)
    assert(part1("3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0") == 43210)
    assert(part1("3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0") == 54321)
    assert(part1("3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0") == 65210)

    var lines = File("day07.in").readLines()
    println(part1(lines[0]))
}
