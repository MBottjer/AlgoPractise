def max_subarray(array):
	max_ending_here = 0
	max_so_far = 0
	for value in array:
		max_ending_here = max(0, max_ending_here + value)
		max_so_far = max(max_so_far, max_ending_here)
	print max_so_far

array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_subarray(array)
array_two = [1,2,3,4,5,6]
max_subarray(array_two)