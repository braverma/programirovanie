a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
if a + b == c and a/b == c:
	print ('Usloviya 1 i 5 vypolneny')
elif a + b == c:
	print ('Uslovie 1 vypolneno, 5 - net')
elif a/b == c:
	print ('Uslovie 5 vypolneno, 1 - net')
else:
	print ('Uslovie 1 i 5 ne vypolneny')