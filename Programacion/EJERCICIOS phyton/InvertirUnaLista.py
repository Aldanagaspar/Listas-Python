#Opción 1: Mediante troceado de listas con step negativo:
Lista = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
Lista = Lista[::-1]
print (Lista)
['Limón', 'Sal', 'Aceite', 'Huevos', 'Agua']

#Opción 2: Mediante la función reversed():
Lista = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
Lista = list(reversed(Lista))
print(Lista)
['Limón', 'Sal', 'Aceite', 'Huevos', 'Agua']