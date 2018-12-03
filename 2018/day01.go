package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

func parse(input string) []string {
	result := []string{}
	parts := strings.FieldsFunc(input, func(r rune) bool {
		if r == '\n' || r == ',' {
			return true
		}
		return false
	})
	for _, part := range parts {
		result = append(result, strings.TrimSpace(part))
	}
	return result
}

func part1(input string) int {
	result := 0
	for _, part := range parse(input) {
		val, err := strconv.Atoi(part)
		if err != nil {
			fmt.Printf("Error converting number: %s\n", err)
			os.Exit(1)
		}
		result += val
	}
	return result
}

func part2(input string) int {
	result := 0
	set := make(map[int]bool)
	for {
		for _, part := range parse(input) {
			set[result] = true
			val, err := strconv.Atoi(part)
			if err != nil {
				fmt.Printf("Error converting number: %s\n", err)
				os.Exit(1)
			}
			result += val
			_, ok := set[result]
			if ok {
				return result
			}
		}
	}
}

func assert(f func(string) int, input string, expected int) {
	result := f(input)
	if result != expected {
		fmt.Printf("Assert failed: got [%d] expecting [%d]\n", result, expected)
		os.Exit(1)
	}
}

func readFile(path string) string {
	b, err := ioutil.ReadFile(path)
	if err != nil {
		fmt.Printf("Error reading file: %s\n", err)
		os.Exit(1)
	}
	return string(b)
}

func main() {
	assert(part1, "+1, +1, +1,", 3)
	assert(part1, "+1, +1, -2", 0)
	assert(part1, "-1, -2, -3", -6)

	data := readFile("day01.in")
	fmt.Println(part1(data))

	assert(part2, "+1, -2, +3, +1", 2)
	assert(part2, "+1, -1", 0)
	assert(part2, "+3, +3, +4, -2, -4", 10)
	assert(part2, "-6, +3, +8, +5, -6", 5)
	assert(part2, "+7, +7, -2, -7, -4", 14)

	fmt.Println(part2(data))
}
