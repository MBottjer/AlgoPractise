# Implement bubblesort

def bubbleSort(alist):
	# first consider that you will need an ever decreaasing array size
	# To achieve this, one needs to produce an array that has the length of the array as its first vale and decreases by one as it iterates through
	for number in range(len(alist)-1,0,-1):
		# At this point I need to iterate through the entire array first and switch pairs as I move along. The largest number will take the last position.
		# Note that after iterating through the entire array, we reduce the size of the array by one as the largest number in the array has been sorted.
		for i in range(number):
			if(alist[i] > alist[i+1]):
				alist[i+1], alist[i] = alist[i], alist[i+1]
	print alist

def shortBubbleSort(alist):
	pairsSwapped = True
	passnum = len(alist)-1
	while passnum > 0 and pairsSwapped:
		pairsSwapped = False
		for i in range(passnum):
			if(alist[i] > alist[i+1]):
				biggest_number = alist[i]
				alist[i+1], alist[i] = alist[i], alist[i+1]
				pairsSwapped = True
		passnum -= 1
	print alist

bubbleSort([1,5,4,7,2,3,9,10,22,12,4,45])
shortBubbleSort([1,5,4,7,2,3,9,10,22,12,4,45])
				