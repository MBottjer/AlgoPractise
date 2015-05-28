# Majority number
# ---------------

# Given an array of integer numbers your task is to print to the standard output (stdout) the majority number.
# One number is considered majority if it occurs more than N / 2 times in an array of size N.

# Note: If no number is majority then print "None"

# Expected complexity: O(N) time, O(1) memory

# Example input:
# 1 1 2 3 4 1 6 1 7 1 1
# Example output:
# 1

# Example input:
# 1 2 2 3
# Example output:
# None

def majority(array):
    number_hash = {}
    for number in array:
	    if(number not in number_hash):
		    number_hash[number] = 1
	    else:
		    number_hash[number] +=1
    keys = number_hash.keys()
    values = number_hash.values()
    if(max(values) > len(array)/2):
	    print keys[values.index(max(values))]
    else:
	    print None

# Despite the above algorithm being in O(n) time it is O(n) in space
# The algorithm below is Moore's Voting algorithm and it allows us to find the majority number in O(1) space

# The way it works is by iterating through the numbers in the array, if a number is equal to the predifined majority number it adds one to count, if not it subtracts one.
# If at any point the count = 0 then it sets the majority index as the current iteration and count back to one.
# Essentially, the number that survives for the longest is the number that wins

def findCandidate(array, size):
	majority_index = 0
	count = 1

	for i in range(size):
		if(array[majority_index] == array[i]):
			count +=1
		else:
			count -=1
		if(count == 0):
			majority_index = i
			count = 1
	if(array[majority_index] > size/2):
		print array[majority_index]
	else:
		print None

findCandidate([1,2,22,32,1,5,6,1,10,54,7,9,0,2,28,27], 16)

findCandidate(["a","e","c","d","e","f","g","h"], 8)

