"""Données de l'appareil qui scan!!!"""
import re
import json
from urllib.request import urlopen

def donnee_localisation():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    Adresse_IP=data['ip']
    country=data['country']
    latitude_longitude=data['loc']
    Fuseaux_horraire = data['timezone']

    message ='Détails des données de localisation\n\n'
    data='Adresse_IP : {1} \nCountry : {0}  \nlatitude_longitude: {2} \nFuseaux_horraire: {3}'.format(country,Adresse_IP,latitude_longitude,Fuseaux_horraire)
    infos= message + data
    return infos

