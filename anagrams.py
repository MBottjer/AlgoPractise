def find_anagrams(word_array):
    
    anagrams = []

    for word in word_array:
        for word_to_compare in word_array:
            if set(word) == set(word_to_compare) and word != word_to_compare:
                anagrams.append(word)
                anagrams.append(word_to_compare)
    print set(anagrams)

find_anagrams(['bat', 'rats', 'god', 'dog', 'cat', 'arts', 'star'])