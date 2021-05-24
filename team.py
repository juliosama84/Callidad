from pokemon import pokebase

class teambase():
    def __init__(self,id_entrenador = -1, pokemones = [], equiponombre = ""):
        self.id_equipo = -1
        self.generacion = -1
        self.id_entrenador = id_entrenador
        self.team_name = equiponombre 
        self.lista_pokemon = pokemones
