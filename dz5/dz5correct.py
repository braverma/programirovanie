f = open("text.txt", encoding="utf-8")    # кодировка может быть и другой, но с UTF-8 работать приятнее
text = f.read() 
k=0
p=0
for x in text:
	if x[len(x)-1]=, or x[len(x)-1]=. :
		k+=1
	p+=1
print (100*(1-k/p) '%')
f.close()