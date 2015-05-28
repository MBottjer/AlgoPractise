# def findRotationPoint(words):

# 	floor_index = 0
# 	ceiling_index = len(words) - 1
# 	first_word = words[0]

# 	while(floor_index < ceiling_index):
# 	guess_index = floor_index + ((ceiling_index-floor_index) / 2)

# 		if (words[guess_index] > first_word):
# 		floor_index = guess_index
# 		else:
# 		ceiling_index = guess_index

# 		if (floor_index + 1 == ceiling_index):
# 		print ceiling_index
# 		break

def rotationPoint(array):
	if len(array) == 1:
		return array[0]

	first_word = array[0]
	floor_index = 0
	ceiling_index = len(array) - 1

	while( floor_index < ceiling_index ):
		guess_index = floor_index + (ceiling_index - floor_index) / 2

		if( array[guess_index] > first_word):
			floor_index = guess_index
		else:
			ceiling_index = guess_index

		floor_index += 1
	print ceiling_index

array = ["hello","initiate","joke","karl","ace","beckon","crash","devesh","estimate","forgot","great"]
rotationPoint(array)
# findRotationPoint(array)