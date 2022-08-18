import sys

# setting path
sys.path.append('../python_automation_with_pokemon')

from apiClients.Pokemon import *

class PokemonLogic:

    name: str = ""

    def __init__(self):
        self.name = "NoName"

    # instance methods
    def isThereAPokemonWithThisName(self, pokemonName: str) -> bool:
        response = pokemon_byName_GET(pokemonName.lower())
        if response.status_code == 200:
            return True
        else:
            return False

    def isThereAPokemonWithThisNumber(self, pokemonNumber: int) -> bool:
        response = pokemon_byNumber_GET(pokemonNumber)
        if response.status_code == 200:
            return True
        else:
            return False
