from flask import jsonify
    
class NGJuego():
  
  def agregarJuego(json):
    if json["nombre"]:
      return "No se ha ingresado el nombre"
    else:
      return jsonify(json)

