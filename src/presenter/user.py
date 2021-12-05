from models.user import User
from typing import List
from repository import user


def get_users() -> List[User]:
    json_users = user.get_users()
    return map(lambda x: User(x.get("id"), x.get("username")), json_users)


def get_user(user_id) -> User:
    return next(filter(lambda x: x.get_id() == int(user_id), get_users()), None)


def add_user(user_name):
    user_id = len(user.get_users()) + 1
    new_user = User(user_id, user_name)
    user.add_user(new_user)
