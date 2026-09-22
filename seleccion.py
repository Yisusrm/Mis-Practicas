slc = [4,2,6,8,5,7,0]
def ordenamiento_selec(slc):
    n = len(slc)
    for i in range(n-1):
        indice_min = i
        for j in range(i+1, n):
            if slc[j]<slc[indice_min]:
                indice_min = j
        if indice_min !=i:
            slc[i],slc[indice_min] = slc[indice_min], slc[i]
    return slc
ordenamiento_selec(slc)
print("lista:",slc)