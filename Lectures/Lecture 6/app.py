import json
from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint  # From the package "flask-swagger-ui"


app = Flask(__name__)


# Instructions for flask-swagger-ui
SWAGGER_URL = "/api/docs"  # Where should the user go to read these docs
API_URL = "/static/MovieDB-API.yaml"  # Which file should be used to generate the docs

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "MovieDB API"
    }
)

app.register_blueprint(swaggerui_blueprint)


# List of all movies (Simulates a proper DB)
movies = [
    {"id": 0, "name": "The Dark Knight", "playtime": 152},
    {"id": 1, "name": "Star Wars", "playtime": 125},
    {"id": 2, "name": "Casablanca", "playtime": 102},
    {"id": 3, "name": "Memento", "playtime": 113},
    {"id": 4, "name": "Toy Story", "playtime": 81},
    {"id": 5, "name": "Die Hard", "playtime": 132}
]


# Keep a separate counter for movie ID's. Used when adding new movies.
movie_id_counter = len(movies)


@app.route('/api/v1/movies/<int:movie_id>', methods=['GET', 'DELETE'])
def movie_route(movie_id):
    global movies

    # Get an individual movie
    if request.method == 'GET':
        try:
            for movie in movies:
                if movie['id'] == movie_id:
                    return jsonify(movie), 200

            return jsonify({'error': 'Movie not found'}), 404
        except Exception:
            return jsonify({'error': 'Internal Server Error'}), 500

    # Delete location
    elif request.method == 'DELETE':
        try:
            for enumerated_id, movie in enumerate(movies):
                if movie['id'] == movie_id:
                    movies.pop(enumerated_id)
                    return jsonify({}), 200
            return jsonify({'error': 'Movie not found'}), 404
        except Exception:
            return jsonify({'error': 'Internal Server Error'}), 500


@app.route('/api/v1/movies', methods=['GET', 'POST'])
def movies_route():
    global movies

    # Get all movies
    if request.method == 'GET':
        try:
            return jsonify(movies), 200
        except Exception:
            return jsonify({'error': 'Internal Server Error'}), 500

    # Create a new movie
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            global movie_id_counter
            movie_id_counter += 1
            record['id'] = movie_id_counter

            movies.append(record)

            response = jsonify(record), 201
            response[0].headers.set('Location', f'/api/v1/movies/{movie_id_counter}')
            return response
        except Exception:
            return jsonify({'error': 'Internal Server Error'}), 500


if __name__ == '__main__':
    app.run()
