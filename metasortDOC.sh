#!/bin/bash

dir=$(ls | grep $1 )

for i in $dir
do
archivo=$i
metadata=$(exiftool $i | grep 'Author                          :')
directorio=""

declare -i incidencias
incidencias=0
declare -i incidenciasDot
incidenciasDot=0

# echo ${#meta}" : "$archivo

for line in $metadata
do
  if [ $line == "Author" ]; then
    incidencias+=1
  fi
  if [ $line == ":" ]; then
    incidenciasDot+=1
  fi
  if [ $incidencias -eq 1 ] && [ $incidenciasDot -eq 1 ] && [ $line != ":" ]; then
    directorio+=$line
  fi
done

if [ -n "$directorio" ]; then
  if ls $PWD/$directorio/; then
     #echo "Existe el dir"
     mv $archivo $PWD/$directorio/
  else
     #echo "No existe el dir"
     mkdir $PWD/$directorio
     mv $archivo $PWD/$directorio/
  fi
fi

if [ -n "$directorio" ]; then
  echo $directorio
fi
done


