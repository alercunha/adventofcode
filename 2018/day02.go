package main

import (
	"fmt"
	"os"
	"strings"
	"io/ioutil"
)

func find(count int, m map[rune]int) bool {
	for _, v := range m {
		if v == count {
			return true
		}
	}
	return false
}


func part1(input string) interface{} {
    parts := strings.Split(input, "\n")
    twoCount := 0
    threeCount := 0
    for _, part := range parts {
    	letterCount := make(map[rune]int)
    	runes := []rune(part)
		for _, r := range runes {
			v, ok := letterCount[r]
			if ok {
				letterCount[r] = v + 1
			} else {
				letterCount[r] = 1
			}
		}
		if find(2, letterCount) {
			twoCount++
		}
		if find(3, letterCount) {
			threeCount++
		}
    }
    return twoCount * threeCount
}

func part2(input string) interface{} {
	parts := strings.Split(input, "\n")
	letterCountMap := make(map[string]map[rune]int)
	for _, part := range parts {
		letterCount := make(map[rune]int)
		runes := []rune(part)
		for _, r := range runes {
			v, ok := letterCount[r]
			if ok {
				letterCount[r] = v + 1
			} else {
				letterCount[r] = 1
			}
		}
		letterCountMap[part] = letterCount
	}
	return findAnswer(0, parts, letterCountMap)
}

func findAnswer(index int, parts []string, letterCountMap map[string]map[rune]int) string {
	if index == len(parts) - 1 {
		fmt.Println("Could not find an answer")
		os.Exit(1)
	}
	part1 := parts[index]
	letterCount1 := letterCountMap[part1]
	for i := index + 1; i < len(parts); i++ {
		part2 := parts[i]
		letterCount2 := letterCountMap[part2]
		failed := 0
		for k, v1 := range letterCount1 {
			v2, ok := letterCount2[k]
			if ok && v1 != v2 {
				failed++
			}
			if failed > 1 {
				break
			}
		}
		if failed < 2 {
			runes1 := []rune(part1)
			runes2 := []rune(part2)
			runes3 := []rune{}
			for i := 0; i < len(runes1); i++ {
				if (runes1[i] == runes2[i]) {
					runes3 = append(runes3, runes1[i])
				}
			}
			if len(runes3) == len(runes1) - 1 {
				return string(runes3)
			}
		}
	}
	return findAnswer(index + 1, parts, letterCountMap)
}

func assert(f func(string)interface{}, input string, expected interface{}) {
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
	i1 := `abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab`

	assert(part1, i1, 12)

	data := readFile("day02.in")
	fmt.Println(part1(data))

	i2 := `abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz`

	assert(part2, i2, "fgij")
	fmt.Println(part2(data))
}
