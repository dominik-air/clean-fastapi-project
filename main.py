from fastapi import FastAPI
from hotel.db.engine import init_db
from hotel.routers import rooms

app = FastAPI()

DB_FILE = "sqlite:///hotel.db"


@app.on_event("startup")
def startup_event():
    init_db(DB_FILE)


@app.get("/")
def get_root():
    return "The server is running."


app.include_router(rooms.router)
