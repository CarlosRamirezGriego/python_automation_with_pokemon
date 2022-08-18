import sys

# setting path
sys.path.append('../python_automation_with_pokemon')

from api_clients.Pokemon import *

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

    def returnAllInformationFromPokemonWithThisName(self, pokemonName: str):
        exist: bool = self.isThereAPokemonWithThisName(pokemonName)
        response = pokemon_byName_GET(pokemonName.lower())
        if not exist:
            print("returnAllInformationFromPokemonWithThisName() didnt return information for Pokemon named: "+pokemonName)
        return response


    def returnAllInformationFromPokemonWithThisNumber(self, pokemonNumber: int):
        exist: bool = self.isThereAPokemonWithThisNumber(pokemonNumber)
        response = pokemon_byNumber_GET(pokemonNumber)
        if not exist:
            print("returnAllInformationFromPokemonWithThisNumber() didnt return information for Pokemon named: "+pokemonNumber)
        return response

    def returnNameOfPokemonWithThisNumber(self, pokemonNumber: int):
        name: str = ""
        response = self.returnAllInformationFromPokemonWithThisNumber(pokemonNumber);
        if response.status_code == 200:
            data = response.json()
            name = data["name"]
        else:
            print("returnNameOfPokemonWithThisNumber() didnt return information for Pokemon number: "+pokemonNumber)
        return name

    def returnNumberOfPokemonWithThisName(self, pokemonName: str):
        id: int = -1
        response = self.returnAllInformationFromPokemonWithThisName(pokemonName);
        if response.status_code == 200:
            data = response.json()
            id = data["id"]
        else:
            print.log("returnNumberOfPokemonWithThisName() didnt return information for Pokemon number: "+pokemonName)
        return id