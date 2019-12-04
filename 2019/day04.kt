import java.io.File

fun part1(pass: String): Boolean {
    var doubleDigits = false
    (1..pass.length-1).forEach{ i -> 
        if (pass[i].toInt() < pass[i-1].toInt()) {
            return false
        }
        if (pass[i] == pass[i-1]) {
            doubleDigits = true
        }
    }
    return doubleDigits
}

fun part2(pass: String): Boolean {
    var countRepetition = 0
    var doubleDigits = false
    (1..pass.length-1).forEach{ i -> 
        if (pass[i].toInt() < pass[i-1].toInt()) {
            return false
        }
        if (pass[i] == pass[i-1]) {
            countRepetition += 1
        } else {
            if (countRepetition == 1) {
                doubleDigits = true
            }
            countRepetition = 0
        }
    }
    if (countRepetition == 1) {
        doubleDigits = true
    }
    return doubleDigits
}

fun main() {
    assert(part1("122345"))
    assert(part1("111123"))
    assert(!part1("135679"))
    assert(part1("111111"))
    assert(!part1("223450"))
    assert(!part1("123789"))

    var result = (245182..790572).filter{ i -> part1(i.toString()) }.count()
    println(result)

    assert(part2("112233"))
    assert(!part2("123444"))
    assert(part2("111122"))

    result = (245182..790572).filter{ i -> part2(i.toString()) }.count()
    println(result)
}
