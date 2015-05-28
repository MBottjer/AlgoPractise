def printAllCombinations(some_list):
	for x in range(0, len(some_list)):
		for y in range(1,len(some_list)):
			for z in range(2,len(some_list)):
				print some_list[x], some_list[y], some_list[z]

printAllCombinations(example)