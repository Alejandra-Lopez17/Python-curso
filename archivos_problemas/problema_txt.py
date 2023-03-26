#2 listas, una con nombres otra con apellidos
nombres = ["Alejandra","Andrea","Ruby","Roberto","Fernando"]
apellidos = ["Lopez","Ospino","Hernandez","Gabiria","Escobar"]

#Registrar esta información en un TXT de forma óptima

with open("archivos_problemas\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-----------\n") for n,a in zip(nombres,apellidos)]
    