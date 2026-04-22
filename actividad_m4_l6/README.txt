Diferencia entre write() y append():

* write() abre el archivo en modo escritura ("w") y sobrescribe todo el contenido existente.
* append() abre el archivo en modo añadido ("a") y agrega contenido al final sin borrar lo anterior.

Ventaja de usar with open():

* Cierra el archivo automáticamente, incluso si ocurre un error.
* Hace el código más limpio, seguro y evita olvidar cerrar el archivo manualmente.
