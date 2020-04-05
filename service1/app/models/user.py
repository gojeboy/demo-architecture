from app.db import DB

db =DB()

def serialize_db_user(db_user):
        user = {
            "id":db_user[0],
            "name":db_user[1],
            "surname":db_user[2],
            "email":db_user[3],
        }

        return user

class User:
    name = ''
    surname = ''
    email =''

    def __init__(self, name, surname, email):

        self.name = name
        self.surname = surname
        self.email = email

    def save(self):
        str_sql ="INSERT INTO tbl_user(name,surname, email) values('{}', '{}', '{}')".format(self.name, self.surname, self.email)
        print(str_sql)
        try:
             db.cursor.execute(str_sql)
             db.conn.commit()
            #  db.conn.close()
            #  db.cursor.close()
        except expression as e:
            print(str(e))
       
        

    @staticmethod
    def get_user(id):
        str_sql = "SELECT * FROM tbl_user WHERE id="+id
        db.cursor.execute(str_sql)
        fetched_user = db.cursor.fetchone()
        db.conn.close()
        db.cursor.close()

        return serialize_db_user(fetched_user)

    @staticmethod
    def get_user_by_email(email):
        str_sql = "SELECT * FROM tbl_user WHERE email='{}'".format(email)
        db.cursor.execute(str_sql)
        fetched_user = db.cursor.fetchone()
        user = serialize_db_user(fetched_user)

        return user


    @staticmethod
    def get_all_users():
        str_sql = "SELECT * FROM tbl_user"
        db.cursor.execute(str_sql)
        fetched_users = db.cursor.fetchall()

        users =[]
        for fetched_user in fetched_users:
            users.append(serialize_db_user(fetched_user))

       
        return users

    def serialize(self):
        return {"name": self.name, "surname": self.surname}
