#!/bin/bash/

archivos=$(ls | grep txt)
declare -i incidencia
incidencia=0

for archivo in $archivos
do
  contenido=$(cat $archivo)
  nombre=$(echo $archivo | tr "." "\n")

  for i in $nombre
  do
    if [ $incidencia -eq 0 ]; then
      basename=$i
    else
      extension=$i
    fi
      incidencia=+1
  done

  for line in $contenido
  do
    if [ $incidencia -eq 0 ] && [ -n "$line" ]; then
      filename=$line
      incidencia+=1
    fi
  done

  if ! echo $filename | grep '��#ࡱ#�################'; then
    if [ -n "$filename" ]; then
      echo $filename
    fi
  fi

  incidencia=0
done














############################################################
: <<'END'
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
  contenido=$(cat $archivo)
  docRename=$(ls | grep '$basename.doc')
  docRename=$(echo $docRename | tr "." "\n")

  for i in $docRename
  do
    if [ $incidencia -eq 1 ]; then
      extension=$docRename
    fi
    incidencia=+1
  done

  incidencia=0

  for line in $contenido
  do
    if [ $incidencia -eq 0 ]; then
      nuevoNombre=$line.$extension
    fi
  done

  incidencia=0
  #textName=$basename".txt"
  #echo $textName
  #if ! ls $textName; then
  #  libreoffice --headless --convert-to "txt:Text (encoded):UTF8" $archivo
  #fi

done
END
#######################################################
