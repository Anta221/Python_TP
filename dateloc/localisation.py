"""Données de l'appareil qui scan!!!"""
import re
import json
from urllib.request import urlopen

def donnee_localisation():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)
    return data

