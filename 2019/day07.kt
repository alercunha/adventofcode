import java.io.File
import day05lib.Program
import day05lib.split

fun thruster(program: String, size: Int, input: Int, phases: List<Int>): Int {
	var amps = ArrayList<Program>()
	(0..size-1).forEach{
		var p = Program(split(program))
		p.run(listOf(phases[it]))
		amps.add(p)
	}
	var signal = input
	var pos = 0
	var halted = false
	while (!halted) {
		var result = amps[pos].run(listOf(signal))
		if (pos == size - 1 && result.second)
			halted = true
		signal = result.first.last()
		pos = (pos + 1) % size
	}
	return signal
}

fun combine(start: Int, end: Int): Sequence<List<Int>> {
	var seq = sequence {
		(start..end).forEach{i0 -> 
			(start..end).forEach{i1 -> 
				(start..end).forEach{i2 -> 
					(start..end).forEach{i3 -> 
						(start..end).forEach{i4 -> 
							var all = setOf(i0, i1, i2, i3, i4)
							if (all.size == 5)
								yield(listOf(i0, i1, i2, i3, i4))
						}
					}
				}
			}
		}
	}
	return seq
}

fun part1(program: String): Int? {
	return combine(0, 4).map{ thruster(program, 5, 0, it) }.max()
}

fun part2(program: String): Int? {
	return combine(5, 9).map{ thruster(program, 5, 0, it) }.max()
}

fun main() {
    assert(thruster("3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0", 5, 0, listOf(4,3,2,1,0)) == 43210)
    assert(part1("3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0") == 43210)
    assert(part1("3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0") == 54321)
    assert(part1("3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0") == 65210)

    var lines = File("day07.in").readLines()
    println(part1(lines[0]))

    assert(thruster("3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5", 5, 0, listOf(9,8,7,6,5)) == 139629729)
    assert(part2("3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5") == 139629729)
    assert(part2("3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10") == 18216)

    println(part2(lines[0]))
}
