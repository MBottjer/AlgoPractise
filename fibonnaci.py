# 0, 1, 1, 2, 3, 5, 8

# Iteratively

def fibonnaci(number):

	if number == 0:
		return 0
	if number == 1:
		return 1

	current_sum = 0
	first = 0
	second = 1

	for numb in xrange(2,number):
		current_sum = first + second
		first = second
		second= current_sum

	print current_sum

fibonnaci(6)


# Recursively

def recursiveFibonacci(number):
	if number == 0: return 0
	elif number == 1: return 1
	else: return recursiveFibonacci(number-1)+recursiveFibonacci(number-2)

print recursiveFibonacci(5)

# Dynamic programming

def dynamicFibonnacci(number):
	

