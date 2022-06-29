from datetime import date, timedelta
from hotel.operations.errors import InvalidDateError
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


def get_available_rooms(
    start_date: date,
    end_date: date,
    room_interface: DataInterface,
    booking_interface: DataInterface,
) -> list[DataObject]:

    if start_date > end_date:
        raise InvalidDateError("Start date cannot be later than the end date!")

    rooms = room_interface.get_all()

    # get days that we need to check
    delta = end_date - start_date
    dates = [start_date + timedelta(days=i) for i in range(delta.days + 1)]

    available_rooms = []

    for room in rooms:
        if all(
            check_room_availability(room["id"], date, booking_interface)
            for date in dates
        ):
            available_rooms.append(room)

    return available_rooms
