


# read - lectura
"""
archivo = open("notas.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()


# leer linea a linea
f = open("archivo.txt", "r")

for linea in f:
    print(linea)

f.close()


# Escritura / sobrescribe todo lo anterior
archivo = open("archivo.txt", "w")
archivo.write("Toma")
archivo.close()
"""

"""
# append - no borra, solo agrega
f = open("archivo.txt", "a")
f.write("Care perro\n")
f.close()
"""

with open("archivo.txt", "a") as f:
    f.write("Pepito\n")


