def fibonnaci(number):

	if number == 0:
		print 0
		return
	elif number == 1:
		print 1
		return

	first_number = 0
	second_number = 1

	for i in range(1, number):
		new_number = first_number + second_number
		first_number = second_number
		second_number = new_number
	print new_number

fibonnaci(3)
fibonnaci(4)
fibonnaci(5)

def recursiveFibonnaci(number):
	if number == 0:
		return 0
	elif number == 1:
		return 1
	else:
		return recursiveFibonnaci(number-2) + recursiveFibonnaci(number-1)


print recursiveFibonnaci(3)
print recursiveFibonnaci(4)
print recursiveFibonnaci(5)