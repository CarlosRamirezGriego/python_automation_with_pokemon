import sys

# setting path
sys.path.append('../python_automation_with_pokemon')

from businessLogic.api.PokemonLogic import PokemonLogic


def test_exampleForAPI():
    apiLogic = PokemonLogic()
    pkNumber: str = apiLogic.returnNumberOfPokemonWithThisName("Pikachu")
    assert pkNumber == 25