
class pokebase():

    def __init__(self, **kwargs):
        self.id_equipo =    kwargs.get("id_equipo", -1)
        self.id_pokedex =   kwargs.get("id_pokedex", -1)
        self.idpokemon =    kwargs.get("idpokemon", -1)

        self.nombre =       kwargs.get("nombre", "")
        self.tipo =         kwargs.get("tipo", "")
        self.especie =      kwargs.get("especie", "")

        self.move_one =     kwargs.get("move1", "")
        self.move_two =     kwargs.get("move2", "")
        self.move_three =   kwargs.get("move3", "")
        self.move_four =    kwargs.get("move4", "")

    def toDict(self):
        return {
            "pokedex_id": self.id_pokedex,
            "nombre": self.nombre,
            "especie": self.especie,
            "tipo": self.tipo,
            "move_one": self.move_one,
            "move_two": self.move_two,
            "move_three": self.move_three,
            "move_four": self.move_four
            }