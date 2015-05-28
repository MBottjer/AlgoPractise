# def get_premutations(word):

# 	if len(word) <= 1:
# 		return [word]

# 	all_characters_except_last = word[:-1]
# 	last_character = word[-1]

# 	permutations_of_all_chars_except_last = get_premutations(all_characters_except_last)

# 	possible_positions_to_put_last_char_in = range(len(permutations_of_all_chars_except_last)+1)

# 	for permutation in permutations_of_all_chars_except_last:
# 		for position in possible_positions_to_put_last_char_in:
# 			permutation = permutations_of_all_chars_except_last[:position] + last_character + permutations_of_all_chars_except_last[position:]
# 			permutations.append(permutation)
# 	return permutations

def get_permutations(word):

	if len(word) <= 1:
		return [word]

	word_without_last_char = word[:-1]
	last_char = word[-1]

	permutations_of_all_chars_except_last = get_permutations(word_without_last_char)

	permutations = []

	for permutation in permutations_of_all_chars_except_last:

		for i in range(len(permutations_of_all_chars_except_last)+1):

			permutations.append(permutation[:i] + last_char + permutation[i:])

	return permutations

print get_permutations("abc")