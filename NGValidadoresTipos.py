class NGValidadoresTipos():
  
  def Juego():
      return {
  "type": "object",
  "properties": {
    "id": { "type": "number" },
    "nombre": { "type": "string" },
    "descripcion": { "type": "string" },
    "dificultad": { "type": "number" }
  },
  "required": ["nombre", "descripcion", "dificultad"]
}

