
#creando una lista (se pueden modificar)
lista = ["Alejandra Lopez","Soy Lopez",True,1.85, "Soy Lopez"]

#creando una tupla (no pueden modificar)
tupla = ("Alejandra Lopez","Soy Lopez",True,1.85, "Soy Lopez")

#esto es vàlido
#lista[3] = "Maquinola"

#esto no
#tupla[3] = "Maquinola"


#creando un conjunto (set) (no se accede a elementos por ìndice, no almacena datos duplicados)
conjunto = {"Alejandra Lopez","Soy Lopez",True,1.85, "Soy Lopez"}

#print(conjunto[3]) -> no puede acceder al elemento


#creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : "Alejandra Lopez",
    'canal' : "Soy Lopez",
    'esta_emocionado' : True,
    'altura' : 1.85,
    'dato_duplicado' : "Soy Lopez"
}

print(diccionario['altura'])



