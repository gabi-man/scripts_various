#MOLUDOS
import os
import time
import tarfile
from pathlib import Path
from dirsync import sync



#VARIABLES
ruta_script = Path("/home/gabriel/Documents/Scripts varios/Python")
fecha_y_hora = time.strftime("%d-%m-%y_%H-%M-%S")
fecha = time.strftime ("%d-%m-%y")
nombre_archivo = f"Test_{fecha}.tgz"
carpeta_destino = ruta_script / "respaldos_prueba"
carpeta_respaldar = "/home/gabriel/Documents/cosas_importantes"
archivo_log = carpeta_destino / "log.txt"
archivo_comprimido = carpeta_destino / nombre_archivo
dias = 2
ahora = time.time()
target_path = '/mnt/compartida81/'
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
    if filename.startswith("Test"):
        if os.path.getmtime(os.path.join(carpeta_destino, filename)) < ahora - (dias * 86400):
            if os.path.isfile(os.path.join(carpeta_destino, filename)):
                print(filename)
                os.remove(os.path.join(carpeta_destino, filename))
                print(f"Se borraron backups antiguos {filename}--> {fecha_y_hora}", file= open (archivo_log, "a"))
        else:
            print(f"No se econtraron Backups viejos para borrar --> {fecha_y_hora}", file= open (archivo_log, "a"))
    
"""
Para que que se pueda copiar por red desde el recurso local a la carpeta compartida (en este caso en dominio con credenciales)
hay que crear una carpeta en ubuntu para luego montarle el recurso compartido y 
a parti de aca poder copiar y gestionar los archivos. Para mas informacion leer adjunto creado en drive
"""
#Con la libreria sync se sincronizan las carpetas en un sentido, borrando en destino lo que no este en el origen
sync(carpeta_destino, target_path, 'sync', purge=True) #for syncing one way

