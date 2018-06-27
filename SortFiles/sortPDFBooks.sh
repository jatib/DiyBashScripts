#!/bin/bash/

category=$1

for file in *pdf*
do
  nameOfFile=($( echo $file | tr "." " "))
  name=${nameOfFile[0]}
  scannedFile="scann"$file
  flatFile=$name".txt"
  ocrmypdf $file $scannedFile 2>/dev/null
  
  if ls $scannedFile; then
    pdftotext $scannedFile $flatFile
  else
    pdftotext $file $flatFile
  fi
  
  fileContent=$( grep $flatFile )
  
  for categ
done
