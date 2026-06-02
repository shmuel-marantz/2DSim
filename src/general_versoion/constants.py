import yaml

with open ('general_version.yaml') as file:
    config = yaml.safe_load(file)

GRID_WIDTH = config['simulation']['grid_width']
GRID_HEIGHT = config['simulation']['grid_height']
ROCK_AMOUNT = config['initialization']['rock_amount']
PLANT_AMOUNT = config['initialization']['plant_amount']
HERBIVORE_AMOUNT = config['initialization']['herbivore_amount']
PREDATOR_AMOUNT = config['initialization']['predator_amount']
PLANT_LIFESPAN = config['entities']['plant']['lifespan']
HERBIVORE_LIFESPAN = config['entities']['herbivore']['lifespan']
PREDATOR_LIFESPAN = config['entities']['predator']['lifespan']
PREVENTS_REPRODUCTION = config['entities']['herbivore']['prevents_reproduction']
SPAWN_CHANCE = config['entities']['plant']['spawn_chance']
