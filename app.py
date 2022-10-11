from flask import Flask
import os


app = Flask(__name__)


@app.get("/")
def pokemon_list():
    return "Bulbasaur, charmander, pikachu, eevee, diglett"


pokemon_creatures = {
    "bulbasaur": "dinosaur",
    "charmander": "reptile",
    "pikachu": "rodent",
    "eevee": "fox",
    "diglett": "mole",
}


@app.get("/<pokemon_name>")
def pokemon_data(pokemon_name):
    creature = pokemon_creatures.get(pokemon_name)
    return f"This is {pokemon_name}, a generation 1 pokemon who looks like a tiny {creature}"



if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 4445)))

