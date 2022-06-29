import unittest
from datetime import date
from hotel.operations.bookings import InvalidDateError
from hotel.operations.interface import DataObject
from hotel.operations.rooms import check_room_availability, get_available_rooms
from test.stub import DataInterfaceStub


class BookingInterface(DataInterfaceStub):
    def get_all(self) -> list[DataObject]:
        return [
            {
                "id": 1,
                "from_date": date(2022, 6, 27),
                "to_date": date(2022, 6, 30),
                "price": 3000_00,
                "customer_id": 1,
                "room_id": 1,
            }
        ]


class RoomInterface(DataInterfaceStub):
    def get_all(self) -> list[DataObject]:
        return [
            {"id": 1, "number": "101", "size": 10, "price": 150_00},
            {"id": 2, "number": "102", "size": 10, "price": 150_00},
            {"id": 3, "number": "103", "size": 10, "price": 150_00},
        ]


class TestRooms(unittest.TestCase):
    def test_available_room(self):
        result = check_room_availability(
            room_id=1, on_date=date(2022, 6, 23), booking_interface=BookingInterface()
        )

        self.assertTrue(result)

    def test_unavailable_room(self):
        result = check_room_availability(
            room_id=1, on_date=date(2022, 6, 28), booking_interface=BookingInterface()
        )

        self.assertFalse(result)

    def test_rooms_available_in_date_range(self):
        result = get_available_rooms(
            start_date=date(2022, 6, 24),
            end_date=date(2022, 6, 28),
            room_interface=RoomInterface(),
            booking_interface=BookingInterface(),
        )

        self.assertEqual(len(result), 2)

    def test_invalid_date_range(self):
        self.assertRaises(
            InvalidDateError,
            get_available_rooms,
            date(2022, 6, 28),
            date(2022, 6, 24),
            RoomInterface(),
            BookingInterface(),
        )
