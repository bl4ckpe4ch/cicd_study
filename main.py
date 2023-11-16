import sys
sys.dont_write_bytecode = True

from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
