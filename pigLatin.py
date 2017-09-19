#!/usr/bin/python

print "Input a word or name to translate to pig latin (or 0 to exit)"
initialWord = raw_input()

while (initialWord != '0') :
	if(initialWord.isalpha()):
		count = 0
		while (count < len(initialWord) and initialWord[count] not in 'aeiou'):
			count += 1
		if (count == len(initialWord)):
			print initialWord + 'ay'
		else :
			print initialWord[count:] + initialWord[:count] + 'ay'
	else:
		print "Sadly, that doesn't translate"
	print "Input a word or name to translate to pig latin (or 0 to exit)"
	initialWord = raw_input()
