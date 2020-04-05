import os

postgres_db = "POSTGRES_DB"
postgres_user = "POSTGRES_DB_USER"
postgres_password = "POSTGRES_DB_PASSWORD"
postgres_host = "POSTGRES_HOST"



    
if "POSTGRES_DB_USER" in os.environ:
    postgres_user= os.environ["POSTGRES_DB_USER"]
else:
    postgres_user ="admin"




if "POSTGRES_DB_PASSWORD" in os.environ:
    postgres_password = os.environ["POSTGRES_DB_PASSWORD"]
else:
    postgres_password = "password"



if "POSTGRES_DB" in os.environ:
    postgres_db= os.environ["POSTGRES_DB"]
else:
    postgres_db= "test_db"



if "POSTGRES_HOST" in os.environ:
    postgres_host= os.environ["POSTGRES_HOST"]
else:
    postgres_host= "localhost"


class Config:


    @staticmethod
    def config_progress():

        connection_str = "postgresql+psycopg2://" + postgres_user + ":" + postgres_password + "@" + postgres_host + "/" + postgres_db
        
    
        return connection_str
