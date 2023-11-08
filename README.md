# flask_6_api_management
The goal of this week's assignment is to develop, document, and manage APIs using Flask. You'll also explore the differences between the two frameworks and integrate your APIs with Azure API Management.

#Endpoint: Games
I created an endpoint called games. It receives information about the name of the game you play, which in turns returns the message "I see you play [game name]". 

- In the [function_app.py file](https://github.com/hal-yu/flask_6_api_management/blob/main/LocalFunctionProj/function_app.py), the ```@app.route(route="games")``` will have the URL displayed at end with /games.
- The function ```def game_get(req: func.HttpRequest) -> func.HttpResponse:``` is important for an API because it gives the entry point to handle requests. 
- The ```game = req.params.get("game")``` is important because it provides a parameter for the request.
- The code block:
```
    if not game:
        game = "League"
    if game:
        return func.HttpResponse(f'You played {game}!')
```
is important for testing the API response. 
