def permutationPalindrome(word):

	frequency_map = {}

	for char in word:
		if char not in frequency_map.keys():
			frequency_map[char] = 1
		else:
			frequency_map[char] += 1

	is_palindrome = True
	seen_odd = False

	for value in frequency_map.values():
		if value % 2 != 0:
			if seen_odd:
				is_palindrome = False
			else:
				seen_odd = True
	print is_palindrome

permutationPalindrome("ass")
permutationPalindrome("civic")
permutationPalindrome("livci")
permutationPalindrome("civil")

# def permutationPalindromeFinder(word):
# parity_map = {}

# for char in word:
# if char not in parity_map.keys():
# parity_map[char] = True
# else:
# parity_map[char] = not parity_map[char]
# print parity_map

# odd_seen = False
# is_palindrome = True

# for has_odd_parity in parity_map.values():
# if has_odd_parity:
# if odd_seen:
# is_palindrome = False
# else:
# odd_seen = True

# print is_palindrome

# permutationPalindromeFinder("ass")
# permutationPalindromeFinder("civic")
# permutationPalindromeFinder("livci")
# permutationPalindromeFinder("civil")