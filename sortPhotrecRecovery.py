import os
import shutil

# Declare the PATH of the recovery
path = str(input("Ingrese el PATH al recovery de photorec\n"))

if path[-1] != "/":
	path += "/"

if path[0] != "/":
	path = "/"+path

dirs = os.listdir(path)
print(dirs)
for dir in dirs:
	print ("{}".format(dir))
	newPath = path + dir + "/"
	files = os.listdir(newPath)
	for file in files:
		fileName = file.split(".")
		if len(fileName)>1:
			if os.path.isdir(path+"/"+fileName[-1]):
				#print("{} es un directorio".format(fileName[-1]))
				os.rename( newPath + "/" + file , path + "/" + fileName[-1] + "/" + file )
			else:
				os.mkdir(path+"/"+fileName[-1])
				print("{} no es un directorio".format(fileName[-1]))
		else:
			if os.path.isdir(path+"/otros/"):
