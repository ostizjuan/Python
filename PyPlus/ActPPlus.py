import csv
import PySimpleGUI as sg
from constant import BUTTON, MARGINS
import json


def popup_error():
    """ Función que genera un popup de error cuando el archivo ya existe. """

    sg.popup_error('ERROR: El archivo ya existe.', font=('Helvetica',12,'bold'), keep_on_top=True)

def plastic_window():
    """ Generación de ventana para la toma de decisiones del criterio a utilizar """

    def plastic_bigger(data):
        """ Creación de archivo con los diez países con mayor probabilidad de emisión de plástico al océano. """

        try:
            data = sorted(data, key= lambda elem: float(elem[3]), reverse=True)
            with open('diez_mayores_plástico.json','x', encoding= 'utf-8') as arch:
                save = [{index+1:data[index][0]} for index in range(10)]
                json.dump(save, arch)
        except FileExistsError:
            popup_error()


    def plastic_smaller(data):
        """ Creación de archivo con los diez países con menor probabilidad de emisión de plástico al océano. """

        try:
            data = sorted(data, key= lambda elem: float(elem[3]))
            with open('diez_menores_plástico.json','x', encoding= 'utf-8') as arch:
                save = [{index+1:data[index][0]} for index in range(10)]
                json.dump(save, arch)
        except FileExistsError:
            popup_error()

    def event_plastic_criterion(event, csv_reader):
        """ Toma de decisiones para creación del archivo de países con probabilidad de emisión de plástico al océano, según el evento ocurrido. """

        data = filter(lambda elem: elem[0] not in ('Africa','Asia','EU-27','Europe', 'North America','South America', 'Oceania'), csv_reader)
        if event == '-MAYOR-':
            plastic_bigger(data)
        elif event == '-MENOR-':
            plastic_smaller(data)    


    layout =    [
                    [sg.Text('¿Qué datos desea obtener?', font=('Helvetica',12,'bold'), border_width= (10), text_color= 'blue')],
                    [sg.Button('10 países con mayor probabilidad', size=BUTTON, key='-MAYOR-')],
                    [sg.Button('10 países con menor probabilidad', size=BUTTON, key='-MENOR-')],
                ]
    
    window = sg.Window('Elección de criterio', layout, margins=MARGINS, element_justification='center')
    while True:
        event, values = window.read()
        if event is sg.WIN_CLOSED:
            break
        archivo = open('DataSets/probability-mismanaged-plastic-ocean.csv', 'r', encoding= 'utf-8')
        csv_reader = csv.reader(archivo, delimiter= ',')
        csv_reader.__next__()
        event_plastic_criterion(event, csv_reader)
        archivo.close()
    
    window.close()

def issuance_window():
    """ Generación de ventana para la toma de decisiones del criterio a utilizar """

    def issuance_bigger(csv_reader):
        """ Creación de archivo con los diez países con mayor emisión de CO2. """

        try:
            data = filter(lambda elem: elem[2] == '2019', csv_reader)
            data = sorted(data, key= lambda elem: float(elem[3]), reverse=True)
            with open('diez_mayores_emisión.json','x', encoding= 'utf-8') as arch:
                save = [{index+1:data[index][0]} for index in range(10)]
                json.dump(save, arch)
        except FileExistsError:
            popup_error()


    def issuance_smaller(csv_reader):
        """ Creación de archivo con los diez países con menor emisión de CO2. """

        try:
            data = filter(lambda elem: elem[2] == '2019', csv_reader)
            data = sorted(data, key= lambda elem: float(elem[3]))
            with open('diez_menores_emisión.json','x', encoding= 'utf-8') as arch:
                save = [{index+1:data[index][0]} for index in range(10)]
                json.dump(save, arch)
        except FileExistsError:
            popup_error()
        
    def event_issuance_criterion(event, csv_reader):
        """ Toma de decisiones para creación del archivo de la emisión de CO2 de países, según el evento ocurrido. """

        if event == '-MAYOR-':
            issuance_bigger(csv_reader)
        elif event == '-MENOR-':
            issuance_smaller(csv_reader)    


    layout =    [
                    [sg.Text('¿Qué datos desea obtener?', font=('Helvetica',12,'bold'), border_width= (10), text_color= 'blue')],
                    [sg.Button('10 países con mayor emisión', size=BUTTON, key='-MAYOR-')],
                    [sg.Button('10 países con menor emisión', size=BUTTON, key='-MENOR-')],
                ]
    
    window = sg.Window('Elección de criterio', layout, margins=MARGINS, element_justification='center')
    while True:
        event, values = window.read()
        if event is sg.WIN_CLOSED:
            break
        archivo = open('DataSets/co-emissions-per-capita.csv', 'r', encoding= 'utf-8')
        csv_reader = csv.reader(archivo, delimiter= ',')
        csv_reader.__next__()
        event_issuance_criterion(event, csv_reader)
        archivo.close()
    
    window.close()


def event_handler(event):
    """ Toma de decisiones para procesar los DataSets """

    if event == '-PLASTIC-':
        plastic_window()
    if event == '-CO2-':
        issuance_window()


def window():
    """ Creación de la ventana principal """

    sg.theme('Default')
    layout =    [
                    [sg.Text('¿Qué datos analizamos?',font=('Helvetica',12,'bold'), border_width= (10), text_color= 'blue')],
                    [sg.Button('Probabilidad de que se emita plástico al océano', size= BUTTON, key='-PLASTIC-')],
                    [sg.Button('Emisión de CO2 según país', size= BUTTON, key= '-CO2-')],
                    [sg.Button('Salir', size= BUTTON, key= '-QUIT-', pad=((0,0),(20,0)))]
                ]
    
    window = sg.Window('Actividad 1 x Python Plus - TEORIA -', layout, margins=MARGINS, element_justification= 'center')
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, '-QUIT-'):
            break
        window.Hide()
        event_handler(event)
        window.UnHide()
    window.close()

window()