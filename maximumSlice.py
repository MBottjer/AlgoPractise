# First I'm going to try and build an O(n^3)

def rubbishMaxSlice(array):
	length = len(array)

	current_maximum = 0
	result = 0

	for i in range(length):
		# print "this is the first iterator: ", i
		for j in range(i,length):	
			# print "this is the second iterator: ", j
			sum_so_far = 0
			for value in range(i, j+1):
				# print "this is the third iterator: ", value
				sum_so_far += array[value]
			result = max(result, sum_so_far)
	print result

rubbishMaxSlice([5,-7,3,5,-2,4,-1])

# we can improve upon this by utilising Kadane's algorithm as follows:

def maxSlice(array):

	maximum_ending_here = 0
	maximum_so_far = 0

	for number in array:
		maximum_ending_here = max(0, maximum_ending_here + number)
		maximum_so_far = max(maximum_so_far, maximum_ending_here)
	print maximum_so_far

maxSlice([5,-7,3,5,-2,4,-1])