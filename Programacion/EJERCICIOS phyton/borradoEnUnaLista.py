#del elimina un elemento de una lista:
a = ['uno', 'dos', 'tres']
del a[1]
print(a)
['uno', 'tres']

#Puede usar una porción como índice para del:
lista = ['a', 'b', 'c', 'd', 'e', 'f']
del lista [1:5]
print (lista)
['a', 'f']

#Otra forma es por su valor: Mediante la función remove():
Ingredientes= [ "Agua" , "Huevos" , "Aceite" , "Sal" , "Limón" ]
Ingredientes.remove( "Sal" )
print (Ingredientes)
[ "Agua" , "Huevos" , "Aceite" , "Limón" ]

#También otra forma es mediante la función .pop:
Ingredientes= [ "Agua" , "Huevos" , "Aceite" , "Sal" , "Limón" ]
Ingredientes.pop ( 3 )
print (Ingredientes)
[ "Agua" , "Huevos" , "Aceite" , "Limón" ]