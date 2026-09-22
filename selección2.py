ls = [4,2,6,8,5,7,0]
for i in range(len(ls)):
    minimo = i 
    for j in range (i, len(ls)):
        if ls[j] < ls[minimo]:
            minimo = j
    aux = ls[i]
    ls[i] = ls[minimo]
    ls[minimo] = aux
print("Ordenamiento por selección:", ls)