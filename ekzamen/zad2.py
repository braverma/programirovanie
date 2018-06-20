files=[itartass1, itartass2, itartass3, itartass4, itartass5, rbk2, rbk3, rbk4, rbk6, rbk7, rian1, rian2, rian3, rian5]
for a in files:	
	f = open(a".html", encoding="utf-8") 
		lines=f.readlines()
	g = open(a'.txt', encoding="cp1251") 
	for x in lines:
		if x[1] == 'w':
			for p in range(len(x)):
				if x[p] in [А, Б, В, Г, Д, Е, Ё, Ж, З, И, Й, К, Л, М, Н, О, П, Р, С, Т, У, Ф, Х, Ц, Ч, Ш, Щ, Ъ, Ы, Ь, Э, Ю, Я]:
					g.write(x[p])
					break
			p+=1
			while x[p] in [а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я]:
				g.write(x[p])
			g.write('\n')
stroki=g.readlines()
for y in stroki:
	t=1
	for z in stroki:
		if len(z)==len(y):
			q=0
			d=0
			while d < len(z) and q==0:
				if y[d]!=z[d]:
					q=1
				d+=1
			if d = len(z):
				t+=1
	