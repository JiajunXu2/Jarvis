import requests
from plugin import plugin

@plugin("sale")
def get_sale(jarvis, s):
    jarvis.say("Enter the game you would like to search: ")
    game = jarvis.input()
    url = "https://www.cheapshark.com/api/1.0/games?title={game}"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    
