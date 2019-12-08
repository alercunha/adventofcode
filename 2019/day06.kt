import java.io.File

class SpaceObj(name: String) {
    var name: String = name
    var orbiting: SpaceObj? = null
    var satellites: ArrayList<SpaceObj> = ArrayList<SpaceObj>()

    fun addSatellite(sat: SpaceObj) {
        satellites.add(sat)
        sat.orbiting = this
    }

    fun countOrbits(): Int {
        if (orbiting == null) {
            return 0
        }
        return orbiting!!.countOrbits() + 1
    }

    fun totalOrbits(): Int {
        return countOrbits() + satellites.sumBy({it.totalOrbits()})
    }

    fun search(name: String): SpaceObj? {
        return _search(name, null).first
    }

    fun distance(name: String): Int {
        return _search(name, null).second - 3
    }

    fun _search(name: String, from: SpaceObj?): Pair<SpaceObj?,Int> {
        if (this.name == name) {
            return Pair(this, 1)
        }
        satellites.filter({it !== from}).forEach{
            var found = it._search(name, this)
            if (found.first != null) {
                return Pair(found.first, found.second + 1)
            }
        }
        if (orbiting != null && from !== orbiting) {
            var found = orbiting!!._search(name, this)
            if (found.first != null) {
                return Pair(found.first, found.second + 1)
            }
        }
        return Pair(null,-1)
    }
}

fun createUniverse(orbits: List<String>): SpaceObj {
    var com = SpaceObj("COM")
    var objMap = listOf(com).associateBy({it.name}, {it}) as MutableMap
    orbits.filter({it.length > 0}).forEach{
        var s = it.split(")")
        var o0 = objMap.get(s[0])
        if (o0 == null) {
            o0 = SpaceObj(s[0])
            objMap.put(s[0], o0)
        }
        var o1 = objMap.get(s[1])
        if (o1 == null) {
            o1 = SpaceObj(s[1])
            objMap.put(s[1], o1)
        }
        o0.addSatellite(o1)
    }
    return com
}

fun main() {
    var input = 
        """
            COM)B
            B)C
            C)D
            D)E
            E)F
            B)G
            G)H
            D)I
            E)J
            J)K
            K)L
        """.trimIndent()
    assert(createUniverse(input.lines()).totalOrbits() == 42)
    var lines = File("day06.in").readLines()
    println(createUniverse(lines).totalOrbits())

    input =
        """
            COM)B
            B)C
            C)D
            D)E
            E)F
            B)G
            G)H
            D)I
            E)J
            J)K
            K)L
            K)YOU
            I)SAN
        """.trimIndent()
    var com = createUniverse(input.lines())
    var you = com.search("YOU")
    assert(you!!.distance("SAN") == 4)

    com = createUniverse(lines)
    you = com.search("YOU")
    println(you!!.distance("SAN"))
}
