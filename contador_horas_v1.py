"""programa que registra a quantidade de horas no computador

Básico:

O programa deve ter um botão que registra os tempos que o botão foi apertado
Os horarios devem ser separados em horario de entrada e horario de saida
O programa deve somar o total de horas 'logadas' no dia
O programa deve registrar num doc e retornar um xlsx pro usuario


Intermed:

checar o funcionamento do computador ao longo do uso


Avançado:

Assistive touch"""

from datetime import datetime
from os import path

data = []

if path.exists('register.csv') is False:
    with open('register.csv', 'w') as rgt:
        rgt.write('entrance,exit,total')
        rgt.write('\n')
        rgt.close()

with open('register.csv', 'a+') as rgt:
    def get_datetime():
        data.append(datetime.now())

        if len(data) == 2:
            data.append(data[1] - data[0])

            for item in data:  # escrever no csv
                try:
                    rgt.write(datetime.strftime(item, '%d/%m/%Y - %H:%M:%S,'))
                except:
                    rgt.write(str(item))
            rgt.write('\n')

            data.clear()  # limpar 'data'
