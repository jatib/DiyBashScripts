#!/bin/bash

mover=$(ls | grep doc)

for file in $mover
do
  mv $file $PWD/nombrar/
done
