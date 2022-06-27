from fastapi import APIRouter
from hotel.db.db_interface import DBInterface
from hotel.db.models import DBRoom
from hotel.operations.rooms import get_all_rooms, get_room

router = APIRouter()



@router.get("/rooms")
def api_get_all_rooms():
    room_interface = DBInterface(db_class=DBRoom)
    return get_all_rooms(room_interface)


@router.get("/room/{room_id}")
def api_get_room(room_id: int):
    room_interface = DBInterface(db_class=DBRoom)
    return get_room(room_id, room_interface)
