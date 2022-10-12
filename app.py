from flask import Flask
from helpers import get_pokemon_by_name
import os

app = Flask(__name__)


# @app.get("/")
# def pokemon_list():
#     return "Bulbasaur, charmander, pikachu, eevee, diglett"
#
#
# pokemon_creatures = {
#     "bulbasaur": "dinosaur",
#     "charmander": "reptile",
#     "pikachu": "rodent",
#     "eevee": "fox",
#     "diglett": "mole",
# }
#
#
# @app.get("/<pokemon_name>")
# def pokemon_data(pokemon_name):
#     creature = pokemon_creatures.get(pokemon_name)
#     return f"This is {pokemon_name}, a generation 1 pokemon who looks like a tiny {creature}"



# @app.get("/")
# def pokemon_list():
#     return "Bulbasaur, charmander, pikachu, eevee, diglett"
#
#
# @app.get("/<pokemon_name>")
# def pokemon_data(pokemon_name):
#     response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
#     pokemon = response.json()
#     return f"This is {pokemon['name']}.\n" \
#            f"Height: {pokemon['height']}.\n" \
#            f"Weight: {pokemon['weight']}.\n" \
#            f"Base experience: {pokemon['base_experience']}.\n" \
#            f"Type(s): {' and '.join(type_info['type']['name'] for type_info in pokemon['types'])}"
#
#
# if __name__ == "__main__":
#     app.run(host=os.getenv('IP', '0.0.0.0'),
#             port=int(os.getenv('PORT', 4445)))




@app.get("/")
def pokemon_list():
    return "Bulbasaur, charmander, pikachu, eevee, diglett"


@app.get("/<pokemon_name>")
def pokemon_data(pokemon_name):
    pokemon = get_pokemon_by_name(pokemon_name)
    return f"This is {pokemon['name']}.\n" \
           f"Height: {pokemon['height']}.\n" \
           f"Weight: {pokemon['weight']}.\n" \
           f"Base experience: {pokemon['base_experience']}.\n" \
           f"Type(s): {' and '.join(type_info['type']['name'] for type_info in pokemon['types'])}"


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 4445)))
