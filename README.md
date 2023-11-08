# flask_6_api_management
The goal of this week's assignment is to develop, document, and manage APIs using Flask. You'll also explore the differences between the two frameworks and integrate your APIs with Azure API Management.

#Endpoint: Games
I created an endpoint called games. It receives information about the name of the game you play, which in turns returns the message "I see you play [game name]". 

- In the [function_app.py file](https://github.com/hal-yu/flask_6_api_management/blob/main/LocalFunctionProj/function_app.py), the ```@app.route(route="games")``` will have the URL displayed at end with /games.
- The function ```def game_get(req: func.HttpRequest) -> func.HttpResponse:``` is important for an API because it gives the entry point to handle requests. 
- The ```game = req.params.get("game")``` is important because it provides a parameter for the request.
- The code block is important for testing the API response. 
```
    if not game:
        game = "League"
    if game:
        return func.HttpResponse(f'You played {game}!')
```

# Azure API Management Integration
1. Install Azure CLI with ```curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash```
2. Use ```az login --use-device-code```
3. Install Azure Functions Core Tool using ```Install Azure Functions Core Tool with this code: sudo apt-get install azure-functions-core-tools-4```
4. Use ```func init``` to create a LocalFinctionProj folder
5. In **local.settings.json**, edit in ```"UseDevelopmentStorage=true"``` next to  **"AzureWebJobsStorage:"**
6. Edit the function_app.py file.
7. Create a resource group using ``` az group create --name <RESOURCE GROUP NAME>-rg --location <REGION>```
8. Create a storage account using ```az storage account create --name <STORAGE ACCOUNT NAME> --location <REGION> --resource-group <RESOURCE GROUP NAME> --sku Standard_LRS
9. Create a function app  using ```az functionapp create --resource-group <RESOURCE GROUPNAME> -rg --consumption-plan-location <REGION> --runtime python --runtime-version 3.9 --functions-version 4 --name <FUNCTION APP NAME> --os-type linux --storage account <STORAGE ACCOUNT NAME>
10. Deploy using ```func azure functionapp publish <FUNCTION APP NAME>. After it is deployed, they should provide you with a link.

# Challenges
I got the "This page isn't working" several times after I tried to open my link. I realized that there was an error with my function_app.py file and after making edits, I continued to encounter this error because I forgot to republish it. Another error I encountered was i initially had the same variable name for my route and variable "game" before I change the route one to "games." 
