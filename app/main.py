from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Travel Ideas API")
class Trip(BaseModel):
    city: str
    days: int

TRIPS = [{"city": "Jaipur", "days": 3}, {"city": "Kochi", "days": 4}]
@app.get("/health")
def health():
    return {"status": "ok"}
@app.get("/trips")
def trips():
    return TRIPS
@app.post("/trips")
def add_trip(trip: Trip):
    item = trip.model_dump()
    TRIPS.append(item)
    return item
