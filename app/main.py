import logging
import sys
from pathlib import Path

from fastapi import FastAPI
from fastapi import status
from models import Location, Speed

from settings import fun, LOG_DIR


logger = logging.getLogger()

logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
log_format = logging.Formatter(
    "%(asctime)s %(levelname)-8s %(name)-8s %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S'
)
console_handler.setFormatter(log_format)
logger.addHandler(console_handler)

Path.mkdir(LOG_DIR, exist_ok=True)
file_logger = logging.FileHandler(LOG_DIR / "app.log")
file_logger.setFormatter(log_format)
logger.addHandler(file_logger)


app = FastAPI()


@app.get("/health", status_code=status.HTTP_200_OK)
async def get_health():
    logger.info("Health Check Requested")
    fun()
    return {"message": "ok"}


@app.post("/location/", status_code=status.HTTP_201_CREATED)
async def post_location(location: Location):
    return {"message": "created"}


@app.post("/speed/", status_code=status.HTTP_201_CREATED)
async def post_speed(speed: Speed):
    return {"message": "created"}
