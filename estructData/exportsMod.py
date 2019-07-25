import os
import shutil

file = open("/home/developer/exports","r")

def trunk(a):
    data = a.readlines()
    head = []
    imod = 0
    for i in range(len(data)):
        if i-imod < len(data)-1:
            if data[i-imod][0] == "#":
                head.append(data[i-imod].split("\n")[0])
                data.pop(i-imod)
                imod += 1
    return [data,head]

def structureData(a):
    structured_data = []
    for line in a:
        structure = []
        if line[0] != '"':
            for oDat in line.split(" "):
                for dat in oDat.split("\t"):
                    if dat != "":
                        structure.append(dat.split("\n")[0])
        else:
            structure.append(line.split('"')[1])
            for oDat in line.split('"')[2].split(" "):
                for dat in oDat.split("\t"):
                    if dat != "":
                        structure.append(dat.split("\n")[0])
        structured_data.append(structure)
    return structured_data

def ipData(a):
    iPs = []
    for line in a:
        for ip in line[1:]:
            dirs = []
            purgedIp = ip.split("(")[0]
            if purgedIp not in iPs and "." in purgedIp and "/" not in purgedIp:
                dirs.append(purgedIp)
                for lin in a:
                    if ip in lin:
                        dirs.append(lin[0])
                iPs.append(dirs)
    return iPs

def load():
    file = open("/home/developer/exports","r")
    data = trunkHead(file)
    structured = structureData(data[0])
    iPs = ipData(structured)

    return data,structured,iPs

data = trunk(file)
structured = structureData(data[0])
iPs = ipData(structured)

def flujo(fin=False):
    if fin == False:
        print("Selecciona una de las siguientes opciones:\n1) Reemplazar ip\n2)Eliminar ip\n3)Añadir ip\n4)Visualizar dependencias según ip\n5)Visualizar dependencias según carpetas\n\n")

        option = int(input("Introduzca número de opción:\n"))
        if option == 4:
            print("Selecciona una de las siguientes opciones:\n1)Filtrar\n2)Mostrar todo\n\n")
            option = int(input("Introduzca número de opción:\n"))
            print("\n\n")
            if option == 1:
                query = input("Introduzca una nueva ip:\n")
                if query in iPs:
                    print(iPs.index(query))
                else:
                    print("La ip señalada no existe")
        flujo()
flujo()
