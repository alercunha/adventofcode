package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
	"strconv"
)

type Claim struct {
	id string
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
		claim.id = tokens[0]
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

func part1(input string) interface{} {
	rows := strings.Split(input, "\n")
	claims := parseClaims(rows)
	fmt.Println(claims)
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
					fabric[x][y] = 1
				} else if (fabric[x][y] == 1) {
					fabric[x][y] = 2
					count++
				}
			}
		}
	}
	return count
}

func part2(input string) interface{} {
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
}
