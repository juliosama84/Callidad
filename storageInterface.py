from abc import ABCMeta, abstractmethod

class IStorage():
  
    @abstractmethod
    def insert_team_data(self,teambase):
        pass
        

    @abstractmethod
    def insert_pokemon_data(self,pokebase):
        pass

    @abstractmethod
    def get_team_data(self,teambase):
        pass
 
    @abstractmethod
    def read_team_list(self, entrenadorId: int):
        pass

    @abstractmethod
    def get_pokemon_data(self,pokebase):
        pass
   
    @abstractmethod
    def insert_entrenador_data(self,entrenadorbase):
        pass


    @abstractmethod
    def get_entrenador_data(self,entrenadorbase):
        pass
