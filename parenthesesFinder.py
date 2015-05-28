def parenthese_finder(opening_position, sentence):

	brackets_map = {"(" : ")"}

	current_brackets = []

	for i in range(opening_position, len(sentence) - 1):

		if(sentence[i] in brackets_map.keys()):
			current_brackets.append(sentence[i])
		elif(sentence[i] in brackets_map.values()):
			if(len(current_brackets) == 1):
				print i
				return
			else:
				current_brackets.pop(-1)

parenthese_finder(10, "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.")
