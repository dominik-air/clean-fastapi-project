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
def api_create_booking(customer: BookingCreateData):
    booking_interface = DBInterface(DBBooking)
    room_interface = DBInterface(DBRoom)
    return create_booking(customer, room_interface, booking_interface)


@router.delete("/booking/{booking_id}")
def api_delete_booking(booking_id: int):
    booking_interface = DBInterface(DBBooking)
    return delete_booking(booking_id, booking_interface)
