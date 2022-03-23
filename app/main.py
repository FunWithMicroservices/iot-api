from fastapi import FastAPI
from fastapi import status
from models import Location, Speed


app = FastAPI()


@app.get("/health", status_code=status.HTTP_200_OK)
async def get_health():
    return {"message": "ok"}


@app.post("/location/", status_code=status.HTTP_201_CREATED)
async def post_location(location: Location):
    return {"message": "created"}


@app.post("/speed/", status_code=status.HTTP_201_CREATED)
async def post_speed(speed: Speed):
    return {"message": "created"}
