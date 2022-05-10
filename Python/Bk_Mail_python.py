#MOLUDOS
import os
import time
from pathlib import Path
import tarfile

#VARIABLES
ruta_script = Path("/home/gabriel/Documents/")
fecha_y_hora = time.strftime("%d-%m-%y_%H-%M-%S")
fecha = time.strftime ("%d-%m-%y")
nombre_archivo = f"Thunder_{fecha}.tgz"
carpeta_destino = ruta_script / "Bk_email_automatico"
carpeta_respaldar = "/home/gabriel/.thunderbird"
archivo_log = carpeta_destino / "log.txt"
archivo_comprimido = carpeta_destino / nombre_archivo
dias = 14
ahora = time.time()
#-----------------------------------------------------------------------------------------#

# Creamos el directorio para los respaldos por si no existe
try:
    os.mkdir(carpeta_destino)
except OSError:
    print(f"La creación del directorio %s falló porque ya existe --> {fecha_y_hora}" % carpeta_destino, file= open (archivo_log, "a") )
else:
    print(f"Se ha creado el directorio: %s --> {fecha_y_hora}" % carpeta_destino, file= open (archivo_log, "a") )


# Creamos un condicional para verificar si existe y no duplicar, de manera indirecta evito el uso excesivo de espacio
# Ademas implemento el uso de logs para verificar en un archivo los fallos del programa y
# Procedemos a comprimir con tar en formato gz

if os.path.exists(carpeta_destino / nombre_archivo):
    print(f"El archivo no se creo, porque ya existe un archivo con el mismo nombre--> {fecha_y_hora}", file= open (archivo_log, "a") )
else:
    tar = tarfile.open(archivo_comprimido, "w:gz")
    os.chdir(carpeta_respaldar)
    for name in os.listdir("."):
       tar.add(name)
       print(name)
    tar.close()
    print(f"El proceso de backup finalizo exitosamente--> {fecha_y_hora}", file= open (archivo_log, "a"))

# Hacemos un for para revisar el directorio donde buscamos solo los archivos que comiencen con 'Test'
# para luego verificar que solo borrremos los mayores a X dias

for filename in os.listdir(carpeta_destino):
    if filename.startswith("Thunder"):
        if os.path.getmtime(os.path.join(carpeta_destino, filename)) < ahora - (dias * 86400):
            if os.path.isfile(os.path.join(carpeta_destino, filename)):
                print(filename)
                os.remove(os.path.join(carpeta_destino, filename))
                print(f"Se borraron backups antiguos {filename}--> {fecha_y_hora}", file= open (archivo_log, "a"))
    else:
        print(f"No se encontraron Backups viejos para borrar --> {fecha_y_hora}", file= open (archivo_log, "a"))

