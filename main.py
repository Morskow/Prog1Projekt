# -*- coding: utf-8 -*-

import csv
import re
import pandas as pd

datoteka = open('year_individual_r.html', "r", encoding="utf-8")
vsebina = datoteka.read()
datoteka.close()

vzorec = re.compile(
    r'id=\d+">(?P<ime>.+?)</a>.*?'
    r'code=[A-Z]+">(?P<drzava>.+?)</a>.*?'
    r'<td align="center">(?P<naloga1>\d+)</td>.*?'
    r'<td align="center">(?P<naloga2>\d+)</td>.*?'
    r'<td align="center">(?P<naloga3>\d+)</td>.*?'
    r'<td align="center">(?P<naloga4>\d+)</td>.*?'
    r'<td align="center">(?P<naloga5>\d+)</td>.*?'
    r'<td align="center">(?P<naloga6>\d+)</td>.*?'
    r'<td align="right">(?P<skupaj>\d+)</td>.*?'
    r'<td align="right">(?P<uvrstitev>\d+)</td>.*?'
    r'<td>(?P<nagrada>.*?)</td>',
    re.DOTALL
)
        
izhod = open('imo-podatki.csv', "w", encoding = "utf-8")

writer = csv.DictWriter(
        izhod, ['ime', 'drzava', 'naloga1', 'naloga2', 'naloga3', 'naloga4', 'naloga5', 'naloga6',
                'skupaj', 'uvrstitev', 'nagrada'])

writer.writeheader()
        
for ujemanje in vzorec.finditer(vsebina):
    writer.writerow((ujemanje.groupdict()))

izhod.close()

podatki = pd.read_csv('imo-podatki.csv')
print(podatki)
