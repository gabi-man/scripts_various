#!/bin/bash
lines=$(find /home/gabriel/Documents/respaldos_prueba/Test* -cmin -100 | wc -l)
if [ "$lines" -eq 0 ]
then
	echo "No encontrado"
else
	echo "Encontrado";
	find /home/gabriel/Documents/respaldos_prueba/Test* -cmin -100 -delete
fi
