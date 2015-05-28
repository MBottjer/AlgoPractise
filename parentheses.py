def validParentheses(brackets):

	bracket_map = {"{": "}", "[":"]", "(":")"}

	current = []

	is_valid = True

	for bracket in brackets:
		if(bracket in bracket_map.keys()):
			current.append(bracket)
		elif(bracket in bracket_map.values()):
			if(bracket == bracket_map[current[-1]]):
				current.pop(-1)
			else:
				is_valid = False
				return is_valid
	return is_valid


print validParentheses("{[]()}")
print validParentheses("{[(])}")
print validParentheses("{ [ }")
