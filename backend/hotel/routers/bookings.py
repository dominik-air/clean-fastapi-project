import random
from fastapi import APIRouter
from hotel.db.db_interface import DBInterface
from hotel.db.models import DBBooking, DBRoom

from hotel.operations.bookings import (
    BookingCreateData,
    create_booking,
    delete_booking,
    get_all_bookings,
    get_booking,
)
from hotel.operations.errors import UnavailableRoomError
from hotel.operations.rooms import get_available_rooms

router = APIRouter()


@router.get("/bookings")
def api_get_all_bookings():
    booking_interface = DBInterface(DBBooking)
    return get_all_bookings(booking_interface)


@router.get("/booking/{booking_id}")
def api_get_booking(booking_id: int):
    booking_interface = DBInterface(DBBooking)
    return get_booking(booking_id, booking_interface)


@router.post("/booking")
def api_create_booking(data: BookingCreateData):
    booking_interface = DBInterface(DBBooking)
    room_interface = DBInterface(DBRoom)
    try:
        return create_booking(data, room_interface, booking_interface)
    except UnavailableRoomError:
        # in case the chosen room is unavailable in the given range choose a random available one
        available_rooms = get_available_rooms(
            data.from_date, data.to_date, room_interface, booking_interface
        )
        room = random.choice(available_rooms)
        data.room_id = room["id"]
        return create_booking(data, room_interface, booking_interface)


@router.delete("/booking/{booking_id}")
def api_delete_booking(booking_id: int):
    booking_interface = DBInterface(DBBooking)
    return delete_booking(booking_id, booking_interface)
