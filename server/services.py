from sqlalchemy.orm import Session

from models import User


async def get_user_by_id(session: Session, uid: int) -> User:
    user = session.query(User).get(uid)
    session.close()
    return user

async def get_user_by_login(session: Session,login: str) -> User:
    user = session.query(User).filter_by(login=login).first()
    session.close()
    return user