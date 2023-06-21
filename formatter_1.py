# -*- coding: utf-8 -*-
import json
import copy

import os
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
    
final_nuevo = {
    "nombre": name,
    "preguntas": list
}

aux = open("aux.json", "w")

with open("finales.json") as finalesBD:
    finales = json.load(finalesBD)
    finales['finales'].append(final_nuevo)

    json.dump(finales, aux, indent = 4, sort_keys = False, ensure_ascii=False)

finalesBD.close()
aux.close()

os.remove("finales.json")
os.rename("aux.json", "finales.json")