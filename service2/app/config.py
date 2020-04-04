import os
import psycopg2

# postgres_db 
# postgres_user 
# postgres_password
# postgres_host 


if "POSTGRES_DB_USER" in os.environ:
    postgres_user = os.environ["POSTGRES_DB_USER"]
else:
        postgres_user= "admin"


if "POSTGRES_DB" in os.environ:
    postgres_db = os.environ["POSTGRES_DB"]
else:
        postgres_db= "test_db"

if "POSTGRES_DB_PASSWORD" in os.environ:
    postgres_password = os.environ["POSTGRES_DB_PASSWORD"]
else:
        postgres_password= "password"


if "POSTGRES_HOST" in os.environ:
    postgres_host = os.environ["POSTGRES_HOST"]
else:
        postgres_host= "localhost"



class Config:
   
    def config_progress():
        connection_str = (
            "postgresql+psycopg2://" + role + ":" + password + "@" + host + "/" + db
        )

        return connection_str

    @staticmethod
    def get_conn():
        conn = psycopg2.connect(
            "dbname="
            + postgres_db
            + " user="
            + postgres_user
            + " host="
            + postgres_host
            + " password="
            + postgres_password
            + ""
        )

        return conn
