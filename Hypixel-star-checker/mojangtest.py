import requests


def getInfo(call):
    r = requests.get(call)
    return r.json()

ask = input("ign:")

h = "https://api.mojang.com/users/profiles/minecraft/{}?at=0".format(ask)
data = getInfo(h)
if data == :
    print("p")
else:
    stat = data["name"]
    print(stat)
    s = input("a")
    
