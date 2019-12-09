package day05

import java.io.File
import day05lib.split
import day05lib.intCode

fun main() {
    assert(intCode(split("1,11,12,3,2,3,13,0,4,0,99,30,40,50"))[0] == 3500)
    assert(intCode(split("1,0,0,0,4,0,99"))[0] == 2)
    assert(intCode(split("2,3,0,3,4,3,99"))[0] == 6)
    assert(intCode(split("2,6,6,7,4,7,99,0"))[0] == 9801)
    assert(intCode(split("1,1,1,4,99,5,6,0,4,0,99"))[0] == 30)

    assert(intCode(split("3,0,4,0,99"), listOf(2))[0] == 2)
    assert(intCode(split("3,0,4,0,99"), listOf(278))[0] == 278)
    assert(intCode(split("1101,100,-1,6,4,6,0"))[0] == 99)
    assert(intCode(split("1002,4,3,4,33,4,0")).size == 0)

    var lines = File("day05.in").readLines()
    var result = intCode(split(lines[0]), listOf(1))
    println(result)

    assert(intCode(split("3,9,8,9,10,9,4,9,99,-1,8"), listOf(8))[0] == 1)
    assert(intCode(split("3,9,8,9,10,9,4,9,99,-1,8"), listOf(7))[0] == 0)

    assert(intCode(split("3,9,7,9,10,9,4,9,99,-1,8"), listOf(7))[0] == 1)
    assert(intCode(split("3,9,7,9,10,9,4,9,99,-1,8"), listOf(8))[0] == 0)
    assert(intCode(split("3,9,7,9,10,9,4,9,99,-1,8"), listOf(-1))[0] == 1)

    assert(intCode(split("3,3,1108,-1,8,3,4,3,99"), listOf(8))[0] == 1)
    assert(intCode(split("3,3,1108,-1,8,3,4,3,99"), listOf(-1))[0] == 0)

    assert(intCode(split("3,3,1107,-1,8,3,4,3,99"), listOf(8))[0] == 0)
    assert(intCode(split("3,3,1107,-1,8,3,4,3,99"), listOf(-1))[0] == 1)

    assert(intCode(split("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"), listOf(0))[0] == 0)
    assert(intCode(split("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"), listOf(1))[0] == 1)
    assert(intCode(split("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"), listOf(10))[0] == 1)

    var program = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
    assert(intCode(split(program), listOf(7))[0] == 999)
    assert(intCode(split(program), listOf(8))[0] == 1000)
    assert(intCode(split(program), listOf(9))[0] == 1001)

    result = intCode(split(lines[0]), listOf(5))
    println(result)
}
