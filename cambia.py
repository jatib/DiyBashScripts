def Cypher(x,k,l,m,n):
	z = ""
	for i in x:
		print " _Step 1: ",i,":",ord(i),":",( ord(i) + k )%126," _Step 2: ",( ( ord(i) + k )%126 + l )%126," _Step 3: ",( ( ( ord(i) + k )%126 + l )%126 + m )%126," _Step 4: ",( ( ( ( ord(i) + k )%126 + l )%126 + m )%126 + n )%126
		z += chr( ( ( ( ( ord(i) + k )%126 + l )%126 + m )%126 + n )%126 )
	return z

text = input("Texto a cifrar: ")
k = int(input("Ingresa llave: "))
l = int(input("Ingresa llave: "))
m = int(input("Ingresa llave: "))
n = int(input("Ingresa llave: "))

print Cypher(text,k,l,m,n)
