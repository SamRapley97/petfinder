from flask import Flask, request, render_template, jsonify
import os
import petpy
import json
import dogs

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

pf = petpy.Petfinder(key=API_KEY, secret=API_SECRET)


app = Flask(__name__)

@app.context_processor
def utility_processor():
    def match_organization_name(org_id):
        organization = pf.organizations(org_id)
        if organization is not None:
            return organization["organizations"]["name"]
        else:
            return "Unknown Organization"  # Or any default value you prefer
    return dict(match_organization_name=match_organization_name)


@app.route("/", methods=["GET", "POST"])
def index():

    all_dog_breeds = dogs.fetch_dog_breeds()

    selected_dog_breed = request.form.get("selected_dog_breed")
    selected_location = request.form.get("selected_location")
    selected_distance = request.form.get("selected_distance")

    dogs.fetch_dogs(selected_dog_breed, selected_location, selected_distance)

    # Read the data from the JSON file
    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Pass the JSON data to the HTML template
    return render_template('index.html', data=data, all_dog_breeds=all_dog_breeds)



if __name__ == "__main__":
    app.run(debug=True)

