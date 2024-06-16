import mysql.connector as mysqlclient


def create_connection(host, port, user, password, database):
    try:
        return mysqlclient.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
    except mysqlclient.Error as e:
        print("error: ", e)
        return None


def close_connection(cursor, connection):
    if cursor:
        cursor.close()
        print("Cursor closed.")
    if connection:
        connection.close()
        print("Connection closed.")


def commit(connection):
    try:
        connection.commit()
        print("Commit successful.")
        return True
    except mysqlclient.Error as e:
        print("error: ", e)
        return False


def run_query(query):
    connection = create_connection('localhost', 3308, 'user', 'password', 'movie_db')
    if connection is None:
        return False

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        commit(connection)
        close_connection(cursor, connection)
        print("Query executed successfully.")
        return True
    except mysqlclient.Error as e:
        print("error: ", e)
        return False


def run_insert_query(query, values):
    connection = create_connection('localhost', 3308, 'user', 'password', 'movie_db')
    if connection is None:
        return False

    try:
        cursor = connection.cursor()
        cursor.execute(query, values)
        commit(connection)
        close_connection(cursor, connection)
        print("Query executed successfully.")
        return True
    except mysqlclient.Error as e:
        print("error: ", e)
        return False
