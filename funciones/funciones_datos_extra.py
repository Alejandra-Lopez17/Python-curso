#creando una funcion de 3 parametros

#def frase(nombre,apellido,adjetivo):
#    return f'Hola {nombre} {apellido}, eres muy {adjetivo}'

#utilizando keyword arguments
#frase_resultante = frase(adjetivo = "capo",nombre = "Alejandra",apellido ="Lopez")


#creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo = "Tonto"):
    return f'Hola {nombre} {apellido}, eres muy {adjetivo}'

frase_resultante = frase("Alejandra","Lopez","inteligente")
print(frase_resultante)

