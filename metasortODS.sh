#!/bin/bash

dir=$(ls | grep $1 )

for i in $dir
do
archivo=$i
test=$(exiftool $i | grep 'File Modification Date/Time'| fold -w1)
#echo $test
directorio=""

declare -i incidencias
incidencias=0
declare -i incidenciasDot
incidenciasDot=0
declare -i limiteNombre
limiteNombre=0
#echo $test

for line in $test
do
  #echo $line
  if [ $line == "T" ] || [ $line == "m" ]; then
    incidencias+=1
  fi
  if [ $line == ":" ]; then
    incidenciasDot+=1
  fi
  if [ $incidenciasDot -ge 3 ]; then
    limiteNombre+=1
  fi
  if [ $limiteNombre -lt 4 ] && [ $incidencias -eq 2 ] && [ $incidenciasDot -ge 1 ] && [ $incidenciasDot -lt 4 ]; then
    if [ $line == ":" ] || [ $line == "" ]; then
      directorio+="_"
    else
      if [ $line == "e" ]; then
        directorio+=""
      else
        directorio+=$line
      fi
    fi
  fi
done

chrlen=${#directorio}

if [ $chrlen -gt 7 ]; then
  if ls $PWD/$directorio/; then
    #echo "Existe el dir"
    mv $archivo $PWD/$directorio
  else
    #echo "No existe el dir"
    mkdir $PWD/$directorio
    mv $archivo $PWD/$directorio
  fi
fi

echo $directorio
done
#echo $test

