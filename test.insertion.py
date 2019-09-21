import insertion
A=[]
f=open("Numeros.txt")
lineas=f.readlines()
f.closed
for i in range(len(lineas)):
	a=int(lineas[i])
	A.append(a)
insertion.ordenamiento_insercion(A)
print(A)