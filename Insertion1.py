
def ordenamiento_insercion(A:list)->list:
	for x in range(1,len(A)):
		Casilla=A[x]
		i=x-1
		while i>=0 and Casilla<A[i]:
				A[i+1]=A[i]
				A[i]=Casilla
				i=i-1
	return A
