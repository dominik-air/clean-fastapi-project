from datetime import date
from hotel.db.engine import DBSession
from hotel.db.models import DBBooking, DBCustomer, DBRoom, to_dict
from pydantic import BaseModel


class InvalidDateError(Exception):
    pass


class BookingCreateData(BaseModel):
    customer_id: int
    room_id: int
    from_date: date
    to_date: date


def get_all_bookings():
    session = DBSession()
    bookings = session.query(DBBooking).all()
    return [to_dict(booking) for booking in bookings]


def get_booking(booking_id: int):
    session = DBSession()
    booking = session.query(DBBooking).get(booking_id)
    return to_dict(booking)


def create_booking(data: BookingCreateData):
    session = DBSession()

    room = session.query(DBRoom).get(data.room_id)

    days = (data.to_date - data.from_date).days

    if days <= 0:
        raise InvalidDateError("Invalid dates.")

    booking_price = room.price * days

    booking = DBBooking(**data.dict(), price=booking_price)
    session.add(booking)
    session.commit()
    return to_dict(booking)


def delete_booking(booking_id: int):
    session = DBSession()
    booking = session.query(DBBooking).get(booking_id)
    session.delete(booking)
    session.commit()
    return to_dict(booking)
