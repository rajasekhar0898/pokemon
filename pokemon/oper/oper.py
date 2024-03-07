from flask import flash
from pokemon.routes import *
from ..models.models import USER1, Pokemons
from pokemon.extensions.db import db


def user_details(username):
    return USER1.query.filter_by(name=username).first()


def search_pokemon(search_term):
    return Pokemons.query.filter((Pokemons.name.like(f'%{search_term}%')) | (Pokemons.id == search_term)).all()

def insert_user(name, email,password):
    user = USER1(name=name,email=email, password=password)  # Create a new instance of the USER class
    db.session.add(user)  # Add the user instance to the session
    db.session.commit()  
                          # Commit the transaction to the database
                          
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"Error in {getattr(form, field).label.text}: {error}", "error")


def insert_pokemon_data(name, image_url, description, height, weight, category, abilities, image_path):
    new_pokemon = Pokemons(name=name, image_url=image_url, description=description, height=height,
                          weight=weight, category=category, abilities=abilities, image_path=image_path)
    db.session.add(new_pokemon)
    db.session.commit()

def fetch_pokemon_details():
    return Pokemons.query.all()

def delete_pokemon_data(pokemon_id):
    pokemon = Pokemons.query.get(pokemon_id)
    db.session.delete(pokemon)
    db.session.commit()

def fetch_pokemon_by_id(pokemon_id):
    return Pokemons.query.get(pokemon_id)

def update_pokemon_data(pokemon_id, form):
    pokemon = Pokemons.query.get(pokemon_id)
    pokemon.name = form.name.data
    pokemon.image_url = form.image_url.data
    pokemon.description = form.description.data
    pokemon.height = form.height.data
    pokemon.weight = form.weight.data
    pokemon.category = form.category.data
    pokemon.abilities = form.abilities.data
    db.session.commit()

