# Don't forget to run the tests (and create some of your own)

from multiprocessing.connection import answer_challenge


def anagrams_for(word, list_of_words):
		sorted_word = sorted(word)
		ans = []
		for x in list_of_words:
			sorted_elem = sorted(x)

			if sorted_elem == sorted_word:
				ans.append(x)
		
		return ans
	
