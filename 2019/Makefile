day01.jar: day01.kt
	kotlinc $< -include-runtime -d $@

day01: day01.jar
	java -ea -jar $<

day02.jar: day02.kt
	kotlinc $< -include-runtime -d $@

day02: day02.jar
	java -ea -jar $<

day03.jar: day03.kt
	kotlinc $< -include-runtime -d $@

day03: day03.jar
	java -ea -jar $<

day04.jar: day04.kt
	kotlinc $< -include-runtime -d $@

day04: day04.jar
	java -ea -jar $<

day05.jar: day05.kt day05-lib.kt
	kotlinc $^ -include-runtime -d $@

day05: day05.jar
	java -ea -jar $<

day06.jar: day06.kt
	kotlinc $< -include-runtime -d $@

day06: day06.jar
	java -ea -jar $<

day07.jar: day07.kt day05-lib.kt
	kotlinc $^ -include-runtime -d $@

day07: day07.jar
	java -ea -jar $<

day08.jar: day08.kt
	kotlinc $< -include-runtime -d $@

day08: day08.jar
	java -ea -jar $<
