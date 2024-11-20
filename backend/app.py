from flask import Flask, request, jsonify, CORS

app = Flask(__name__)
CORS(app)

# Sample route to test
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Watch Recommendation API!"})

if __name__ == '__main__':
    app.run(port=5001)
