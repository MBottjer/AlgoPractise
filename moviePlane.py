# O(n^2) solution first

def findTwoFilms(flightLength, movieLengths):

	for i in range(0,len(movieLengths)-1):
		for j in range(i+1, len(movieLengths)):
			if movieLengths[i] + movieLengths[j] == flightLength:
				print movieLengths[i], movieLengths[j]

findTwoFilms(6, [3,2,4,1,3,10,5])

# To improve upon this method perhaps I can sort the values first. Failed attempt!

# def sortedFilmFinder(flightLength, movieLengths):

# 	sorted_movieLengths = sorted(movieLengths)
# 	floor_index = 0
# 	ceiling_index = len(movieLengths) - 1

# 	while floor_index <= ceiling_index:
# 		guess_index = (floor_index + ceiling_index) / 2
# 		if sorted_movieLengths[floor_index] +  sorted_movieLengths[guess_index] < flightLength:
# 			floor_index = guess_index
# 		elif sorted_movieLengths[ceiling_index] + sorted_movieLengths[guess_index] > flightLength:
# 			ceiling_index = guess_index
# 		elif sorted_movieLengths[floor_index] + sorted_movieLengths[ceiling_index]:
# 			print sorted_movieLengths[floor_index], sorted_movieLengths[ceiling_index]


# sortedFilmFinder(6, [3,2,4,1,3,10,5])

# Optimal solution

def get_two_movies_to_fill_flight(flight_length, movie_lengths):

	movie_lengths_seen_hash = {}

	for first_movie_length in movie_lengths:

		matching_second_movie_length = flight_length - first_movie_length
		if matching_second_movie_length in movie_lengths_seen_hash:
			print True
			return

		movie_lengths_seen_hash[first_movie_length] = True

	print False

get_two_movies_to_fill_flight(6, [9,2,4,1,3,10,5])	


