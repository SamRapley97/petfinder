import petpy
import os
import json
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')


pf = petpy.Petfinder(key=API_KEY, secret=API_SECRET)
x = pf.animals(animal_type="dog", breed="Spaniel", house_trained="true", location="San Antonio, TX", distance="50")
print(x)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(x, f, ensure_ascii=False, indent=4)





