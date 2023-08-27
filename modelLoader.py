import numpy as np
f = open("arch.obj", "r")
faces = []
verticies = []
# print(faces)
for x in f:
    line = x.split(" ")
    if(line[0] == "v"):
        verticies.append([[float(line[1]),float(line[2]),float(line[3])]])
    if(line[0] == "f"):
        faces.append([[int(line[1])],[int(line[2])],[int(line[3])]])