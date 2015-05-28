def sort_names(aList):

	for i in range(len(aList) - 1, 0, -1):
		for j in range(i):
			if(aList[j].split(" ")[1][0] > aList[j+1].split(" ")[1][0]):
				aList[j+1], aList[j] = aList[j], aList[j+1]
	print aList

# A one liner to avoid a bubble sort

def sort_simple(aList):
	print "\n".join(sorted(aList, key = lambda x : x.split(" ")[-1]))

sort_names(["Ashley Yards", "Melissa Banks", "Martin Stove", "Erika Johnson", "Robert Jones"])
sort_simple(["Ashley Yards", "Melissa Banks", "Martin Stove", "Erika Johnson", "Robert Jones"])