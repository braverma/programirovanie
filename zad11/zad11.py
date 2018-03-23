w = input('File name:')
b=[]
f = open(w, encoding="utf-8") 
	lines=f.readlines()
for line in lines:
	a=re.findall('вып[ьие][юелтвй][штмаоиьсы]?[ьесяий]?[сьяй]?[сяь]?[я]?')
for p in a:
	if p not in b:
		b.append(p)
		print(p)
f.close()
		
