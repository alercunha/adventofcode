package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
	"strconv"
	"sort"
)

type Entry struct {
	id int
	date string
	asleep [60]int
	asleepSum int
	asleepMostFrequently int
}

func parseEntries(rows []string) []*Entry {
	sort.Strings(rows)
	entry := &Entry{}
	entries := []*Entry{}
	falls := -1
	for _, row := range rows {
		parts := strings.Split(row, " ")
		if parts[2] == "Guard" {
			entry = &Entry{}
			entries = append(entries, entry)
			entry.id, _ = strconv.Atoi(parts[3][1:])
			entry.date = parts[0][6:]
			falls = -1
		} else if parts[2] == "falls" {
			falls, _ = strconv.Atoi(parts[1][3:5])
			entry.asleep[falls] = 1
			entry.asleepSum++
		} else if parts[2] == "wakes" {
			wakes, _ := strconv.Atoi(parts[1][3:5])
			for i := falls + 1; i < wakes; i++ {
				entry.asleep[i] = 1
				entry.asleepSum++
			}
		}
	}
	return entries
}

func combineEntries(entries []*Entry) []*Entry {
	entryMap := make(map[int]*Entry)
	for _, entry := range entries {
		v, ok := entryMap[entry.id]
		if ok {
			for i := 0; i < len(entry.asleep); i++ {
				v.asleep[i] = v.asleep[i] + entry.asleep[i]
			}
			v.asleepSum = v.asleepSum + entry.asleepSum
		} else {
			root := &Entry{}
			root.id = entry.id
			root.date = "all"
			root.asleepSum = entry.asleepSum
			copy(root.asleep[:], entry.asleep[:])
			entryMap[entry.id] = root
		}
	}
	combined := []*Entry{}
	for _, v := range entryMap {
		_, v.asleepMostFrequently = findMax(v.asleep)
		combined = append(combined, v)
	}
	return combined
}

func findMax(values [60]int) (int, int) {
	max := 0
	idx := 0
	for i := 0; i < len(values); i++ {
		if values[i] > max {
			max = values[idx]
			idx = i
		}
	}
	return idx, max
}

func part1(input string) interface{} {
	rows := strings.Split(input, "\n")
	entries := parseEntries(rows)
	combined := combineEntries(entries)
	sort.Slice(combined, func(i, j int) bool {
		return combined[i].asleepSum > combined[j].asleepSum
	})	
	//for _, entry := range combined {
	//	fmt.Println(*entry)
	//}
	idx, _ := findMax(combined[0].asleep)
	return idx * combined[0].id
}

func part2(input string) interface{} {
	rows := strings.Split(input, "\n")
	entries := parseEntries(rows)
	combined := combineEntries(entries)
	sort.Slice(combined, func(i, j int) bool {
		return combined[i].asleepMostFrequently > combined[j].asleepMostFrequently
	})
	//for _, entry := range combined {
	//	fmt.Println(*entry)
	//}
	idx, _ := findMax(combined[0].asleep)
	return idx * combined[0].id
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
	i1 := `[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up`

	assert(part1, i1, 240)

	data := readFile("day04.in")
	fmt.Println(part1(data))

	assert(part2, i1, 4455)
	fmt.Println(part2(data))
}
