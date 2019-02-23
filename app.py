from flask import Flask, jsonify, request
from logic import locationsWithinBudget

app = Flask(__name__)


@app.route('/trip/v1/', methods=['POST'])
def predict_trip():
    data = request.get_json()
    present_location = data['present_location']
    budget = int(data['budget'])
    zone = data['zone'].replace(' ','').lower()
    available_locations = locationsWithinBudget(budget, present_location, zone)

    return jsonify(available_locations)


@app.route('/')
def index():
    return 'Welcome to the Trip Recommendation'


if __name__ == '__main__':
    app.run(debug=True)


