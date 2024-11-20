from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define the '/recommend' endpoint
@app.route('/recommend', methods=['POST'])
def recommend():
    # Get the JSON data from the POST request
    data = request.get_json()

    if not data or 'responses' not in data:
        return jsonify({"error": "Invalid request, 'responses' key missing"}), 400

    # Extract the responses (this should be replaced by your logic)
    responses = data['responses']

    # Dummy logic to return a recommendation based on responses
    # Replace this with your machine learning model prediction logic
    recommendation = {
        "brand": "Sample Brand",
        "collection": "Sample Collection",
        "style": "Sample Style",
        "price": "Sample Price",
    }

    # Respond with the recommendation
    return jsonify({
        "recommendation": recommendation
    })

if __name__ == '__main__':
    app.run(port=5001)
