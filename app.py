from flask import Flask, Response, request
from bson import json_util
from bson.objectid import ObjectId
from flask_expects_json import expects_json
from NGValidadoresTipos import NGValidadoresTipos
from flask_pymongo import PyMongo
import requests
import os

app = Flask(__name__)
 
app.config['MONGO_URI'] = 'mongodb+srv://jrcamacho:jrcamacho@cluster0.bxmeh.mongodb.net/Juarqsoft'
API = 'https://62859626f0e8f0bb7c063948.mockapi.io/api/v1/Juego'

mongo = PyMongo(app)

@app.route('/')
def home():
    return 'hello'

@app.route('/api/juego', methods=['GET'])
def consultarjuegos():
    juegos = requests.get(API, {}, timeout=5)
    #juegos = mongo.db.juego.find()
    respuesta =  json_util.dumps(juegos.json())
    return Response(respuesta, mimetype='application/json')

@app.route('/api/juego/<id>', methods=['GET'])
def consultarjuego(id):
    juegos = requests.get(API + '/' + id, {}, timeout=5)
    #juego = mongo.db.juego.find_one({'_id' : ObjectId(id)})
    respuesta =  json_util.dumps(juegos.json())
    return Response(respuesta, mimetype='application/json')

@app.route('/api/juego/<id>', methods=['DELETE'])
def eliminarjuego(id):
    juegos = requests.delete(API + '/' + id, data ={'key':'value'}, timeout=5)
    #juego = mongo.db.juego.delete_one({'_id' : ObjectId(id)})
    #return str(juego.deleted_count)
    respuesta =  json_util.dumps(juegos.json())
    return Response(respuesta, mimetype='application/json')
    
@app.route('/api/juego', methods=['POST'])
@expects_json(NGValidadoresTipos.Juego())
def crearjuego():
    juegos = requests.post(API, data =request.json, timeout=5)
    #juegoPorNombre = mongo.db.juego.find_one({'nombre' : request.json['nombre']})
    #if juegoPorNombre == None:
    #    juego = mongo.db.juego.insert_one(request.json)
    #    return str(juego.inserted_id)
    #else:
    #    return 'ya existe un juego con el nombre ' + request.json['nombre']
    respuesta =  json_util.dumps(juegos.json())
    return Response(respuesta, mimetype='application/json')
         

@app.route('/api/juego/<id>', methods=['PUT'])
@expects_json(NGValidadoresTipos.Juego())
def actualizarjuego(id):
    juegos = requests.put(API + '/' + id, data =request.json, timeout=5)
    #juegoPorNombre = mongo.db.juego.find_one({'nombre' : request.json['nombre']})
    #if juegoPorNombre == None:
    #    #juego = mongo.db.juego.update_one({'_id' : ObjectId(id)}, {'$set' : request.json})
    #    return str(juego.modified_count)
    #else:
    #    print (juegoPorNombre['_id'])
    #    if str(juegoPorNombre['_id']) == str(id):
    #        juego = mongo.db.juego.update_one({'_id' : ObjectId(id)}, {'$set' : request.json} )
    #        return str(juego.modified_count)
    #    else:
    #        return 'ya existe un juego con el nombre ' + request.json['nombre']
    respuesta =  json_util.dumps(juegos.json())
    return Response(respuesta, mimetype='application/json')

@app.errorhandler(404)
def not_found(error=None):
    menssage={
        'message': 'Recurso no encontrado ' + request.url,
        'status':404
    }
    return menssage

port = os.environ.get("PORT", 5000)
#print('get port %d' % port)



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)