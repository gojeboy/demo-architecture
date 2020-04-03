from app import db, app


class User(db.Model):
    __tablename__ = "tbl_user"

    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    surname = db.Column(db.String(200))

    # addresses = db.relationship("address")

    def __init__(self, name, surname):

        self.name = name
        self.surname = surname

    def save(self):
        print(app.config)
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_users():
        return db.session.query(User).all()

    def serialize(self):
        return {"id": self.id, "name": self.name, "surname": self.surname}
