import os
import logging
import redis
from fastapi import HTTPException, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
import uvicorn

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file named 'app.log'
        logging.StreamHandler()          # Also log to console
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI()
cache = redis.Redis(host='redis', port=6379)

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

    def func1(self):
        return f"Function 1 executed for city {self.city}"

    def run(self):
        return self.func1()

@app.get("/")
async def health_check():
    return {"status": "ok"}

@app.get("/use_case/{city}")
def get_use_case(city: str):
    try:
        use_case = UseCase(city)
        result = use_case.run()
        
        # Increment city count in Redis
        count = cache.incr(city)
        logger.info(f"City: {city}, Count: {count}")
        
        return {"result": result, "city_count": count}
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/code/{s}")
def random_code_return(s: str) -> str:
    return s

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
