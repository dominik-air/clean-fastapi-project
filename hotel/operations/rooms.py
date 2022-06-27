from hotel.operations.interface import DataInterface, DataObject


def get_all_rooms(room_interface: DataInterface) -> list[DataObject]:
    return room_interface.get_all()


def get_room(room_id: int, room_interface: DataInterface) -> DataObject:
    return room_interface.get_by_id(room_id)
