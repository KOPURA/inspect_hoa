from models.base_model import BaseModel


class HOA(BaseModel):

    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }
