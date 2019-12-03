package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
	"strconv"
	"sort"
)

func part1(input string) interface{} {
	return 0
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
	i1 := ``

	assert(part1, i1, 240)
}
