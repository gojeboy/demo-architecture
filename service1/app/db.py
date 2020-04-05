from app.config import Config

import psycopg2

# conn = Config().get_conn()

class DB:
  conn = Config().get_conn()
  cursor = conn.cursor()

  


  def execute_sql(self, str_sql):
    try:
      res =self.cursor.execute(str_sql)

      print("fect_return return ",fect_return)
      commit = self.conn.commit()
      print("commit return ",commit)
      self.cursor.close()
      self.conn.close()
    except Exception as e:
      print(str(e))
    
