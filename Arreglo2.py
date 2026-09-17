Lista = [10, 20, 30, 40, 50, 60]
#Primera forma de recorrer arreglos
for x in Lista:
    print(x)
print("********************************************")
#Segunda forma de recorrer arreglos
for i in range(len(Lista)):
    print (Lista[1])
print("********************************************")
#Para imprimir un solo elemento
print(Lista[0])
print("********************************************")
#En forma rebanado o segmentación
print(Lista[0:5])
print("********************************************")
#Metodo de Ordenamiento Burbuja 
Lista1 = [29, 10, 14, 100]
n = len(Lista1)
swapped = True
while swapped:
    swapped = False
for i in range(n-1):
    if Lista1[i]>Lista1[i+1]:
        Lista1[i],Lista1[i+1]= Lista1[i+1],Lista1[i]
        swapped = True
print("Lista ordenada:", Lista1)