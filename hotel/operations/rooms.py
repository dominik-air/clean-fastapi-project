from hotel.db.engine import DBSession
from hotel.db.models import DBRoom


def get_all_rooms():
    session = DBSession()
    rooms = session.query(DBRoom).all()
    return rooms


def get_room(room_id: int):
    session = DBSession()
    room = session.query(DBRoom).get(room_id)
    return room
