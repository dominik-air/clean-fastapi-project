from fastapi import APIRouter
from hotel.operations.rooms import get_all_rooms, get_room

router = APIRouter()

# NOTE: I might want to do more stuff like authentication or sending messages on the router
# level so it's important to move operations into separate files to keep things clean


@router.get("/rooms")
def api_get_all_rooms():
    return get_all_rooms()


@router.get("/room/{room_id}")
def api_get_room(room_id: int):
    return get_room(room_id)
