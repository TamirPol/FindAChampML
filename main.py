from flask import Flask, request, jsonify
from flask_cors import CORS
from usingSavedModel import testImage
app = Flask(__name__)
CORS(app)

@app.route('/mushroom', methods=['POST'])
def process_data():
    image_file = request.files.get("image")
    probabilities = testImage(image_file)
    result = {'probabilities': probabilities}
    return jsonify(result)

@app.route("/test", methods=["GET"])
def test():
    return ({"Yes": "Sir"})
if __name__ == '__main__':
    app.run(host="192.168.50.187", port="5000",debug=True)
