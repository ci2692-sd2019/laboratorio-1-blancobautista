<<<<<<< HEAD
import insertion
A=[]
f=open("Numeros.txt")
lineas=f.readlines()
f.closed
for i in range(len(lineas)):
	a=int(lineas[i])
	A.append(a)
insertion.ordenamiento_insercion(A)
=======
import insertion
A=[]
f=open("Numeros.txt")
lineas=f.readlines()
f.closed
for i in range(len(lineas)):
	a=int(lineas[i])
	A.append(a)
insertion.ordenamiento_insercion(A)
>>>>>>> 0f74d0255afa67eddf616c29d1895267e93ef474
print(A)