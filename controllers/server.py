from fastapi import Request, Response, status
from utils import HTTP
from datetime import datetime
import os
import time

def health(request: Request, response: Response):
    http = HTTP(response)
    payload = {
        "identity": os.getpid(),
        "uptime": time.time() - os.getppid(),
        "timestamp": datetime.utcnow().isoformat() + 'Z'
    }
    return http.response(status.HTTP_200_OK, payload)
