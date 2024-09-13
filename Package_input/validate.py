def validate_number(numero:str, mensaje_error:str):

    while True:
        try:
            retorno = float(numero)
            return retorno
        
        except ValueError:
            numero = input (mensaje_error)

        




    # while numero.isdigit() != True:
    #     numero = input(mensaje_error)

    # numero = int(numero)

    # return numero    






def validate_length(cadena:str, longitud:int, mensaje_error:str):
    retorno = None
    
    while True:
        while cadena.isalpha() is not True or len(cadena) > longitud:
        
            cadena = input(mensaje_error)
            retorno = None
    
        retorno = cadena

        return retorno
