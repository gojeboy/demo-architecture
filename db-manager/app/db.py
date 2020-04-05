from app import config


class DB:
    conn = config.get_conn()
    cursor = conn.cursor()

    def execute_sql(str_sql):
        cursor.execute(str_sql)
        conn.commit()
        cur.close()
        con.close()
