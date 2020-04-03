from app import db


class User(db.Model):
    __tablename__ = "tbl_user"

    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    surname = db.Column(db.String(200))

    children = db.relationship("address")

    def __init__(self, name, surname):

        self.name = name
        self.surname = surname

    def save(self):
        db.session.add(self)
        db.session.commit()
