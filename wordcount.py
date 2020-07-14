# put your code here.
import sys
from collections import Counter
def make_word_counts_dict(filename):
	"""returns dict of count of each word in the file"""
	# for line in fileinput.input():
	# 	process(line)
	test_file = open(filename)
	words_count = {}
	file_words_list = []
	file_words_list2 = []
	punctuation = [',', '?','.','-','"',';',':']
	
	for words in test_file:
		if words in punctuation:
			words.rstrip()
		else:
			words=words.lower()
			words = words.rstrip("\n").split(" ")
			file_words_list.extend(words)
	print(file_words_list)
	# print(file_words_list)
	words_count = Counter(file_words_list)
	# for word in file_words_list:
	# 	# words_count[word] = words_count.get(word, 0) + 1
	# 	words_count[word]=Counter(word)
	# words = findall(r'\w+', open(filename).read().lower())
	# for word in words:
	# 	cnt[word] += 1
	
	
	print(words_count)	
	return words_count

make_word_counts_dict(sys.argv[1])
# make_word_counts_dict(sys.argv[2])


# import sys
# from collections import Counter
# def make_word_counts_dict(filename):
# 	"""returns dict of count of each word in the file"""
	
# 	test_file = open(filename)
# 	words_count = {}
# 	file_words_list = []
# 	file_words_list2 = []
# 	punctuation = [',', '?','.','-','"',';',':']
	
# 	for words in test_file:
# 		if words in punctuation:
# 			words.rstrip()
# 		else:
# 			words=words.lower()
# 			words = words.rstrip("\n").split(" ")
# 			file_words_list.extend(words)
# 	print(file_words_list)
# 	words_count = Counter(file_words_list)

	
# 	print(words_count)	
# 	return words_count

# make_word_counts_dict(sys.argv[1])