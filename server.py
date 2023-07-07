from flask import Flask, jsonify
app = Flask(__name__)
CORS(app)

@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify({
        'message': "Like this video if this helped!"
        'people': ['Jack', 'Harry', 'Apran']

    })

if __name__ == "__main__":

    app.run(debug=True, port=8080)