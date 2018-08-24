#!/bin/bash

lista=$(ls | grep doc)

for file in $lista
do
  cp $file $PWD/nombres/
done
