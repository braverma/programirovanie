f = open("Extinct_languages.tsv", encoding="utf-8") 
	lines=f.readlines()
w = 'word'
while w!='':
	w = input('Language:')
	for line in lines:
		text=line.split('-')
		if w in text:
			print(text)
			break
		print('Language not in text')
f.close()
		
