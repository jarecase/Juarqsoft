from dataclasses import dataclass

@dataclass
class Juego:
    id: int 
    nombre: str
    descripcion: str = ""
    dificultad: float = 0