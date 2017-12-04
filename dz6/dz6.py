word='o'
with open("latin.txt", "w", encoding="utf-8") as f:
	while word!='':
		word = input("Latin word:")
		if (word[len(word)-1]=="e" or word[len(word)-1]=="i") and word[len(word)-2]==r:
			f.write(word)
	f.close()
