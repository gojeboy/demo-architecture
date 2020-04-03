from app import db


class Address(db.Model):
    __tablename__ = "address"
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(255))
    city = db.Column(db.String(255))
    province = db.Column(db.String(255))

    user_id = db.Column(db.Integer, db.ForeignKey("tbl_user.id"))
    user = db.relationship("User", back_populates="tbl_user")

    def __init__(self, street, city, province, user_id):
        self.street = street
        self.city = city
        self.province = province
        self.user_id = user_id

    def save(self):
        db.session.add(self)
        db.session.commit()
