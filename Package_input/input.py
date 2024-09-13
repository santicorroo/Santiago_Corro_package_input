from Package_input.validate import *

def get_int(mensaje:str, mensaje_error:str):
    while True:
        
        numero = input(mensaje)
        
        validacion = validate_number(numero, mensaje_error)

        return validacion

        





def get_float(mensaje:str, mensaje_error:str):
    
    flotante = input(mensaje)

    validacion = validate_number(flotante, mensaje_error)

    return validacion




def get_string(mensaje:str, mensaje_error:str, longitud:int ):
    cadena = input(mensaje)

    validacion = validate_length(cadena, longitud, mensaje_error)

    return validacion

