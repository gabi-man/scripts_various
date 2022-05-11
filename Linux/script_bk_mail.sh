#!/bin/bash
RUTA_SCRIPT=`dirname ${BASH_SOURCE[0]}`
FECHA_Y_HORA=`date "+%d-%m-%y_%H-%M-%S"`
FECHA=`date "+%d-%m-%y"`
NOMBRE_ARCHIVO="Thunder_$FECHA.tgz"
LINES=0
CARPETA_DESTINO="$RUTA_SCRIPT/Bk_email_automatico"
# Nota: la carpeta a respaldar puede ser otra, pero si no es relativa al script, pon su ruta completa
CARPETA_RESPALDAR="/home/gabriel/.thunderbird"
# Creamos el directorio para los respaldos por si no existe
crear_carpeta()
{
  mkdir -p "$CARPETA_DESTINO"
}

#Creamos un condicional para verificar si existe y no duplicar, de manera indirecta evito el uso excesivo de espacio
#Ademas implemento el uso de logs para verificar en un archivo los fallos del programa
comprimir_archivo()
{
if [ -f /home/gabriel/Documents/Bk_email_automatico/$NOMBRE_ARCHIVO ];then
  echo "El archivo no se creo,porque ya existe un archivo con el mismo nombre-->  $FECHA_Y_HORA" >> $CARPETA_DESTINO/log.txt;
  echo "El proceso de backup finalizo con errores. Ver Logs"
else
#Comprimo con TAR  c es para crear, la v para que sea verboso o imprima mensajes de debug, la z para que los archivos sean comprimidos con gzip 
#y f para que opere sobre el archivo   	
  tar cfvz "$CARPETA_DESTINO/$NOMBRE_ARCHIVO" --absolute-names "$CARPETA_RESPALDAR";
  echo "El proceso de backup finalizo exitosamente -->  $FECHA_Y_HORA" >> $CARPETA_DESTINO/log.txt
fi
}
#Le asigno a la variable LINES el resultado de la busqueda, ademas con wc cuenta las palabras y con -l las lineas
LINES=$(find /home/gabriel/Documents/Bk_email_automatico/Thunder* -mtime +14 | wc -l)

#En base a lo anterior ejecuto la condicion para tener un control de la eliminacion de bk antiguos y registro el resultado
eliminar_antiguos()
{
if [ "$LINES" -eq 0  ]; then
  echo "No se encontraron archivos en la busqueda. No se borraron backups antiguos -->  $FECHA_Y_HORA" >> $CARPETA_DESTINO/log.txt;
else
  find /home/gabriel/Documents/Bk_email_automatico/Thunder* -mtime +14 -delete;
  echo "Se encontraron archivos en la busqueda. Se borraron backups antiguos -->  $FECHA_Y_HORA" >> $CARPETA_DESTINO/log.txt;
fi
}
#cat $CARPETA_DESTINO/log.txt
crear_carpeta
comprimir_archivo
eliminar_antiguos