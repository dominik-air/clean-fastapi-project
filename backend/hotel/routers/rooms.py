from datetime import date
from fastapi import APIRouter
from hotel.db.db_interface import DBInterface
from hotel.db.models import DBBooking, DBRoom
from hotel.operations.rooms import (
    check_room_availability,
    get_all_rooms,
    get_available_rooms,
    get_room,
)


router = APIRouter()


@router.get("/rooms")
def api_get_all_rooms():
    room_interface = DBInterface(db_class=DBRoom)
    return get_all_rooms(room_interface)


@router.get("/room/{room_id}")
def api_get_room(room_id: int):
    room_interface = DBInterface(db_class=DBRoom)
    return get_room(room_id, room_interface)


@router.get("/available/room/{room_id}")
def api_check_room_availability(room_id: int, on_date: date):
    booking_interface = DBInterface(db_class=DBBooking)
    return check_room_availability(room_id, on_date, booking_interface)


@router.get("/available/rooms")
def api_check_available_rooms(start_date: date, end_date: date):
    return get_available_rooms(
        start_date,
        end_date,
        room_interface=DBInterface(db_class=DBRoom),
        booking_interface=DBInterface(db_class=DBBooking),
    )
