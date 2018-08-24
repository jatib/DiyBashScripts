#!/bin/bash

dir=$(ls | grep $1 )

for i in $dir
do
archivo=$i
test=$(exiftool $i | grep Last)
directorio=""

declare -i incidencias
incidencias=0
declare -i incidenciasDot
incidenciasDot=0
#echo $test

for line in $test
do
  if [ $line == "Date" ]; then
    incidencias+=1
  fi
  if [ $line == ":" ]; then
    incidenciasDot+=1
  fi
  if [ $incidencias -eq 1 ] && [ $incidenciasDot -eq 1 ]; then
    if [ $line != ":" ]; then
      directorio+=""
    else 
     directorio+=$line
    fi
  fi
done

if [ $directorio != "" ]; then
if ls $PWD/$directorio/; then
  # echo "Existe el dir"
  mv $archivo $PWD/$directorio
else
  # echo "No existe el dir"
  mkdir $PWD/$directorio
  mv $archivo $PWD/$directorio
fi
fi

echo $directorio
done
#echo $test

