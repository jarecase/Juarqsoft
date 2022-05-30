from flask import Flask, Response, request
from bson import json_util
from bson.objectid import ObjectId
from flask_expects_json import expects_json
from Negocio.NGValidadoresTipos import NGValidadoresTipos
from flask_pymongo import PyMongo

app = Flask(__name__)
 
app.config['MONGO_URI'] = 'mongodb+srv://jrcamacho:jrcamacho@cluster0.bxmeh.mongodb.net/Juarqsoft'
 
mongo = PyMongo(app)

@app.route('/api/juego', methods=['GET'])
def consultarjuegos():
    juegos = mongo.db.juego.find()
    respuesta = json_util.dumps(juegos)
    return Response(respuesta, mimetype='application/json')

@app.route('/api/juego/<id>', methods=['GET'])
def consultarjuego(id):
    juego = mongo.db.juego.find_one({'_id' : ObjectId(id)})
    respuesta = json_util.dumps(juego)
    return Response(respuesta, mimetype='application/json')

@app.route('/api/juego/<id>', methods=['DELETE'])
def eliminarjuego(id):
    juego = mongo.db.juego.delete_one({'_id' : ObjectId(id)})
    return str(juego.deleted_count)

@app.route('/api/juego', methods=['POST'])
@expects_json(NGValidadoresTipos.Juego())
def crearjuego():
    juegoPorNombre = mongo.db.juego.find_one({'nombre' : request.json['nombre']})
    if juegoPorNombre == None:
        juego = mongo.db.juego.insert_one(request.json)
        return str(juego.inserted_id)
    else:
        return 'ya existe un juego con el nombre ' + request.json['nombre']
         

@app.route('/api/juego/<id>', methods=['PUT'])
@expects_json(NGValidadoresTipos.Juego())
def actualizarjuego(id):
    validarnombre = mongo.db.juego.find_one({'nombre' : ObjectId(id)})

    id = mongo.db.juego.update_one({'_id' : ObjectId(id)}, request.json)
    return str(id)

@app.errorhandler(404)
def not_found(error=None):
    menssage={
        'message': 'Recurso no encontrado ' + request.url,
        'status':404
    }
    return menssage

if __name__ == "__main__":
    app.run(debug=True)