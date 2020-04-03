import os

postgres_db = "POSTGRES_DB"
postgres_user = "POSTGRES_DB_USER"
postgres_password = "POSTGRES_DB_PASSWORD"
postgres_host = "POSTGRES_HOST"


def get_role():
    
    if postgres_user in os.environ:
        return os.environ[postgres_user]
    else:
        return "admin"


def get_password():

    if postgres_password in os.environ:
        return os.environ[postgres_password]
    else:
        return "password"


def get_db():
    if postgres_db in os.environ:
        return os.environ[postgres_db]
    else:
        return "test_db"


def get_host():
    if postgres_host in os.environ:
        return os.environ[postgres_host]
    else:
        return "localhost"


def config_progress():

    role = get_role()
    password = get_password()
    db = get_db()
    host = get_host()

    connection_str = (
        "postgresql+psycopg2://" + role + ":" + password + "@" + host + "/" + db
    )

    print(connection_str)
   
    return connection_str
