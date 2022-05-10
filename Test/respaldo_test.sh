#!/bin/bash
RUTA_SCRIPT=`dirname ${BASH_SOURCE[0]}`
FECHA_Y_HORA=`date "+%d-%m-%y_%H-%M-%S"`
FECHA=`date "+%d-%m-%y"`
NOMBRE_ARCHIVO="Test_$FECHA_Y_HORA.tgz"
LINES=0
CARPETA_DESTINO="$RUTA_SCRIPT/respaldos_prueba"
# Nota: la carpeta a respaldar puede ser otra, pero si no es relativa al script, pon su ruta completa
CARPETA_RESPALDAR="/home/gabriel/Documents/cosas_importantes"
# Creamos el directorio para los respaldos por si no existe
mkdir -p "$CARPETA_DESTINO"
if [ -f /home/gabriel/Documents/respaldos_prueba/$NOMBRE_ARCHIVO ];then
	echo "El archivo no se creo,porque ya existe un archivo con el mismo nombre-->  $FECHA_Y_HORA" >> $CARPETA_DESTINO/log.txt;
	echo "El proceso finalizo con errores. Ver Logs"
else
	tar cfvz "$CARPETA_DESTINO/$NOMBRE_ARCHIVO" --absolute-names "$CARPETA_RESPALDAR";
	echo "El proceso Finalizo exitosamente -->  $FECHA_Y_HORA" >> "$CARPETA_DESTINO/log.txt"
fi

LINES=$(find /home/gabriel/Documents/respaldos_prueba/Test* -cmin +60 | wc -l)

if [ $LINES==0 ];then
	echo "No se encontraron archivos en la busqueda. No se borraron backups antiguos -->  $FECHA_Y_HORA" >> $CARPETA_DESTINO/log.txt
else
	find /home/gabriel/Documents/respaldos_prueba/Test* -cmin +60 -delete;
	echo "Se encontraron archivos en la busqueda. Se borraron backups antiguos -->  $FECHA_Y_HORA" >> $CARPETA_DESTINO/log.txt
fi
