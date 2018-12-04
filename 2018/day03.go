package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
	"strconv"
)

type Claim struct {
	id int
	left int
	top int
	width int
	height int
}

func (c Claim) minWidth() int {
	return c.left + c.width
}

func (c Claim) minHeight() int {
	return c.top + c.height
}

func parseClaims(rows []string) []Claim {
	claims := []Claim{}
	for _, row := range rows {
		tokens := strings.Split(row, " ")
		claim := Claim{}
		claim.id, _ = strconv.Atoi(tokens[0][1:])
		edges := strings.Split(tokens[2], ",")
		claim.left, _ = strconv.Atoi(edges[0])
		claim.top, _ = strconv.Atoi(edges[1][:len(edges[1])-1])
		size := strings.Split(tokens[3], "x")
		claim.width, _ = strconv.Atoi(size[0])
		claim.height, _ = strconv.Atoi(size[1])
		claims = append(claims, claim)
	}
	return claims
}

func createFabric(claims []Claim) ([][]int, int) {
	minWidth := 0
	minHeight := 0
	for _, claim := range claims {
		if claim.minWidth() > minWidth {
			minWidth = claim.minWidth()
		}
		if claim.minHeight() > minHeight {
			minHeight = claim.minHeight()
		}
	}
	fabric := make([][]int, minWidth)
	for i := range fabric {
		fabric[i] = make([]int, minHeight)
	}
	count := 0
	for _, claim := range claims {
		for x := claim.left; x < claim.left + claim.width; x++ {
			for y := claim.top; y < claim.top + claim.height; y++ {
				if fabric[x][y] == 0 {
					fabric[x][y] = claim.id
				} else if (fabric[x][y] != -1) {
					fabric[x][y] = -1
					count++
				}
			}
		}
	}
	return fabric, count
}

func part1(input string) interface{} {
	rows := strings.Split(input, "\n")
	claims := parseClaims(rows)
	_, count := createFabric(claims)
	return count
}

func part2(input string) interface{} {
	rows := strings.Split(input, "\n")
	claims := parseClaims(rows)
	fabric, _ := createFabric(claims)
	countMap := make(map[int]int)
	for x := 0; x < len(fabric); x++ {
		row := fabric[x]
		for y := 0; y < len(row); y++ {
			id := row[y]
			if id > 0 {
				v, ok := countMap[id]
				if ok {
					countMap[id] = v + 1
				} else {
					countMap[id] = 1
				}
			}
		}
	}
	for _, claim := range claims {
		v, ok := countMap[claim.id]
		if ok && v == claim.width * claim.height {
			return claim.id
		}
	}
	return 0
}

func assert(f func(string) interface{}, input string, expected interface{}) {
	result := f(input)
	if result != expected {
		fmt.Println("Assert failed: got [", result, "] expecting [", expected, "]")
		os.Exit(1)
	}
}

func readFile(path string) string {
	b, err := ioutil.ReadFile(path)
	if err != nil {
		fmt.Println("Error reading file: ", err)
		os.Exit(1)
	}
	return string(b)
}

func main() {
	i1 := `#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2`

	assert(part1, i1, 4)
	data := readFile("day03.in")
	fmt.Println(part1(data))

	assert(part2, i1, 3)
	fmt.Println(part2(data))
}
