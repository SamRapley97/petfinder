import os
import json
import petpy
from dotenv import load_dotenv
from flask import request



load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

pf = petpy.Petfinder(key=API_KEY, secret=API_SECRET)

def fetch_dog_breeds():
    all_dog_breeds = pf.breeds(types='dog')
    return all_dog_breeds

def fetch_dogs(selected_dog_breed, selected_location, selected_distance):

    print(selected_distance)
 
    results = []
    dog_search = pf.animals(animal_type="dog", breed=selected_dog_breed, location=selected_location, distance=selected_distance)
    results.extend(dog_search["animals"])
    
    # Save the combined results to a JSON file
    with open('data.json', 'w', encoding='utf-8') as f:
        x = json.dump({"animals": results}, f, ensure_ascii=False, indent=4)    
    
    return x


