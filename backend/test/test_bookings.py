from datetime import date
import unittest

from hotel.operations.bookings import (
    BookingCreateData,
    InvalidDateError,
    create_booking,
)
from hotel.operations.errors import UnavailableRoomError
from hotel.operations.interface import DataObject
from test.stub import DataInterfaceStub


class RoomInterface(DataInterfaceStub):
    def get_by_id(self, id: int) -> DataObject:
        return {"id": id, "number": "101", "size": 10, "price": 150_00}


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

    def create(self, data: DataObject) -> DataObject:
        booking = dict(data)
        booking["id"] = 1
        return booking


class TestBooking(unittest.TestCase):
    def test_price_one_day(self):
        booking_data = BookingCreateData(
            room_id=1, customer_id=1, from_date="2022-06-23", to_date="2022-06-24"
        )

        booking = create_booking(
            booking_data,
            room_interface=RoomInterface(),
            booking_interface=BookingInterface(),
        )

        self.assertEqual(booking["price"], 150_00)

    def test_date_error(self):
        booking_data = BookingCreateData(
            room_id=1, customer_id=1, from_date="2022-06-27", to_date="2022-06-27"
        )
        self.assertRaises(
            InvalidDateError,
            create_booking,
            booking_data,
            RoomInterface(),
            BookingInterface(),
        )
    
    def test_unavailable_room_booking(self):
        booking_data = BookingCreateData(
            room_id=1, customer_id=2, from_date="2022-06-28", to_date="2022-07-01"
        )

        self.assertRaises(
            UnavailableRoomError,
            create_booking,
            booking_data,
            RoomInterface(),
            BookingInterface(),
        )
