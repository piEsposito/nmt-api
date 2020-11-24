from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse

import logging
import time
import os

from lib.translator import Translator
from lib.logger import set_logger

from dotenv import load_dotenv
load_dotenv()

set_logger()

setup_start = time.time()
app = FastAPI()

API_TOKEN = os.getenv("TOKEN")
mname = os.getenv("MODEL_NAME")

translator = Translator(mname)

setup_end = time.time()
setup_time = setup_end - setup_start

logging.info(f"Setup took {setup_time:.3f} seconds")
logging.info(f"Started NMT-API with model {mname}")


async def authenticate(request: Request):
    global API_TOKEN
    token = request.headers.get("TOKEN")
    if (token is None) or (token != API_TOKEN):
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {}


async def validate_json(request: Request):
    # makes the requests keys to keep the same order as the model

    try:
        body = await request.json()
    except:
        raise HTTPException(status_code=400, detail="Bad request")

    keys = ["text"]
    for key in keys:
        if body.get(key) is None:
            raise HTTPException(status_code=400, detail="Bad request")

    return body


@app.post("/translate")
async def root(token: dict = Depends(authenticate), features: dict = Depends(validate_json)):
    text_to_translate = features.get("text")
    word_nbr = text_to_translate.split(" ").__len__()

    translation = translator(text_to_translate)
    translated_text = translation["translation"]
    elapsed_time = translation["elapsed_time"]

    logging.info(f"Performed translation on {word_nbr} words in {elapsed_time:.4f} seconds")
    return JSONResponse(
        status_code=200,
        content={"translation": translated_text,
                 "compute_time": elapsed_time,
                 "words_to_translate_nbr": word_nbr,
                 "translated_word_nbr": translated_text.split(" ").__len__()}
    )


@app.get("/")
async def health_check():
    return JSONResponse(
        status_code=200,
        content={"message": "alive and running!"}
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": str(exc.detail)}
    )


@app.exception_handler(Exception)
async def handle_exception(*args):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal error"}
    )
