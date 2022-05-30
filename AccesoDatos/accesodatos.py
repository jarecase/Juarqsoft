from replit import db
import requests

res = requests.get('https://scotch.io')

print(res)

def agregarJuego(juego):
  db["Juego"] = juego