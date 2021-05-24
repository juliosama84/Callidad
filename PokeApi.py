import requests
import subprocess
import json

class PokeApi():

    def write_pokemon_list(self, generation: int):
        total_pokemon_by_gen = [151, 251, 386, 493, 649, 721, 809, 898]
        pokeURL = "https://pokeapi.co/api/v2/pokemon?limit={}"

        r = requests.get(pokeURL.format(total_pokemon_by_gen[generation - 1]))
        data = r.json()

        with open("pokemon_list.txt", "w") as handle:
            i = 1
            for pokemon in data.get("results"):
                handle.write(f"{i} " + pokemon["name"] + "\n")
                i += 1

    def write_move_list(self, pokemon: int):
        pokeURL = "https://pokeapi.co/api/v2/pokemon/{}"

        r = requests.get(pokeURL.format(pokemon))
        data = r.json()

        with open("move_list.txt", "w") as handle:
            for i in data.get("moves"):
                handle.write(i["move"]["name"] + "\n")


    def create_pokemon(self, generacion, data):
        total_pokemon_by_gen = [151, 251, 386, 493, 649, 721, 809, 898]
        pokeURL = "https://pokeapi.co/api/v2/pokemon/{}/"

        data = data.lstrip().rstrip().lower()

        if data != -1: pokeURL = pokeURL.format(data)
        else:
            data = data.lower() 
            pokeURL = pokeURL.format(data)

        r = requests.get(pokeURL)
        if r.content == b"Not Found": return {}

        data = r.json()
        pokedex_id = data.get("id")

        if int(pokedex_id) > total_pokemon_by_gen[generacion-1]: return {}

        types = [i for i in data.get("types")]
        types = "-".join([i["type"]["name"] for i in types])

        return {"id_pokedex": pokedex_id,
                "especie": data.get("name"),
                "tipo": types
                }

####