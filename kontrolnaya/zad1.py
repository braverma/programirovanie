f = open("Extinct_languages.tsv", encoding="utf-8") 
	lines=f.readlines()
for x in lines:
	if len(x)>35:
		print(x)
f.close()
