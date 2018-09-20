def Cypher(x,k,l,m,n):
	z = ""
	key = [ k,l,m,n ]
	for i in x:
		a = ord(i)
		for j in key:
			a = (a + j)%126
			if a < 33:
				a = a + 33
		z += chr(a)
	return z

text = input("Texto a cifrar: ")
k = int(input("Ingresa llave: "))
l = int(input("Ingresa llave: "))
m = int(input("Ingresa llave: "))
n = int(input("Ingresa llave: "))

print Cypher(text,k,l,m,n)
