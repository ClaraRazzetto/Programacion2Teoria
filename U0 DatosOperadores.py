# Comentario de lìnea ctrl+ç

"""
Comentario
en multiples lineas
Mayus+Alt+A

"""
#Operadores aritméticos

1 + 1     #Suma
8 - 1     #Resta
10 * 2    #Multiplicación (si uno de los operandos es float devuelve float)
5 ** 2    #Potencia
pow(5,2)  #Potencia
2 ** 0.5  #Raiz con Potencia fraccionaria
3 / 5     #Division (devuelve float) error al dividir por cero
3 // 5    #Division entera 
3 % 2     #Modulo

#Operadores lógicos => tipos de datos "boolean"

#not
not True  #False
not False #True

#and
True and True #True

#or
False or False #False

#Cortocircuito por defecto
""" Si tengo una expresión lógica compleja 
y uno de sus términos lanzaría un error
phyton en algunos determina no evaluar ese término utilizando las
propiedades absorventes de los operadores lógicos"""

True and False and 1/0  
#False sabiendo que true and false, ya da False se determina por anticipado el resultado y no se evalua el ultimo término

True and True and 1/0 
#Error debe evaluar todos los terminos para determinar el resultado

False or True or 1/0 
#True analizando los dos primeros términos se puede determinar el resultado

False or False or 1/0
#Error, es necesario evaluar todos los términos para determinar el resultado

#Operadores de Comparación

#Básicos devuelven true o false
1 == 1 
1 != 1
1 < 10
1 > 10
2 >= 2
2 <= 2 

#Combinadas: 
# a diferencia de otros lenguajes se puede combinar 
# operadores de comparación sin necesidad de agregar operadores lógicos 
# La longitud de la combinación es indefinida

1 < 2 < 3             #True
1 < 3 < 2             #False
1 < 0 < 1/0           #False (cortocircuito)
1 <= 2 <= 4 <= 6      #True 
1 != 2 <= 4           #True

# Cadena de Caracteres Strings se usan "" o ''

"Esto es un string"
'Esto es un string' 

#Concatenación
"hola" + "mundo" #hola mundo
"hola" "mundo"   #hola mundo (concatenación automática, no se recomienda)

#Los string tambien funcionan como listas
#podes acceder a los caracteres individuales indicando la posición
"Esto es un string"[0] 
#Me devuelve el caracter 'E' que se encuentra en la posición 0

#Formateo de String: formas de intruducir variables a un string 
# hay 2 formas de hacerlo: 
# usando el método .format() 
# usando la función f-Strings
nombre = "Ezquiel"
precio = 12.5
descuento = 0.8
comida = "lasagña"
 
"{} debe pagar {}$".format(nombre,precio) 
# Ezequiel debe pagar 12.5$

#Agrego indices podemos repetir los parametros
"{0} no vino, {0} se fue, {0} debe aún {1}$ ".format(nombre, precio*descuento)
#Ezequiel no vino, Ezequiel se fue, Ezequiel debe aún 10$

#Agrego un nombre y luego le doy un valor, en este caso no es necesario que estén en orden
"{nombre} quiere comer {comida}".format(comida=comida, nombre="Bob")
#Bob quiere comer lasagña

#Uso de la fucion f-String: el nombre debe coincidir con el de la variable
f'{nombre} quiere comer {comida}'
#Ezequiel quiere comer lasagña

#Objeto None: es un objeto que define una no salida (no es ni falso ni idefinido)

#Operación de identidad is: valida si dos objetos son ideticos (si la posición en memoria es identica) 
#Tanto true, false, none, tienen una única instancia o posición, con un único id, en memoria
True is None  #False
False is None #False
None is None  #True

#Valores interpretados como booleanos

bool(0) #False 
bool(1) #True

bool("")  #False (string vacio)
bool("a") #True (string con contenido)

bool([])  #False (Lista vacia)
bool([3]) #True (lista con cotenido)

#Operaciones lógicas usando valores interpretados como booleanos
#El resultado no siempre es True o False
#Regla: el resultado es el ultimo valor evaluado como True incluyendo cortocircuito

not "1" #False
not []  #True

1 and [3]  # Evalua las dos expresiones: True and True => [3]
[3] and 1  # True and True => 1
#Si uno de los valores en la expresión es 0, se devuelve el resultado de la expresión
[3] and 0  # True and False = False => 0
0 and [3]  # False and True = False => 0
0 and ""   # False and False = False => 0 Aca hay cortocircuito, entonces devuelve el primer valor False
"" and 0   # False and False = False => "" Aca hay cortocircuito, entonces devuelve el primer valor False


#Si hay un True el resultado va a ser True (hay cortocircuito) devuelve el primer valor True
1 or [3]  # 1 True or True
[3] or 1  # [3] True or True
1 or []   # 1 True or False
[] or 1   # 1 False or True
#Si los dos son False debe evaluar toda la expresión, devuelve el último valor evaluado
0 or []   # [] False or False 
[] or 0   # 0 False or False

#Coversiones

#Decimal
str(10)   # 10
int("10") # 10


#Binario
bin(10)          # ‘0b1010’
int("0b1010", 2) # 10
int("1010", 2)   # 10

# Octal
oct(10)          # ’0o12’
int("0o12", 8)   # 10
int("12", 8)     # 10

# Hexadecimal
hex(10)        #’0xa’
int("0xa", 16) # 10
int("0xA", 16) # 10
int("a", 16)   # 10
int("A", 16)   # 10

# En Python soporta Unicode (como estandar de codificacion de caracteres).

chr(65)  # “A”
chr(191) # ”¿”
ord("A") # 65
ord("¿") # 19
