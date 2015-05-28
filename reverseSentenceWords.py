def reverse_words(sentence):

	new_sentence = ""
	list_of_words = sentence.split()
	
	for i in range(len(list_of_words)-1, -1, -1):
		new_sentence += list_of_words[i] + " "

	print new_sentence

message = 'find you will pain only go you recordings security the into if'
reverse_words(message)