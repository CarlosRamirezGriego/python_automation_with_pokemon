import sys

# setting path
sys.path.append('../python_automation_with_pokemon')

from businessLogic.api.PokemonLogic import PokemonLogic


def test_exampleForAPI():
    apiLogic = PokemonLogic()
    pkNumber: int = apiLogic.returnNumberOfPokemonWithThisName("Pikachu")
    pkName: str = apiLogic.returnNameOfPokemonWithThisNumber(25)
    assert pkNumber == 25
    assert pkName == "pikachu"