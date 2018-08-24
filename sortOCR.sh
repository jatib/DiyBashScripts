#!/bin/bash/

files=$(ls | grep pdf)
declare -i counter
counter=0

for file in $files
do

  name=$(echo $file | tr "." "\n")

  for i in $name
  do
    if  [ $counter -eq 0 ]; then
      baseName=$i
    else
      extension=$i
    fi
      counter=+1
  done

  counter=0
  scannedName="scann"$file
  textName=$basename".txt"

  ocrmypdf $file $scannedName

  if ls $scannedName; then
    pdftotext $scannedName $textName
  else
    pdftotext $file $textName
  fi

  #fileContents=$(cat $textName)
  #for line in $fileContents
  #do
  #  if [ counter -lt 4 ]; then
  #    titleOfFile+=$line
  #    counter+=1
  #  fi
  #done

  counter=0
  titleOfFile+=".pdf"
  mv $file $titleOfFile

done
