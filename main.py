from flask import Flask, jsonify
from zad_3 import get_movies

app = Flask(__name__)

@app.route('/')
def index():
    movies = get_movies()
    return jsonify(movies)

if __name__ == '__main__':
    app.run(debug=True)
