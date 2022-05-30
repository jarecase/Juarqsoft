from flask import Flask, request
from flask_pymongo import PyMongo
from threading import Thread
from flask_expects_json import expects_json
from Negocio.NGJuego import NGJuego

app = Flask('')

app.config['MONGO_URI'] = 'mongodb://cluster0.bxmeh.mongodb.net/myFirstDatabase'

mongo = PyMongo(app)

schema = {
  "type": "object",
  "properties": {
    "id": { "type": "number" },
    "nombre": { "type": "string" },
    "descripcion": { "type": "string" },
    "dificultad": { "type": "number" }
  },
  "required": ["nombre", "descripcion", "dificultad"]
}
 
@app.route('/api/juego', methods=['POST'])
@expects_json(schema)
def post():

  if request.json:
    return NGJuego.agregarJuego(request.json)
  else:
    return 'Nose ha enviado el json necesario'
  
def run():
	app.run(host='0.0.0.0',port=7000)

t = Thread(target=run)
t.start()