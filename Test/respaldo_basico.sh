#!/bin/bash
RUTA_SCRIPT=`dirname ${BASH_SOURCE[0]}`
FECHA_Y_HORA=`date "+%d-%m-%y_%H-%M-%S"`
NOMBRE_ARCHIVO="Bk_Thunder_$FECHA_Y_HORA.tgz"
CARPETA_DESTINO="$RUTA_SCRIPT/respaldos"
# Nota: la carpeta a respaldar puede ser otra, pero si no es relativa al script, pon su ruta completa
CARPETA_RESPALDAR="/home/gabriel/.thunderbird"
# Creamos el directorio para los respaldos por si no existe
mkdir -p "$CARPETA_DESTINO"
tar cfvz "$CARPETA_DESTINO/$NOMBRE_ARCHIVO" "$CARPETA_RESPALDAR"
