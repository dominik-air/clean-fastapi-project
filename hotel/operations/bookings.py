from datetime import date
from pydantic import BaseModel

from hotel.operations.interface import DataInterface, DataObject


class InvalidDateError(Exception):
    pass


class BookingCreateData(BaseModel):
    customer_id: int
    room_id: int
    from_date: date
    to_date: date


def get_all_bookings(booking_interface: DataInterface) -> list[DataObject]:
    return booking_interface.get_all()


def get_booking(booking_id: int, booking_interface: DataInterface) -> DataObject:
    return booking_interface.get_by_id(booking_id)


def create_booking(
    data: BookingCreateData,
    room_interface: DataInterface,
    booking_interface: DataInterface,
) -> DataObject:

    room = room_interface.get_by_id(data.room_id)

    days = (data.to_date - data.from_date).days

    if days <= 0:
        raise InvalidDateError("Invalid dates.")

    booking_dict = data.dict()
    booking_dict["price"] = room["price"] * days

    return booking_interface.create(booking_dict)


def delete_booking(booking_id: int, booking_interface: DataInterface) -> DataObject:
    return booking_interface.delete(booking_id)
