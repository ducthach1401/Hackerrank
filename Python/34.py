def minion_game(string):
	vowels=['E','U','O','A','I']
	consonants=[]
	stuart=0
	kevin=0
	for i in range(65,91):
		if (chr(i) in vowels)==False:
			consonants.append(chr(i))
	for i in range(len(s)):
		if s[i] in consonants:
			stuart=stuart+len(s)-i;
		else:
			kevin=kevin+len(s)-i
	if (stuart>kevin):
		print('Stuart ',stuart)
	elif (stuart<kevin):
		print ('Kevin ',kevin)
	else:
		print('Draw')
s='BAANANAS'
minion_game(s)
