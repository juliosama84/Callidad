import subprocess

import const
from storageInterface import IStorage
from baseConection import DataBaseInteract
from team import teambase
from pokemon import pokebase
from entrenador import entrenadorbase
from PokeApi import PokeApi

class insertarDatos(IStorage):

    def insert_team_data(self, equipo: teambase, entrenador_id: int):
        base = DataBaseInteract()

        return base.insert_team(equipo, entrenador_id)

    def eliminarEquipo(self, equipo: teambase, entrenador_id: int):
        base = DataBaseInteract()
        return base.eliminarEquipo(equipo, entrenador_id)
    
    def insert_pokemon_data(self, pokemon: pokebase):
        base=DataBaseInteract()
        
        return base.inserta_poke(pokemon)


    def insert_entrenador_data(self,entrenadorbase):
        base=DataBaseInteract()
        return base.insert_user(entrenadorbase)

    def read_team_list(self, entrenador: entrenadorbase):
        base=DataBaseInteract()
        team_list = base.consul_teams_by_trainer(entrenador) 

        with open("teams_list.txt", "w") as file:
            for team in team_list:
                team_write = f"{team.id_equipo} {team.team_name}\n"
                file.write(team_write)

        subprocess.run(f"{const.READ_COMMAND} teams_list.txt", shell = True)
        
    def read_team_data(self, string_to_search: str):
        base = DataBaseInteract()
        team_data = base.consul_team(string_to_search) 

        with open("team_data.txt", "w") as file:
            for pokemon in team_data:
                team_data_write = const.pokemon_format.format(**pokemon)
                file.write(team_data_write)
        
        subprocess.run(f"{const.READ_COMMAND} team_data.txt", shell = True)

    def read_pokemon_list(self):
        pokeapi =  PokeApi()
        pokeapi.write_pokemon_list(const.Equipo.generacion)

        subprocess.run(f"{const.READ_COMMAND} pokemon_list.txt", shell = True)

    def get_entrenador_data(self, entrenadorbase):
        base=DataBaseInteract()
        return base.validate_user(entrenadorbase)

    def createPokemon(self, data, generacion: int):
        api = PokeApi()
        return pokebase(**api.create_pokemon(generacion, data))

    def write_move_list(self, pokemon_id: int):
        api = PokeApi()
        api.write_move_list(pokemon_id)

    def read_move_list(self):
        subprocess.run(f"{const.READ_COMMAND} move_list.txt", shell = True)
    