# Creando sobrenombres (alias) en Python
a = [1, 2, 3]  # Creando una lista 'a' con elementos [1, 2, 3]
b = a         # Creando un alias 'b' que apunta a la misma lista que 'a'

# Cambiando un valor a través del alias 'b'
b[0] = 5      # Cambiando el primer elemento de la lista a través del alias 'b'

# Debido al alias, el cambio también se refleja en la lista original 'a'
print(a)      # Salida: [5, 2, 3]

# Imprimiendo la lista a través del alias 'b' también muestra el cambio
print(b)      # Salida: [5, 2, 3]