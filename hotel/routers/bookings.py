from fastapi import APIRouter

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
    return get_all_bookings()


@router.get("/booking/{booking_id}")
def api_get_booking(booking_id: int):
    return get_booking(booking_id)


@router.post("/booking")
def api_create_booking(customer: BookingCreateData):
    return create_booking(customer)


@router.delete("/booking/{booking_id}")
def api_delete_booking(booking_id: int):
    return delete_booking(booking_id)
