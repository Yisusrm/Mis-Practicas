#Funcion con parametros
print("***********Función con parámetros*************")
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


#Funcion sin parametros
print("***********Función sin parámetros*************")
def calcular_area_fija():
  radio = 5
  pi = 3.14159
  area = pi * (radio**2)
  return area

resultado = calcular_area_fija()
print(f"El área del círculo es: {resultado}")