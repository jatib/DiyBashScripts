
class Estructura:
    def __init__(self):

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
