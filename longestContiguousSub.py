# Longest improvement
# ---------------------

# A student's performance in lab activities should always improve, but that is not always the case.
# Since progress is one of the most important metrics for a student, lets write a program that computes the longest period of increasing performance for any given student.
# For example, if his grades for all lab activities in a course are: 9, 7, 8, 2, 5, 5, 8, 7 then the longest period would be 4 consecutive labs (2, 5, 5, 8).

# Given an array with the lab grades of a student
# Your task is to write a function that computes and prints to standard output (stdout) the longest period of increasing performance for the student that has these grades
# Note that your function will receive the following arguments: grades, which is an array containing the grades of the student

def longest_improvement(grades):
	# There are two things we need consider: the increasing list we're analysing and the current maximum increasing list
	# We know by default that the smallest possible length is 1 given this is the largest if no numbers increase
	current_length = 1
	maximum_length = 1

	previous_value = grades[0]
	# When iterating through the array, we want to consider whether the current i is greater than the previous hence, we start at 1
	for value in grades[1:]:
		if(value >= previous_value):
			current_length += 1
		else:
			maximum_length = max(current_length, maximum_length)
			current_length= 1
		previous_value = value
	# If I reach the end of the array and I have a set of icnreasing values, I will have a current list and maximum list to compare. Hence, I need th maximum
	print max(maximum_length, current_length)

longest_improvement([9, 7, 8, 2, 5, 5, 8, 7])

# The algorithm runs in O(n), given that it iterates through N numbers in the array