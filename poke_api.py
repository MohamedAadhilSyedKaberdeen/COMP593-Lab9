'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''

import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def get_pokemon_info(pokemon):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # Clean the Pokemon name parameter by:
    # - Converting to a string object,
    # - Removing leading and trailing whitespace, and
    # - Converting to all lowercase letters
    pokemon = str(pokemon).strip().lower()

    # Check if Pokemon name is an empty string
    if pokemon == '':
        print('Error: No Pokemon name specified.')
        return None

    # Send GET request for Pokemon info
    print(f'Getting information for {pokemon.capitalize()}...', end='')
    url = POKE_API_URL + pokemon
    try:
        resp_msg = requests.get(url)
        resp_msg.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.RequestException as e:
        print(f'failure\nError: {e}')
        return None

    print('success')
    # Return dictionary of Pokemon info
    return resp_msg.json()

if __name__ == '__main__':
    # Test out the get_pokemon_info() function
    poke_info = get_pokemon_info("Rockruff")
    if poke_info:
        print(poke_info)
