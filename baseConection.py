from typing import OrderedDict
import pyodbc
from pokemon import pokebase
from entrenador import entrenadorbase
from team import teambase
from getpass import getpass



class DataBaseInteract():
#Creo el conexión string
    def __init__(self):
        self.cnxn_str = pyodbc.connect(r'''Driver={SQL Server};
                    Server=localhost\SQLEXPRESS;
                    Database=Pokedatabase;
                    Trusted_Connection=yes;''')
                    
        self.cursor = self.cnxn_str.cursor()
    ################################ Poke-sql querys ###############################

    def insert_user(self,entrenador: entrenadorbase):
        query =  self.cursor.execute(f'''SELECT COALESCE( (SELECT 1
		                             FROM Entrenador
                                    WHERE nombre_entrenador = '{entrenador.nombre.lower()}'), -1) ''')

        if [i for i in query][0][0] == -1:
            query = self.cursor.execute(f'''INSERT INTO Entrenador(nombre_entrenador, [password]) 
		                                VALUES ('{entrenador.nombre.lower()}', '{entrenador.password.lower()}')''')
            self.cnxn_str.commit()
            return True

        return False
        
    def validate_user(self, entrenador: entrenadorbase):

        query = self.cursor.execute(f'''SELECT COALESCE((SELECT id_entrenador
				                                    FROM Entrenador
				                                    WHERE nombre_entrenador = '{entrenador.nombre.lower()}'
					                                AND password = '{entrenador.password.lower()}' ), -1)''')
        
        return [i for i in query][0][0]
    
    def inserta_poke(self, poke: pokebase):
        if self.cursor.execute(f'''
                                    DECLARE @equipo_id AS Integer
                                    SET @equipo_id = (SELECT IDENT_CURRENT('Team'))

                                    INSERT INTO Pokemon(id_equipo,
                                                        id_pokedex,
                                                        nombre, 
                                                        tipo, 
                                                        especie, 
                                                        move_one, 
                                                        move_two, 
                                                        move_three, 
                                                        move_four) 
        VALUES (@equipo_id, {poke.id_pokedex}, '{poke.nombre}', '{poke.tipo}', '{poke.especie}', '{poke.move_one}',  '{poke.move_two}', '{poke.move_three}', '{poke.move_four}')'''):
            self.cnxn_str.commit()
            return True
        
        return False
    
    def delete_poke(self):#pasarle id
        if(self.cursor.execute("DELETE FROM pokemon WHERE id_equipo = '{}'")):
            print("Se borraron los pokemon correctamente")
            self.cnxn_str.commit()
            #return "Se borraron los pokemon correctamente"
        else:
            print("No se eliminó")
            #return "No se eliminó"

    def consul_team(self, string_to_search):
        id_to_search = -1

        if string_to_search.isnumeric():
            id_to_search = int(string_to_search)

        query = f'''DECLARE @string_to_search VARCHAR(100)
                    DECLARE @id_to_search INTEGER

                    SET @string_to_search = '{string_to_search}'
					SET @id_to_search = {id_to_search}
          
                    SELECT  T.team_name,
                            P.id_pokedex,
                            P.nombre, 
                            P.tipo, 
                            P.especie, 
                            P.move_one, 
                            P.move_two, 
                            P.move_three, 
                            P.move_four 
                    FROM Team T
                    INNER JOIN Pokemon P
                        ON T.id_equipo = P.id_equipo
                    WHERE T.team_name LIKE @string_to_search
                        OR T.id_equipo = @id_to_search'''
 
        self.cursor.execute(query)
        poke_list = []

        for row in self.cursor:
            pokedict = {
                        "pokedex_id": row[1],
                        "nombre": row[2],
                        "tipo": row[3],
                        "especie": row[4],
                        "move_one": row[5],
                        "move_two": row[6],
                        "move_three": row[7],
                        "move_four": row[8]
                        }

            poke_list.append(pokedict)

        return poke_list

    def consul_teams_by_trainer(self, entrenador: entrenadorbase):
        query = f'''SELECT id_equipo, team_name 
                    FROM Team 
                    WHERE  id_entrenador = {entrenador.entrenadorId}'''

        self.cursor.execute(query)

        equipos = []
        for row in self.cursor:
            equipo = teambase() 
            equipo.id_equipo = row[0]
            equipo.team_name =  row[1]

            equipos.append(equipo)

        return [equipo for equipo in equipos]

    def insert_team(self, equipo: teambase, entrenador_id: int): 
        if self.cursor.execute(f'''IF NOT EXISTS(SELECT 1
                                    FROM Team
                                    WHERE id_entrenador = {entrenador_id}
                                        AND team_name LIKE '{equipo.team_name}')
                                    BEGIN
                                
                                        INSERT INTO Team(id_entrenador, team_name) 
                                        VALUES ('{entrenador_id}', '{equipo.team_name}')

                                    END
                                 '''):
            self.cnxn_str.commit()
            return True

        return False
    
    def insert_pokemon(self, pokemon: pokebase, equipo_id: int): 
        if self.cursor.execute(f'''INSERT INTO Pokemon(id_pokedex,
                                                      id_equipo,
                                                      nombre,
                                                      tipo,
                                                      especie,
                                                      move_one,
                                                      move_two,
                                                      move_three,
                                                      move_four)
                                 VALUES({pokemon.pokedex_id}, {pokemon.equipo_id}, '{pokemon.nombre}', '{pokemon.tipo}', '{pokemon.especie}', '{pokemon.move_one}', '{pokemon.move_two}', '{pokemon.move_three}', '{pokemon.move_four}')'''
                             ):
            
            self.cnxn_str.commit()
            return True

        return False

    def eliminarEquipo(self, string_to_search, entrenador_id: int):
        id_to_search = -1

        if isinstance(string_to_search, int):
            id_to_search = string_to_search

        if(self.cursor.execute(f''' DECLARE @id_equipo INT
                                    SET @id_equipo = (SELECT id_equipo
                                                      WHERE team_name = '{string_to_search}'
                                                      OR id_equipo = '{id_to_search}'
                                                        AND id_entrenador = '{entrenador_id})'
                                DELETE FROM Team 
                                  WHERE team_name = '{string_to_search}'
                                    OR id_equipo = '{id_to_search}' 
                                  AND id_entrenador = {entrenador_id}
                                  
                                  DELETE Pokemon
                                  WHERE id_equipo = @id_equipo
                                  ''')):
            self.cnxn_str.commit()  
            return True
        return False