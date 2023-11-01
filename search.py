from pymongo import MongoClient
from flask import Flask, jsonify, request, render_template
from random import randint
from bson import json_util
import json


app = Flask(__name__, template_folder='template')

mongo_uri = "mongodb+srv://ecommerce:boom1234@cluster0.wrhg7tc.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"
database_name = "cigarette"  # Replace with your database name
collection_name = "cigaretteData"


client = MongoClient(mongo_uri)
db = client[database_name]
collection = db[collection_name]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/random', methods=['GET'])
def rand():
    json_file = list(collection.find())
    return jsonify({"cigarettes": json.loads(json_util.dumps(json_file[randint(0, len(json_file))]))})


@app.route('/search', methods=['GET'])
def cigarettes():
    try:
        cig_id = str(request.args.get("cig_id")).title()
        json_file = list(collection.find({"name": cig_id}))

        return jsonify({"cigarettes": json.loads(json_util.dumps(json_file[0]))})

    except Exception as e:
        return json.dumps({"error": str(e)}), 500


if __name__ == "__main__":
    app.run()
