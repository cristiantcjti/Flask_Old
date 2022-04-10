from tkinter import N
from tkinter.messagebox import NO
from db import db
import uuid
from time import time
from default import Config as config



class ConfirmationModel(db.Model):
    __tablename__ ="confimations"

    id = db.Column(db.String(50), primary_key=True)
    expire_at = db.Column(db.Interger, nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Interger, db.ForeignKey("user.id"), nullable=False)
    user = db.relatioship("UserModel")

    def __init__(self, user_id: int, **kwargs):
        super().__init__(**kwargs)
        self.user_id = user_id
        self.id = uuid.uuid4().hex
        self.expire_at = int(time()) + config.CONFIRMATION_EXPIRATION_DELTA 
        self.confirmed = False

    @classmethod
    def find_by_id(cls, _id: str)-> "ConfirmationModel":
        return cls.query.filter_by(id=_id).first()

    @property
    def expired(self)-> bool:
        return time() > self.expire_at

    def force_to_expire(self)-> None:
        if not self.expired:
            self.expire_at = int(time())
            self.save_to_db()
        
        
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self)-> None:
        db.session.delete(self)
        db.session.commit()