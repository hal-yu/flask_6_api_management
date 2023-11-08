from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return f'Welcome to my flask about playing games!'

@app.route('/games', methods=['GET'])
def game_get():
    game = request.args.get('game', 'League')
    return jsonify({'message': f'I see that you play {game}!'})


if __name__ == '__main__':
    app.run(debug=True)

## test CURL for post:
# curl -X POST http://localhost:5000/hello -H "Content-Type: application/json" -d '{"name": "Cooper"}'

## test CURL for get:
# curl -X GET http://localhost:5000/hello?name=Cooper