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

- *horodatage et localisation (GPS +IP)
- *Base de donnée
- Actualisation automatique des info  sur la page web 
- Actualisation automatique du scan (daemon)
- authentification 
- front 
- informations sur les périphériques 
- héberger/ déployer 
- mutualiser 