

# 1. ESCRIBIR EN UN ARCHIVO
# Abrir (o crear) el archivo en modo escritura
archivo = open("datos.txt", "w")

# Escribir líneas en el archivo
archivo.write("Primera linea de texto\n")
archivo.write("Segunda linea de texto\n")
archivo.write("Tercera linea de texto\n")

# Cerrar el archivo
archivo.close()


# 2. LEER EL ARCHIVO COMPLETO
# Abrir el archivo en modo lectura
archivo = open("datos.txt", "r")

# Leer todo el contenido
contenido = archivo.read()

# Mostrar en pantalla
print(contenido)

# Cerrar el archivo
archivo.close()


# 3. LEER LINEA POR LINEA
# Abrir el archivo en modo lectura
archivo = open("datos.txt", "r")

# Leer e imprimir solo la primera línea
primera_linea = archivo.readline()
print("Primera línea:")
print(primera_linea)

# Leer e imprimir el resto línea por línea
print("Resto del archivo:")
for linea in archivo:
    print(linea)

# Cerrar el archivo
archivo.close()


# 4. AÑADIR CONTENIDO (MODO APPEND)
# Abrir el archivo en modo append (añadir)
archivo = open("datos.txt", "a")

# Agregar una nueva línea
archivo.write("Cuarta linea agregada\n")

# Cerrar el archivo
archivo.close()

# Volver a abrir en modo lectura
archivo = open("datos.txt", "r")

# Leer y mostrar el contenido completo
contenido = archivo.read()
print(contenido)

# Cerrar el archivo
archivo.close()


# 5. Atributos y cierre
# Abrir el archivo
archivo = open("datos.txt", "r")

# Mostrar atributos
print("Nombre del archivo:", archivo.name)
print("Modo de apertura:", archivo.mode)
print("¿Está cerrado?:", archivo.closed)

# Cerrar el archivo
archivo.close()

# Verificar nuevamente si está cerrado
print("¿Está cerrado después de close()?:", archivo.closed)