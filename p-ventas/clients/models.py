import email
from turtle import position
import uuid

class Client:
    
    def __init__(self, name, company, email, position, uid=None) -> None:
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4()

    def to_dict(self):
        return vars(self)

    
    @staticmethod
    def schema():
        return ['name', 'company', 'email', 'position', 'uid']