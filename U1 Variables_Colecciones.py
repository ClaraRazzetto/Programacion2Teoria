# Asignación de variables

# No hay necesidad de declarar las variables antes de asignarlas
#Varible no asignada => Error
#Convención utilizar guiones bajos y minusculas
una_variable = 5 
# Type-Hints es una sintaxis que permite declarar el tipo de variable (RECOMENDADO)
una_variable : float = 5 

# Operadores con reasignación y asignación múltiple

una_variable += 2 #=> 7
una_variable -= 1 #=> 6
una_variable *= 5        # una_variable == 30
una_variable /= 5        # una_variable == 3.0
una_variable **= 3       # una_variable == 27.0
una_variable %= 10       # una_variable == 7.0
una_variable //= 5       # una_variable == 1.0
# Asignación múltiple
a = b = 3  			     # a = 3 y b = 3

# Colecciones: listas
# Las listas no tienen longitud fija ni tipo de dato predeterminado

lista = []                    	# Vacia
otra = [4, 5, 6]              	# Con valores por defecto
multiple = [2, "Juan", [2]]     # Valores de distinto tipo

# Métodos que se aplican a las listas


lista.append(1)               	# Agregar un elemento al final
lista.extend([2, 4, 3])       	# Agregar múltiples elementos
lista.pop()                  	# Devuelve un elemento de la lista si agregamos el indice como parámetro, si no devuelve el ultimo y lo remueve 
#lista.pop() == 3 y lista == [1,2,4]
lista.insert(3, 3)           	# Agregar un elemento en la posición dada
# .insert(posicion, elemento)
len(lista)                    	# 4 Devuelve la longitud de la lista

# Indexación simple y múltiple en listas:
# Indexado Simple
lista[0]       # => 1 Primer elemento
lista[-1]      # => 4 Último elemento
lista[4]       # Error - Fuera de los límites

# Indexado Múltiple lista [inicio:final:pasos]
lista = [1,2,3,4]
lista[1:3]     # => [2, 3] (del segundo elemento al cuarto sin incluir)
lista[2:]      # => [3, 4] (del tercer elemento en adelante)
lista[:3]      # => [1, 2, 3] (todo hasta el cuarto elemento sin incluir)
lista[::2]     # => [1, 3] (todos los elementos pero con pasos de 2)
lista[::-1]    # => [4, 3, 2, 1] (todos los elementos invertidos)
a = lista[:]   # => Crea una copia idéntica de lista 
a = lista	   # => a es igual a lista. Si cambio lista, cambia a.

#Operaciones con listas
lista + otra  #concatena ambas listas
lista * 2     #concatena la lista consigo misma 2 veces

# Operador in, devuelve true o false
1 in lista 
5 not in lista 
not 5 in lista 

# Operador ==
lista == [1, 2, 4, 3]  # => True
lista == lista[:]      # => True
lista == lista         # => True

# Operador is
lista is [1, 2, 4, 3]  # => False
lista is lista[:]      # => False
lista is lista         # => True

# Operaciones especiales para listas booleanas
any(lista) # => True | Devuelve True si al menos uno de los elementos es True
all(lista) # => True | Devuelve True si todos los elemetos son True 


#Colecciones: tuplas
"""Es un tipo de dato que se usa mayormente de manera 
implícita. La diferencia entre una tupla y una lista es que la 
tupla es inmutable. Esto quiere decir que una vez definida la 
tupla no puede modificarse. """

tupla = (1, 2, 3) # Se definen con (,) en lugar de []
tupla = 1, 2, 3 # Los paréntesis son opcionales
tupla[0] # => 1
tupla[0] = 3 # TypeError

# Métodos idénticos a las listas pero sin asignación

len(tupla) # => 3
tupla + (4, 5, 6) # => (1, 2, 3, 4, 5, 6)
tupla[:2] # => (1, 2)
2 in tupla # => True

# Desempaquetado

# Desempaquetado Simple
a, b, c = (1, 2, 3) # a == 1, b == 2, c == 3
a, b, c = [1, 2, 3] # a == 1, b == 2, c == 3
a, b = [1, 2, 3]    # Error | Cantidad de elementos debe ser idéntica
a, b = b, a         # Intercambio a == 2, b == 1

# Desempaquetado Con comodines
a, *rest = [1, 2, 3, 4]    # a == 1, rest == [2, 3, 4]
*rest, b = [1, 2, 3, 4]    # b == 4, rest == [2, 3, 4]
a, *rest, b = [1, 2, 3, 4] # a == 1, b == 4, rest == [2, 3]

# Desempaquetado Anidado
(a, b), c = [[1, 2], [3]]  # a == 1, b == 2, c == [3]         