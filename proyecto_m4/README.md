# Ecommerce CLI - Modulo 4

Aplicacion de ecommerce por consola hecha con Programacion Orientada a Objetos en Python.

## Archivos

- main.py - punto de entrada del programa
- catalogo.py - clases Producto y Catalogo
- carrito.py - clases ItemCarrito y Carrito
- usuarios.py - clases Usuario, Admin y Cliente
- excepciones.py - excepciones personalizadas

## Como ejecutar

Tener Python 3.8 o superior instalado, luego desde la carpeta del proyecto:

```
python main.py
```

No necesita instalar ninguna libreria externa.

## Roles

- ADMIN: puede listar, crear, actualizar y eliminar productos, y guardar el catalogo en un archivo csv.
- CLIENTE: puede ver el catalogo, buscar productos, agregar al carrito y confirmar compras.

## Archivos que genera el programa

- catalogo.csv: se crea cuando el admin guarda el catalogo. La proxima vez que se inicie el programa, los productos se cargan desde ese archivo.
- ordenes.txt: se genera automaticamente cada vez que un cliente confirma una compra.