from getpass import getpass
from os import system, name

import const
from PokeApi import PokeApi
from domainInsercion import insertarDatos


def opening_screen():
    def clear(): 
        system(const.CLEAR_COMMAND)

    clear()
    with open("pokemon_logoTB.txt") as reader:
        content = reader.read()
        print(content)

def efectoOpcionesEntrenador():
    opening_screen()
    opcionesEntrenador()

def efectoOpcionesEquipo():
    opening_screen()
    opcionesEquipo()

def efectoOpcionesPokemon():
    opening_screen()
    opcionesPokemon()

def insertarPokemon(datos: list):
    pass

def insercionPokemon():
    pass

def listarEquipos():
    getdatos = insertarDatos()
    getdatos.read_team_list(const.Entrenador)
    opening_screen()
    efectoOpcionesEntrenador()

def listarPokemonDisponibles():
    domain = insertarDatos()
    domain.read_pokemon_list()
    efectoOpcionesEquipo() 

def verEquipo():
    domain = insertarDatos()
    string_to_search = str(input("Nombre o id del equipo:"))

    domain.read_team_data(string_to_search)
    efectoOpcionesEntrenador()

def verEquipoActual():
    pass

def agregarPokemon():
    domain = insertarDatos()
    pokemon = domain.createPokemon(input("id o nombre de pokemon a insertar:"), const.Equipo.generacion)
    
    if pokemon.id_pokedex != -1:
        if  len(const.Equipo.lista_pokemon) < 6:
            const.Equipo.lista_pokemon.append(pokemon) 
        else: 
            print("Un equipo solo puede tener maximo 6 pokemon")
    else:
        print(f"Pokemon no disponible en la generacion {const.Equipo.generacion}")
        
    opcionesEquipo()

def eliminarPokemon():
    indice_pokemon_eliminar = int(input("Indice de pokemon a eliminar:"))
    const.Equipo.lista_pokemon.remove(const.Equipo.lista_pokemon[indice_pokemon_eliminar])
    opcionesEquipo()

def agregarMovimiento():
    numero = input("numero movimiento a modificar: ")
    movimiento = input("movimiento a agregar: ").lower()
    learnable = False

    with open('move_list.txt') as f:
        if movimiento in f.read():
            learnable = True

    if learnable:
        if numero == "1":
            const.pokemon_a_modificar.move_one = movimiento
        elif numero == "2":
            const.pokemon_a_modificar.move_two = movimiento
        elif numero == "3":
            const.pokemon_a_modificar.move_three = movimiento
        elif numero == "4":
            const.pokemon_a_modificar.move_four = movimiento
        else:
            print("Un pokemon solo puede tener 4 movimientos")
    else:
        print("Movimiento no puede ser aprendido")

    modificarPokemon()

def cambiarNombre():
    const.pokemon_a_modificar.nombre = input("Nuevo nombre del pokemon: ")
    modificarPokemon()


def setPokemonAModificar():
    base = insertarDatos()
    const.index = int(input("Indice Pokemon a modificar: "))

    const.pokemon_a_modificar = const.Equipo.lista_pokemon[const.index]
    base.write_move_list(const.pokemon_a_modificar.id_pokedex)
    modificarPokemon()

def modificarPokemon():
    print(const.pokemon_format.format(**const.pokemon_a_modificar.toDict()))
    opcionesPokemon()

def guardarPokemon():
    const.Equipo.lista_pokemon[const.index] = const.pokemon_a_modificar
    opcionesEquipo()

def guardarEquipo():
    domain = insertarDatos()
    const.Equipo.team_name = input("Nombre del equipo: ")

    if domain.insert_team_data(const.Equipo, const.Entrenador.entrenadorId):
        print("Equipo guardado con exito")
        for pokemon in const.Equipo.lista_pokemon:
            if domain.insert_pokemon_data(pokemon): 
                continue
            else:
                print("Error guardando pokemon")
                efectoOpcionesEquipo()

        efectoOpcionesEquipo()
    else:
        print("Error al guardar equipo")
        efectoOpcionesEquipo()

def eliminarEquipo():
    domain = insertarDatos()
    if domain.eliminarEquipo(input("id o nombre de equipo a eliminar: "), const.Entrenador.entrenadorId):
        print("Equipo eliminado con exito")
    else:
        print("Error al eliminar equipo")
    efectoOpcionesEquipo()

