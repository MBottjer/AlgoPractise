def threeSum(some_list):
	sorted_list = sorted(some_list)

	for i in range(0, len(sorted_list)-3):
		x = sorted_list[i]
		start = i + 1
		last = len(sorted_list)-1

		while(start < last):

			y = sorted_list[start]
			z = sorted_list[last]

			if x + y + z == 0:
				print x, y, z
				start += 1
				last -= 1
			elif x + y + z > 0:
				last -= 1
			else:
				start += 1

example = [1, -10, 15, -5, 6, -8, 2, 0, 2, -2, 4, -6, 2]
threeSum(example)


	