import database
from flask import Flask, request, render_template, redirect, url_for
import json


app = Flask(__name__)


@app.route('/homePage', methods=['GET'])
def home():
  homePage = parse_from_json()
  return render_template("PythonHtml.html", homePage=homePage)


@app.route('/devices', methods=['GET'])
def devices():
  devices = parse_from_json()
  return render_template("devices.html", devices=devices)



def parse_from_json():
  devices = []
  with open('./devices.json', 'r') as f:
    data = json.loads(f.read())
    for device in data:
      devices.append({"id": device["id"],
                      "name": device["name"],
                      "rssi": device["rssi"] if "rssi" in device else "?"})
    return devices

def dump_to_json(devices):
  pass
