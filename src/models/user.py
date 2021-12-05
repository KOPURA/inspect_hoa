from models.base_model import BaseModel


class User(BaseModel):

    def __init__(self, id, username):
        self.id = id
        self.username = username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username
        }

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username
