from fastapi import FastAPI
from controllers import ServerController

app = FastAPI()

@app.get("/api/health")
def heath_api(request, response):
    return ServerController.health(request, response)