from flask import Flask, request, render_template, jsonify
import json
import dogs



app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def display_json():

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

