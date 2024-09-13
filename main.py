

def get_int(mensaje:str, mensaje_error:str, maximo:int, minimo:int, reintentos:int):
    contador = 0
    numero = int(input(mensaje))
    while numero > maximo or numero < minimo:
        numero = int(input(mensaje_error))
        contador += 1
        if contador == reintentos:
            numero = None
            return None
        
    return numero

resultado = get_int("Ingrese un numero", "Reingrese un numero valido", 1000, 1, 3)

print(resultado)


def get_str(mensaje:str, mensaje_error:str, longitud:int, reintentos:int):
    contador = 0

    cadena = input(mensaje) 

    while len(cadena) < longitud or len(cadena) > longitud:
        cadena = input(mensaje_error)
        contador+=1
        if contador == reintentos:
            return None
    
    return cadena
    
resultado = get_str("Ingrese una cadena", "Reingrese una cadena valida", 6, 3)

print(resultado)

