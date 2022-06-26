from hotel.db.engine import DBSession
from hotel.db.models import DBRoom, to_dict


def get_all_rooms():
    session = DBSession()
    rooms = session.query(DBRoom).all()
    return [to_dict(room) for room in rooms]


def get_room(room_id: int):
    session = DBSession()
    room = session.query(DBRoom).get(room_id)
    return to_dict(room)
