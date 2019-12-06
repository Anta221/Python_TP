# epydeble

epydeble is a project which goal is to display nearby bluetooth devices on a web page.

## requirements

   - python > 3.6
   - libbluetooth-dev (linux)
   - modules in requirements.txt

## how to

The code currently provides two simple scripts:

	- `scan.py`: scan devices and store them in a json file with their ids, names, and RSSI.
	- `app.py`: simple Flask app

An devices.json file is provided as an example.
The bluetooth code in `blscan` uses PyBluez library.


Amélioration : 

- Horodatage 
    Permet de recuperer la date et l'heure au moment du scanne  toutes les connexion des appareils 


- Localisation
    Permet de récupérer certains données de l'utilisateur comme  l'adresse IP, latitude longitude, la ville 

Nous avons mis en place une base donnée avec Sqlite qui crée la base de donnée database.db contenant les tables information, localisation et user. (init.py)

- La table Information stock l'identifiant, le nom et le rssi du réseau bluetooth.

- La table Localisation stock l'adresse ip , le pays , la région, les coordonnées géographiques et le fuseau horaire du scanneur. 

- La table User stock les informations de connection au système 




Pour lancer l'application il faut faire un python scan.py.
Notre système de scannage ne fonctionnant pas, nous avons récupéré en Http un fichier json contenant les péripéhiques scanner via l'URL : http://swiv.outfplusto.com/5000/api/devices
Grâce à ce fichier nous créeons un json (device.json) dont les données seront insérés en base grâce à notre module Database (contient les fonctions d'insertion et d'affichage). Au moment du scannage nous récupérons également les données de localisation grâce à notre module Localisation qui fait appel au module python urllib.request . Ces informations seront insérées dans la table localisation. 

L'horodatage affiche la date complète et l'heure du scannage. 

Pour accéder à la page de l'application, il faut lancer l'envrinonnement virtuel et activer flask.Nous n'avons pas eu le temps de crée le système de login qui permet d'accéder à la page d'acceuil /homePage 
La page de scannage est sur l'url /devices et affiche les périphériques scanner. Nous n'avons pas réussi à afficher l'horodatage dans le template devices.html

Avec un peu plus de temps nous arions pu finaliser les éléments manquant et améliorer nos fonctions en mettant des docstring. 

(impossible d'installer pylint :(   )