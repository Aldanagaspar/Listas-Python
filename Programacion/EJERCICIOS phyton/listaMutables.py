#Podemos modificar uno de sus elementos usando el 
#operador corchetes en el lado izquierdo de una asignación:
fruta = ["plátano", "manzana", "membrillo"]
fruta[0] = "pera"
fruta[-1] = "naranja"
print (fruta)
#['pera', 'manzana', 'naranja']

#Con el operador de porción podemos reemplazar varios elementos a la vez:
#El operador de porción ([inicio:fin]
lista = ['a', 'b', 'c', 'd', 'e', 'f']
lista[1:3] = ['x', 'y']
print (lista)
#['a', 'x', 'y', 'd', 'e', 'f']

#Además, puede eliminar elementos de una lista asignándoles la lista vacía:
lista = ['a', 'b', 'c', 'd', 'e', 'f']
lista[1:3] = []
print (lista)
#['a', 'd', 'e', 'f']

#Y puede añadir elementos a la lista en una porción vacía en la
#posición deseada:
lista = ['a', 'd', 'f']
lista[1:1] = ['b', 'c']
print (lista)
#['a', 'b', 'c', 'd', 'f']
