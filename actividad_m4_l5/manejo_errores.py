

# 1. Captura básica de errores

try:
    num1 = float(input("Ingrese el numerador: "))
    num2 = float(input("Ingrese el denominador: "))

    resultado = num1 / num2
    print(f"El resultado es {resultado}")

except ZeroDivisionError:
    print("No es posible dividir por cero.")


# 2. Multiples excepciones
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    resultado = num1 / num2
    print("El resultado es:", resultado)

except ZeroDivisionError:
    print("Error: No puedes dividir por cero.")

except ValueError:
    print("Error: Debes ingresar solo números válidos.")


# 3. Excepciones personalizadas
class EdadInvalidaError(Exception):
    pass

def validar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser negativa.")
    return True

try:
    edad = int(input("Ingresa tu edad: "))
    validar_edad(edad)
    print("Edad válida")

except EdadInvalidaError as e:
    print(f"Error: {e}")

except ValueError:
    print("Error: Debes ingresar un número entero.")


# 4. Limpieza de recursos
try:
    print("Abriendo archivo...")

    num = int(input("Ingresa un número: "))
    resultado = 10 / num

    print("Resultado:", resultado)

except ZeroDivisionError:
    print("Error: No puedes dividir por cero.")

except ValueError:
    print("Error: Debes ingresar un número válido.")

finally:
    print("Cerrando archivo...")