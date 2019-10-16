os.makedirs(articles)
import os
for i in os.listdir(os.getcwd(union)):
	f = open (i)
	data=f.readlines()
	for p in data:
		a=p.find('{id')
		if a!=-1:
			d.close
			d=open (union, 'p.tsv', 'w')
		d.write (p)
	d.close
	i.close