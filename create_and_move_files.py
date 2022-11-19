import csv
import os
import shutil
import pathlib  #manejo libreria de rutas

from pathlib import Path, PurePath


# leer csv y crear listas

with open('students.csv') as csv_file:
    data = csv.reader(csv_file, delimiter=' ', quotechar='|')  # debe estar la dir de mi .py
    list_name = []
    list_id = []
    for row in data:
        student = ' '.join(row).split(',')
        list_name.append(student[0])
        list_id.append(student[1])

only_names = list_name.pop(0)
only_id = list_id.pop(0)

#Crear carpeta
for name in list_name:
    os.mkdir(name)

#
game_move = []
pdf_move = []
origin_path = os.path.join(os.getcwd(), 'data')                    #De donde mover

#lista con lo que tiene la carpeta
files = os.listdir('data')                                    # Acceder al contenido de  carpeta

for file in files:
    if 'game' in file.lower() and '.' not in file:
        game_move.append(file)
    if file.endswith('.pdf'):
        pdf_move.append(file)

path_move = Path.cwd()

for file in game_move:
    if os.path.exists(origin_path + '/' + file):
        shutil.move(origin_path + '/' + file, (os.path.join(os.getcwd(), 'Games')))

for file in pdf_move:
    if os.path.exists(origin_path + '/' + file):
        shutil.move(origin_path + '/' + file,  (os.path.join(os.getcwd(), 'Tutorials')))