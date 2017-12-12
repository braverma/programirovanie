k=0
f = open("Extinct_languages.tsv", encoding="utf-8") 
	text=f.read()
words=text.split()
for word in words:
	if word == 'critically':
		k+=1
f.close()
print (k)
