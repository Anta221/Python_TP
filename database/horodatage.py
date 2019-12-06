"""horodatage pour afficher la date et l'heure de la récupération de tout les bluethooth """
from datetime import datetime
from jinja2 import Template



def date_time():
    now = datetime.now()
    horodatage = now.strftime("%m/%d/%Y, %H:%M:%S")
    return horodatage

