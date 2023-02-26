# -*- coding: utf-8 -*-
import json
import copy

# the file to be converted to
# json format
filename = 'data.txt'

# dictionary where the lines from
# text will be stored
list = []
pregunta = "pregunta"
resp = "respuesta"
i=0
d = {}
# creating dictionary
with open(filename) as fh:   
    for line in fh:
        if(i%2 == 0 or i == 0):
            d[pregunta] = line.strip()
        else:
            d[resp]= line.strip()
            list.append(copy.deepcopy(d))
        i=i+1
        
print(list)

# creating json file
# the JSON file is named as test1
out_file = open("test1.json", "w")
json.dump(list, out_file, indent = 4, sort_keys = False, ensure_ascii=False)
out_file.close()
