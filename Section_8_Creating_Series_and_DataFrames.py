# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Create a data dictionary that looks like the DataFrame below
data = {
    'evolution': ['Ivysaur', 'Charmeleon', 'Wartortle', 'Raichu', 'Tamtam', 'Venusaur', 'Charizard', 'Blastoise', 'Pukpuk', 'Flareon'],
    'hp': [45, 39, 44, 35, 55, 80, 78, 79, 85, 65],
    'name': ['Bulbasaur', 'Charmander', 'Squirtle', 'Pikachu', 'Eevee', 'Ivysaur', 'Charmeleon', 'Wartortle', 'Raichu', 'Flareon'],
    'pokedex': [1, 4, 7, 25, 133, 2, 5, 8, 26, 136],
    'type': ['Grass', 'Fire', 'Water', 'Electric', 'Normal', 'Grass', 'Fire', 'Water', 'Electric', 'Fire']
}

# Step 3. Assign it to a variable called pokemon
print(f"------------Step 3. Assign it to a variable titanic")
pokemon = pd.DataFrame(data)
print(pokemon)

# Step 4. Ops...it seems the DataFrame columns are in alphabetical order. Place the order of the columns as name, type, hp, evolution, pokedex
print(f"------------Step 4. Ops...it seems the DataFrame columns are in alphabetical order. Place the order of the columns as name, type, hp, evolution, pokedex")
pokemon = pokemon[['name', 'type', 'hp', 'evolution', 'pokedex']]
print(pokemon)

# Step 5. Add another column called place, and insert what you have in mind.
print(f"------------Step 5. Add another column called place, and insert what you have in mind.")
data['place'] = ['Forest', 'Volcano', 'Ocean', 'Power Plant', 'Grassy Field', 'Jungle', 'Mountain', 'Lake', 'Power Plant', 'Volcano']
pokemon = pd.DataFrame(data)
print(pokemon)

# Step 6. Present the type of each column
print(f"------------Step 6. Present the type of each column")
print(pokemon.dtypes)

# BONUS: Create your own question and answer it.
# How can I calculate the average HP of Electric-type Pokémon in the Pokémon dataset?
print(f"------------How can I calculate the average HP of Electric-type Pokémon in the Pokémon dataset?")
electric_pokemon = pokemon[pokemon['type'] == 'Electric']
average_hp_electric = electric_pokemon['hp'].mean()
print("The average HP of Electric-type Pokémon is:", average_hp_electric)
