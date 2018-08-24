#! /usr/bin/python

from audiodiff import *
import os
import shutil
import sys

print "Comparar audio "
dir=sys.argv[1]
contadorEX=0

for i in os.listdir(dir):
	contadorEX = contadorEX + 1
	contador=0
	for j in os.listdir(dir):
		if i != j and j != "f1165262968.wav":
			contador=contador+1
			print contador,":",contadorEX
			print dir+"/"+i
			print dir+"/"+j
			if equal(dir+"/"+i,dir+"/"+j):
				shutil.move(dir+"/"+j,dir+"/"+i)
