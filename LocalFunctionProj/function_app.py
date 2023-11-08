import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="games")
def game_get(req: func.HttpRequest) -> func.HttpResponse:
    game = req.params.get("game")
    if not game:
        game = "League"
    if game:
        return func.HttpResponse(f'You played {game}!')