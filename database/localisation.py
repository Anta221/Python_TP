"""Données de l'appareil qui scan!!!"""
import json
from urllib.request import urlopen


def donnee_localisation():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    liste = {'ip': data['ip'],
    'country': data['country'],
    'loc': data['loc'],
    'timezone': data['timezone']
    
    
    }


    return liste


