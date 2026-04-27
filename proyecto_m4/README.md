# Ecommerce CLI – Módulo 4

Aplicación de comercio electrónico por consola desarrollada con **Programación Orientada a Objetos en Python**.

## Estructura del proyecto

```
ecommerce/
├── main.py          # Punto de entrada
├── catalogo.py      # Clases Producto y Catalogo
├── carrito.py       # Clases ItemCarrito y Carrito
├── usuarios.py      # Clases Usuario (base), Admin y Cliente
├── excepciones.py   # Excepciones personalizadas
├── catalogo.csv     # Generado automáticamente al guardar
└── ordenes.txt      # Generado automáticamente al confirmar compras
```

## Cómo ejecutar

```bash
cd ecommerce
python main.py
```

> Requiere **Python 3.8+**. No necesita librerías externas.

## Roles disponibles

| Rol     | Funcionalidades |
|---------|----------------|
| ADMIN   | Listar, crear, actualizar y eliminar productos; guardar catálogo en CSV |
| CLIENTE | Ver catálogo, buscar, agregar al carrito, ver carrito y confirmar compra |

## Decisiones de diseño

- **Composición**: `Cliente` contiene un `Carrito`; `Catalogo` contiene múltiples `Producto`.
- **Herencia**: `Admin` y `Cliente` heredan de `Usuario`.
- **Excepciones personalizadas**: `ProductoNoEncontradoError`, `CantidadInvalidaError`, `CarritoVacioError`, `ArchivoError`.
- El bloque `finally` en `Carrito.confirmar_compra` garantiza que el carrito se vacíe aunque falle la escritura del archivo.
- El catálogo se carga desde `catalogo.csv` si existe; si no, se usan datos de ejemplo predefinidos.
