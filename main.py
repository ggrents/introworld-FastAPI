from fastapi import Depends, FastAPI
from db import create_db_and_tables

app = FastAPI(title="IntroWorld")


@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()
