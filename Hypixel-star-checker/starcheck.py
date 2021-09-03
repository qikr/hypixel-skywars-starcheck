import requests
import json
from pprint import pprint
import time
import os
import sys
import colour
from sty import fg, bg, ef, rs



def getInfo(call):
    r = requests.get(call)
    return r.json()

print("_░▒███████")
print("░██▓▒░░▒▓██")
print("█▓▒░  ░▒▓██   ██████")
print("██▓▒░    ░▓███▓  ░▒▓██")
print("██▓▒░   ░▓██▓     ░▒▓██")
print("██▓▒░               ░▒▓██")
print(" ██▓▒░              ░▒▓██")
print("  ██▓▒░            ░▒▓██")
print("   ██▓▒░          ░▒▓██")
print("    ██▓▒░        ░▒▓██")
print("     ██▓▒░     ░▒▓██")
print("      ██▓▒░  ░▒▓██")
print("       █▓▒░░▒▓██")
print("         ░▒▓██")
print("       ░▒▓██")
print("      ░▒▓██")

API_ASK = input("API Key: ")
User = input("User: ")
API_KEY = '5b806a72-117b-49e9-a7ba-2775a9210c9c'

url = "https://api.hypixel.net/player?key={}&name={}".format(API_KEY, User)

data = getInfo(url)

stat = data["player"]["stats"]["SkyWars"]["levelFormatted"]

stat2 = ((stat).replace('§', ''))

stat10 = stat2[1:9]
stat11 = ((stat10).replace('a', ''))
stat12 = ((stat11).replace('b', ''))
stat13 = ((stat12).replace('c', ''))
stat14 = ((stat13).replace('d', ''))
stat15 = ((stat14).replace('e', ''))
stat16 = ((stat15).replace('f', ''))
stat17 = ((stat16).replace('g', ''))
stat18 = ((stat17).replace('l', ''))
stat19 = ((stat18).replace('k', ''))
print(stat19)


i = 1
while i < 6:

    User = input("User: ")
    API_KEY = "API_ASK"

    url = "https://api.hypixel.net/player?key={API_KEY}&name={User}"

    data = getInfo(url)

    stat = data["player"]["stats"]["SkyWars"]["levelFormatted"]

    stat2 = ((stat).replace('§', ''))

    stat10 = stat2[1:9]
    stat11 = ((stat10).replace('a', ''))
    stat12 = ((stat11).replace('b', ''))
    stat13 = ((stat12).replace('c', ''))
    stat14 = ((stat13).replace('d', ''))
    stat15 = ((stat14).replace('e', ''))
    stat16 = ((stat15).replace('f', ''))
    stat17 = ((stat16).replace('g', ''))
    stat18 = ((stat17).replace('l', ''))
    stat19 = ((stat18).replace('k', ''))
    print(stat19)

    #if stat19.__contains__('6') == True:
        # stat201 = ((stat19).replace('16', '1'))
        #stat201 = stat19[0:1]
        #stat202 = stat19[2:9]
        #print(stat201+stat202)
    #else:

    # print('stat contains a =', stat19.__contains__('16'))
