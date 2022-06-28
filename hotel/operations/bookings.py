from datetime import date, timedelta
from pydantic import BaseModel
from hotel.operations.errors import InvalidDateError, UnavailableRoomError

from hotel.operations.interface import DataInterface, DataObject
from hotel.operations.rooms import check_room_availability


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

    # check if the room is available
    delta = data.to_date - data.from_date
    dates = [data.from_date + timedelta(days=i) for i in range(delta.days + 1)]
    if not all(
        check_room_availability(data.room_id, date, booking_interface) for date in dates
    ):
        raise UnavailableRoomError(
            f"Room with id: {data.room_id} is not available from {data.from_date} to {data.to_date}."
        )

    booking_dict = data.dict()
    booking_dict["price"] = room["price"] * days

    return booking_interface.create(booking_dict)


def delete_booking(booking_id: int, booking_interface: DataInterface) -> DataObject:
    return booking_interface.delete(booking_id)
