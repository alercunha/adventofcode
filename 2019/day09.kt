import java.io.File
import day05lib.Program
import day05lib.splitLong
import day05lib.longCode

fun main() {
	assert(longCode(splitLong("109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99")).joinToString(",") == "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99")
	assert(longCode(splitLong("1102,34915192,34915192,7,4,7,99,0"))[0] == 1219070632396864L)
	assert(longCode(splitLong("104,1125899906842624,99"))[0] == 1125899906842624L)

	var lines = File("day09.in").readLines()
	println(longCode(splitLong(lines[0]), listOf(1L)))

	println(longCode(splitLong(lines[0]), listOf(2L)))
}
