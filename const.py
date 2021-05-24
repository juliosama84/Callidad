from pokemon import pokebase
from team import teambase
from entrenador import entrenadorbase

MENU_INICIAL = f"{'#'*3} MENU {'#'*3}\n1: Iniciar Sesion\n2: Registrarse\n0: Salir\n"
MENU_ENTRENADOR = f"{'#'*3} OPCIONES {'#'*3}\n1: Listar Equipos\n2: Ver Equipo\n3: Crear Equipo\n4: Eliminar Equipo\n0: Cerrar Sesion\n"
MENU_EQUIPO = f"{'#'*3} OPCIONES {'#'*3}\n1: Listar Pokemon disponibles\n2: Modificar Pokemon\n3: Agregar a Equipo\n4: Eliminar de Equipo \n5: Guardar Equipo\n0: Regresar\n"

MENU_POKEMON = f"{'#'*3} OPCIONES {'#'*3}\n1: Listar Movimientos Disponibles\n2: Agregar movimiento\n3: Cambiar Nombre\n4: Eliminar Movimiento\n5: Guardar Pokemon\n0: Regresar\n"


pokemon_format = '''\nPOKEMON {nombre}\nPOKEDEX_ID: {pokedex_id}\nESPECIE: {especie}  TIPO: {tipo}\n------------------------\nMOVIMIENTO 1: {move_one}\nMOVIMIENTO 2: {move_two}\nMOVIMIENTO 3: {move_three}\nMOVIMIENTO 4: {move_four}\n    '''

Entrenador = entrenadorbase()
Equipo =  teambase()
Pokemon = pokebase()

pokemon_a_modificar = pokebase()
index = 1

USER_OS = ""
READ_COMMAND = ""
CLEAR_COMMAND = ""