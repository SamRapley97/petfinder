from flask import Flask, request, render_template, jsonify
import json
import dogs



app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def display_json():

    all_dog_breeds = dogs.fetch_dog_breeds()

    dogs.fetch_dogs(request.form.get("selected_dog_breed"))

    # Read the data from the JSON file
    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Pass the JSON data to the HTML template
    return render_template('hello.html', data=data, all_dog_breeds=all_dog_breeds)


if __name__ == "__main__":
    app.run(debug=True)

