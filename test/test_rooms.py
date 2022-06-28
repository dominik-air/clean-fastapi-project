import unittest
from datetime import date
from hotel.operations.interface import DataObject
from hotel.operations.rooms import check_room_availability
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
