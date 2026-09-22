cal = [9.0, 8.5, 7.8, 9.5, 9.2, 8.0, 7.5, 10.0, 9.9, 8.6, 8.1, 9.3, 8.2, 9.6, 9.5]
n = len(cal)
swapped = True
while swapped:
    swapped = False
    for i in range(n-1):
        if cal[i]>cal[i+1]:
            cal[i],cal[i+1] = cal[i+1],cal[i]
            swapped = True
print("Orden Ascendente:", cal)

#ORDEN DESCENDENTE
print("*****************************************************************")
swapped = True
while swapped:
    swapped = False
    for j in range(n-1):
        if cal[j]<cal[j+1]:
            cal[j],cal[j+1] = cal[j+1],cal[j]
            swapped = True
print("Orden Descendente:", cal)