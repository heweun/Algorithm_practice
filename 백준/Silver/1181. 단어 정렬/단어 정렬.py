N, *word_list = open(0).read().split()
word_list = sorted(set(word_list), key=lambda x:(len(x),x))
print(*word_list, sep='\n')