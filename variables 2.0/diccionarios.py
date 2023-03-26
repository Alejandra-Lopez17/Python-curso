#creando diccionarios con dict()
diccionario = dict(nombre="alejandra",apellido="lopez")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["lopez","pasada" ]):"jajas"}

#creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"],"No se")



print(diccionario["nombre"])