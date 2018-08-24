#!/bin/bash

#declare -i numero
declare -i num


for numero in {100..999}
do

num=0

#if [ $numero -gt 99 ] && [ $numero -lt 1000 ]; then
  let 'num = (numero/100)*(numero/100)*(numero/100) + ((numero%100)/10)*((numero%100)/10)*((numero%100)/10) + ((numero%100)%10))*((numero%100)%10)*((numero%100)%10)' &>/dev/null
  if [ $num -eq $numero ]; then
    echo "$num es igual a $numero, por tanto, es un numero de Armstrong"
  #else
    # echo "$num distinto de $numero, por tanto, no es un numero de Armstrong"
  fi
#else
 # echo "El número no es válido"
#fi

done
