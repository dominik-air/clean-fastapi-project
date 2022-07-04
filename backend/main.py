from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from hotel.db.engine import init_db
from hotel.routers import bookings, customers, rooms

app = FastAPI()

DB_FILE = "sqlite:///db/hotel.db"

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    init_db(DB_FILE)


@app.get("/")
def get_root():
    return "The server is running."


app.include_router(rooms.router)
app.include_router(customers.router)
app.include_router(bookings.router)
