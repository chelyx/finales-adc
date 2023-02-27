# -*- coding: utf-8 -*-
import json
import copy

import sys

print('cmd entry:', sys.argv)

# the file to be converted to
# json format
filename = sys.argv[1]
name = sys.argv[2]
list = []
i=0
d = {}
# creating dictionary
with open(filename) as fh:   
    for line in fh:
        if(line.upper().strip() == 'TEORIA' or line.upper().strip() == 'PRACTICA'):
            d['esSeparador']= True
            d['texto']= line.strip()
            list.append(copy.deepcopy(d))
            d = {}
            i =-1
        elif(i%2 == 0 or i == 0):
            d['pregunta'] = line.strip()
        else:
            d['respuesta']= line.strip()
            list.append(copy.deepcopy(d))
            d = {}
        i=i+1
    
final = {
    "nombre": name,
    "preguntas": list
}

# creating json file
# the JSON file is named as test1
out_file = open("test1.json", "w")
json.dump(final, out_file, indent = 4, sort_keys = False, ensure_ascii=False)
out_file.close()
