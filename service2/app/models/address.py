from app.db import DB
import psycopg2 as pg


db = DB()

class Address:

    
    street=''
    city=''
    province=''
    user_id=''

    def __init__(self, street, city, province, user_id):
        self.street = street
        self.city = city
        self.province = province
        self.user_id = user_id

    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()

    # @staticmethod
    # def get_all_address():
    #     return db.session.query(Address).all()

    def serialize(self):
        return {
            "street": self.street,
            "city": self.city,
            "province": self.province,
            "user_id": self.user_id,
        }

    def save_address_to_db(self):
        str_sql = "INSERT INTO address(street, city,province, user_id) VALUES('{}','{}','{}','{}')".format(
            self.street, self.city, self.province, self.user_id
        )

        print(str_sql)

        try:
            db.execute_sql(str_sql)
        except Exception as e :
            print("Something went wrong ")
            print(e.message)
