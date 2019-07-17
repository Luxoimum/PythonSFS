# PythonSFS
Python Simple File System es una pequeña API que funciona como servicio interno de carga y descarga de ficheros en una red local. Para ello se utiliza la librería Flask.

### Version 1.0:
-   GET de todas las imagenes
      
        localhost:5000/images
        
-   GET de una imagen

        localhost:5000/images/<name>
        
### Funcionalidad por hacer
-   Crear rama POST para una imagen
-   El GET de todas las imágenes no diferencia entre ficheros y carpetas
-   Contemplar distitnas extensiones de fichero (jpg, jpeg, png, swf, etc)
-   Crear ramas para navegar entre carpetas