#Definir funciones

# Puedo omitir el tipo de variable en los parametros 
# Esta recomendado poner el tipo xq por adelantado 
# te salta error si devolves otro tipo en el return

def dividir(x: float, y:float) -> float: 
    return x/y

#Puedo no tener return: por defecto devuelve None
def dividir(x,y):
    x/y

# Puedo tener + de un return
# Return con multiples valores: devuelve una tupla q se puede desempaquetar
precio: list[float] = [4.04, 5.06, 7.77, 0.09]
def hay_oferta(precio: list[float]) -> tuple[bool,float]:
    precio_mas_bajo = min(precio)
    if precio_mas_bajo < 3:
        return True, precio_mas_bajo
    return False, precio_mas_bajo


#Llamada a la función
dividir(10,8)
#si pongo el nombre del parametro no es necesario que estén en orden esto se llama Keyword
dividir(y=10,x=8) 

existe_oferta , monto = hay_oferta(precio)

#Parámetros arbitrarios: permiten que una función tome una cantidad de parámetros no definida
#Hay dos tipos:
    #Posicionales (*args) llegan en forma de lista a la función
    #De palabra clave (**kwargs) llegan en forma de diccionario (clave=valor)

#Si una funcion recibe parametros fijos y arbitrarios, los arbitrarios deben ir despues de los fijos
def funcionParamArbitrarios(parametro_fijo, *arbitrarios, **kwords):
    return 0
#También se puede hacer de manera inversa: 
# la función espera una lista fija de parámetros, pero se encuentren contenidos en una lista

lista: list[float] = [1.2, 10]
dividir(*lista) #Envio los paramétros a la funcion y esta los desempaqueta automaticamente

#Funciones de orden superior: son funciones que toman otras funciones como parámetros 
#Las funciones se toman como objetos
