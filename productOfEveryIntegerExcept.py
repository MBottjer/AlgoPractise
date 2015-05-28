# Brute force solution first

def get_products_of_all_ints_except_at_index(array):

	product_array = []

	for index in range(len(array)):
		total_product = 1
		for nest_index in range(len(array)):
			if index != nest_index:
				total_product *= array[nest_index]
		product_array.append(total_product)
	print product_array

get_products_of_all_ints_except_at_index([1,7,3,4])

# To improve on this solution, note that for example

def product_of_values_before(index, array):
	product = 1
	for number in array[0:index]:
		product *= number
	return product

def product_of_values_after(index, array):
	product = 1
	for number in array[index+1:]:
		product *= number
	return product

def second_attempt(array):

	product_array = []

	for index in range(len(array)):
		if index == 0:
			product_array.append(product_of_values_after(index, array))
		elif index == len(array) - 1:
			product_array.append(product_of_values_before(index, array))
		else:
			product_array.append(product_of_values_before(index, array) * product_of_values_after(index, array))
	print product_array

second_attempt([1,7,3,4])

# Third attempt as my refactoring above is still in O(n2), need to come back to this problem
	
				 