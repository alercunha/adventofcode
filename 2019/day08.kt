import java.io.File

class Layer(wide: Int, tall: Int) {
    var pixels: List<Int> = ArrayList<Int>()
    var wide = wide
    var tall = tall

    fun take(imageData: String): String {
        pixels = imageData.take(wide * tall).map{ (it - '0').toInt() }
        return imageData.drop(wide * tall)
    }
}

class Image(imageData: String, wide: Int, tall: Int) {
    var layers = createLayers(imageData, wide, tall)
    var wide = wide
    var tall = tall

    fun print() {
        (0..wide*tall-1).forEach {
            if (it % wide == 0 && it != 0)
                println("")
            print(if (getPixel(it) == 1) '#' else ' ')
        }
    }

    fun getPixel(pos: Int): Int {
        layers.forEach {
            if (it.pixels[pos] != 2)
                return it.pixels[pos]
        }
        return 2
    }
}

fun createLayers(imageData: String, wide: Int, tall: Int): List<Layer> {
    var layers = ArrayList<Layer>()
    var input = imageData
    while (!input.isEmpty()) {
        var layer = Layer(wide, tall)
        input = layer.take(input)
        layers.add(layer)
    }
    return layers
}

fun part1(input: String, wide: Int, tall: Int): Int {
    var layers = createLayers(input, wide, tall)
    var pick = layers.minBy{ it.pixels.filter{it == 0}.count() }!!
    return pick.pixels.count{it == 1} * pick.pixels.count{it == 2}
}

fun part2(input: String, wide: Int, tall: Int) {
    var image = Image(input, wide, tall)
    image.print()
}

fun main() {
    assert(part1("123456789012", 3, 2) == 1)
    assert(part1("221156789012", 3, 2) == 4)

    var lines = File("day08.in").readLines()
    println(part1(lines[0], 25, 6))

    part2(lines[0], 25, 6)
}
