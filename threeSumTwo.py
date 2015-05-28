def threeSum(array):
	sorted_array = sorted(array)

	for i in range(0, len(array)-3):
		x = sorted_array[i]
		start = i + 1
		last = len(sorted_array) - 1

		while start < last:

			y = sorted_array[start]
			z = sorted_array[last]

			if x + y + z == 0:
				print x, y, z
				start += 1
				last -= 1
			elif x + y + z > 0:
				last -= 1
			else:
				start += 1

threeSum([1, -10, 15, -5, 6, -8, 2, 0, 2, -2, 4, -6, 2])

		