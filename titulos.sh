#!/bin/bash/

archivos=$(ls | grep doc)
declare -i incidencia
incidencia=0

for archivo in $archivos
do

  nombre=$(echo $archivo | tr "." "\n")

  for i in $nombre
  do
    if [ $incidencia -eq 0 ]; then
      basename=$i
    fi
    incidencia=+1
  done

  incidencia=0
  textName=$basename".txt"

  #echo $textName
  if ! ls $textName; then
    libreoffice --headless --convert-to "txt:Text (encoded):UTF8" $archivo
  fi

done
