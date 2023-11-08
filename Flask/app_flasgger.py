from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/')
def home():
    return f'Welcome to my flask about games!'

@app.route('/games', methods=['GET'])
def game_get():
    """
    This endpoint returns a response about the game you play.
    ---
    parameters:
      - name: game
        in: query
        type: string
        required: false
        default: League of Legends
    responses:
      200:
        description: This is stating the game you play.
    """

    game = request.args.get('game', 'League')
    return f'The game you play is called {game}!'

    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400
    
    game = data.get('game', 'League')
    return jsonify({'message': f'I see that you play {game}!'})

if __name__ == '__main__':
    app.run(debug=True)