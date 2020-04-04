from app.config import Config

conn = Config.get_conn()
cursor = conn.cursor()

class DB:

    def execute_sql(self,str_sql):
        print(str_sql)
        cursor.execute(str_sql)
        conn.commit()
        conn.close()
        conn.close()
       
