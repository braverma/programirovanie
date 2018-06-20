files=[itartass1, itartass2, itartass3, itartass4, itartass5, rbk2, rbk3, rbk4, rbk6, rbk7, rian1, rian2, rian3, rian5]
for a in files:	
	f = open(a".html", encoding="utf-8") 
		lines=f.readlines()
	g = open(a'.txt', encoding="cp1251") 
	for x in lines:
		if x[1] == 't':
			g.write(x[7:-8])
		if x[1] == 'p':
			g.write('\n')
		if x[1] == 'w':
			for j in range (len(x)):
				if x[j]=='a' and x[j+1] == '>':
					q = j+2
					break
			while x[q] != '\'':
				g.write(x[q])
				q+=1
			while x[q+1] != '<':
				g.write(x[q+1])
				q+=1
			if x[-2]=='e':
				g.write(x[q+5])		
	g.close()
	f.close()