def listarMovimientosDisponibles():
    domain = insertarDatos()
    domain.read_move_list()
    modificarPokemon()

def eliminarMovimiento():
    numero = input("numero del movimiento a eliminar: ")

    if numero == "1":
            const.pokemon_a_modificar.move_one = ""
    elif numero == "2":
            const.pokemon_a_modificar.move_two = ""
    elif numero == "3":
            const.pokemon_a_modificar.move_three = ""
    elif numero == "4":
            const.pokemon_a_modificar.move_four = ""

    modificarPokemon()

def iniciarSesion():
    def validar(entrenador):
        getdatos = insertarDatos()
        const.Entrenador = entrenador
        const.Entrenador.entrenadorId = getdatos.get_entrenador_data(entrenador)

        if  const.Entrenador.entrenadorId > 0:
            return True

        return False
    
    entrenador = const.Entrenador
    entrenador.nombre = input("Entrenador: ")
    entrenador.password = getpass("Password: ")
    
    if validar(entrenador):
        opening_screen()
        opcionesEntrenador()
    else:
        opening_screen()
        print("Credenciales Invalidas\n")
        opcionesInicio()

def registrarUsuario():
    def registrar(entrenador):
            guardar = insertarDatos()
            return guardar.insert_entrenador_data(entrenador)

    entrenador = const.Entrenador
    entrenador.nombre = input("Entrenador: ")
    entrenador.password = getpass("Password: ")

    if registrar(entrenador): 
        opening_screen()
        print('Se registro al entrenador de manera exitosa')
    else:
        opening_screen() 
        print("Usuario Existente")

    opcionesInicio()

def setGeneracion():
    equipo = const.Equipo
    equipo.generacion = int(input("Numero de generacion: "))
    const.Equipo = equipo
    opcionesEquipo()

def opcionesEquipo():

    for i, pokemon in enumerate(const.Equipo.lista_pokemon):
        print(f"\nIndice: {i}")
        print(const.pokemon_format.format(nombre_equipo = const.Equipo.team_name ,**pokemon.toDict()))


    print(f"Entrenador@: {const.Entrenador.nombre}")
    opciones = {1: listarPokemonDisponibles,
                2: setPokemonAModificar,
                3: agregarPokemon,            
                4: eliminarPokemon,
                5: guardarEquipo,
                0: efectoOpcionesEntrenador}

    print(const.MENU_EQUIPO)
    opcion = int((max(input(), "-1")))

    respuesta = opciones.get(opcion, 
                            opcionesEquipo
                            )
    respuesta()

def opcionesPokemon():

    opciones = {1: listarMovimientosDisponibles,
                2: agregarMovimiento,
                3: cambiarNombre,
                4: eliminarMovimiento,
                5: guardarPokemon,
                0: opcionesEquipo}

    print(const.MENU_POKEMON)
    opcion = int(input())

    respuesta = opciones.get(opcion, 
                            modificarPokemon
                            )
    respuesta()

def opcionesEntrenador():

    print(f"Entrenador@: {const.Entrenador.nombre}")
    opciones = {1: listarEquipos,
                2: verEquipo,
                3: setGeneracion,
                4: eliminarEquipo,
                0: main}

    print(const.MENU_ENTRENADOR)
    opcion = int((max(input(), "-1")))

    respuesta = opciones.get(opcion, 
                            opcionesEntrenador
                            )
    respuesta()
            
def opcionesInicio():
    opciones = {1: iniciarSesion,
                2: registrarUsuario,
                0: exit}

    print(const.MENU_INICIAL)
    opcion = int(input())

    respuesta = opciones.get(opcion, 
                            main
                            )
    respuesta()
            
#def suma(numun,numdos):
 #   numun=int(numun)
  #  numdos=int(numdos)
   # return numun+numdos

def main():
    opening_screen()
    opcionesInicio()

def config():
    const.USER_OS = name
    const.READ_COMMAND = "more" if name == "nt" else "less"
    const.CLEAR_COMMAND = "cls" if name == "nt" else "clear"

if __name__ == "__main__":
    config()
    main() 