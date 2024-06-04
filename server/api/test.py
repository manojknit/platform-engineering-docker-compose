import os
import logging
import requests
from fastapi import HTTPException, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
import uvicorn

app = FastAPI()

origins = [
    "*",  # allow all origins
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UseCase:
    """use case."""

    def __init__(self, city: str):
        self.city = city
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.api_key = "dbb01c03954080c8b7ff6db81528f028"

    def func1(self):
        url = f"{self.base_url}?q={self.city}&appid={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="Error fetching weather data")

    def run(self):
        return self.func1()

@app.get("/")
async def health_check():
    return {"status": "ok"}

@app.get("/use_case/{params}")
def get_use_case(params: str):
    use_case = UseCase(params)
    return {"result": use_case.run()}

@app.get("/code/{s}")
def random_code_return(s: str) -> None:
    return {"code": s}

@app.post("/external_api")
def fetch_external_data(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Error fetching data")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
