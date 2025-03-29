#!/usr/bin/env python3

import os

#dobbiamo trovare gli shebang interpreter dei file eseguibili dentro questo
FILEPATH = "\\inserisci\\path\\qui"

def shebang_finder(path):
    matches = []
    # Scorri il folder e i suoi figli
    for (root,dirs,files) in os.walk(path,topdown=True):
        for file in files:
        #estraiamo i file
          if os.access(file, os.X_OK):
          #filtriamo quelli accessibili in modalità execute
            with open(file, "r") as content:
                first_line = content.readline() #lo shebang si deve trovare all'inizio del file

                if first_line.startswith('#!'):
                 matches.append(first_line.strip()) #strip per pulire la riga da newline o spazi
                else:
                    continue #prossimo file

    return matches

array = shebang_finder(FILEPATH)
shebang_counts = {}

print("shebang interpreter trovati in " + FILEPATH)
for key in array:
    if key not in shebang_counts:
        shebang_counts[key] = 0

    shebang_counts[key] += 1

print(shebang_counts)