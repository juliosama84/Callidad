from team import teambase

class entrenadorbase:
    def __init__(self, nombre = "", password = "", equipos = [], entrenadorId = -1):
        self.entrenadorId = entrenadorId
        self.nombre = nombre
        self.password = password
        
