from datetime import date
from hotel.operations.interface import DataInterface, DataObject


def get_all_rooms(room_interface: DataInterface) -> list[DataObject]:
    return room_interface.get_all()


def get_room(room_id: int, room_interface: DataInterface) -> DataObject:
    return room_interface.get_by_id(room_id)


def check_room_availability(
    room_id: int,
    on_date: date,
    booking_interface: DataInterface,
) -> bool:

    bookings = booking_interface.get_all()

    for booking in bookings:
        if (
            booking["room_id"] == room_id
            and booking["from_date"] <= on_date <= booking["to_date"]
        ):
            return False
    return True
