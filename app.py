from flask import Flask
import os


app = Flask(__name__)


@app.get("/")
def pokemon_list():
    return "Bulbasaur, charmander, pikachu, eevee, diglett"


@app.get("/bulbasaur") # write after server link slash for each bit you want
def bulbasaur_data():
    return "This is bulbasaur, a generation 1 pokemon who looks like a tiny dinosaur"


@app.get("/charmander")
def charmander_data():
    return "This is charmander, a generation 1 pokemon who looks like a tiny reptile"


@app.get("/pikachu")
def pikachu_data():
    return "This is pikachu, a generation 1 pokemon who looks like a tiny rodent"


@app.get("/eevee")
def eevee_data():
    return "This is eevee, a generation 1 pokemon who looks like a tiny fox"


@app.get("/diglett")
def diglett_data():
    return "This is diglett, a generation 1 pokemon who looks like a tiny mole"



if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 4445)))
