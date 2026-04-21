
# try y except
'''
try:
    lista = [1,2,3,4,5,6,7,8]
    print(lista[9])

except IndexError:
    print(f"Error: Fuera de rango, la lista solo tiene {len(lista)} datos")

except ValueError:
    print("Error: No letras por favor")

except SyntaxError:
    print("Error: Revisa tu código") 



try:
    a = int(input("Ingresa un número: "))
    b = int(input("Ingresa un número: "))
    resultado = a/b
except ValueError:
    print("Error: Ingresar solamente números por favor")

except ZeroDivisionError:
    print("Error: No es posible dividir por cero")



# raise, else y finally

edad = -5

try:
    edad = int(input("Ingresa tu edad: "))
    if edad < 0:
        raise ValueError("Error de edad") # el raise forza el error si la validacion salio mal
    
except Exception as e: # la clase exception captura todos los errores
    print(f"Error capturado desde el bloque try: {e}")

else: # el else se ejecuta si todo sale bien y no hay errores
    print("Todo salió bien, felicidades.")

finally: # se ejecuta cuando termina el proceso, haya o no errores
    print("Proceso terminado y completado con manejo de errores.")

'''
import re

try:
    nombre = input("Ingrese su nombre: ")
    nota = float(input("Ingrese su nota: "))

    if re.match(r'^[A-Za-záéíóúÁÉÍÓÚñÑ]+$', nombre):
        print("Esto es un nombre válido")
    else:
        raise re.error("Error de regex")

    # validar nota
    if nota < 1 or nota > 7:
        raise ValueError("La nota debe ser entre 1 y 7")
    
    # open, abrir el archivo en modo append
    archivo = open("notas.txt", "a")

except re.error as r:
    print(f"error del regex")

except Exception as e:
    print(f"Errores capturados desde el bloque try: {e}")

else:
    # Esto se va a ejecutar si todo salió bien
    archivo.write(f"{nombre}, {nota}")
    print("Datos guardados correctamente.")

finally:
    try:
        archivo.close()
        print("Archivo cerrado.")
    except:
        print("No se puede cerrar un archivo que no existe.")