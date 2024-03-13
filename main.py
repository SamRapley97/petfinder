import petpy
import os
import json
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

pf = petpy.Petfinder(key=API_KEY, secret=API_SECRET)

# Specify multiple breeds in a list
breeds = ["Labrador Retriever", "Spaniel"]
combined_results = []

# Make a separate API request for each breed and combine the results
for breed in breeds:
    result = pf.animals(animal_type="dog", breed=breed, house_trained=True, location="San Antonio, TX", distance="50")
    combined_results.extend(result["animals"])

# Save the combined results to a JSON file
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump({"animals": combined_results}, f, ensure_ascii=False, indent=4)

app = Flask(__name__)

@app.route("/")
def display_json():

    # Read the data from the JSON file
    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Pass the JSON data to the HTML template
    return render_template('hello.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)



