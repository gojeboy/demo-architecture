from app.db import DB

db =DB()

class User:
    name = ''
    surname = ''

    def __init__(self, name, surname):

        self.name = name
        self.surname = surname

    def save(self):
        str_sql ="INSERT INTO tbl_user(name,surname) values('{}', '{}')".format(self.name, self.surname)
        db.execute_sql(str_sql)

    @staticmethod
    def get_all_users():
        return db.session.query(User).all()

    def serialize(self):
        return {"name": self.name, "surname": self.surname}
