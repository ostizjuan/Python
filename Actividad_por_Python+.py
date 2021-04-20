import csv

with open('appstore_games.csv', 'r') as archivo:
    csvreader = csv.reader(archivo, delimiter= ',')
    csvreader.__next__()

    listado = filter(lambda col: col[7] == '0' and 'ES' in col[12].replace(',','').split(), csvreader)
    
    print('Listado de juegos gratuitos: ')
    for linea in listado:
        print(linea[2])