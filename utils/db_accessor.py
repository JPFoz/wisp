import mysql.connector.pooling

DB_SETTINGS = {
    "host": "localhost",
    "user": "pi",
    "port": 3306,
    "password": "SecRetPI",
    "database": "weather"
}


class MySQLPool(object):

    def __init__(self):
        self.pool = self.create_pool()

    def create_pool(self, pool_name="mypool", pool_size=3):
        """
        Create a connection pool, after created, the request of connecting
        MySQL could get a connection from this pool instead of request to
        create a connection.
        :param pool_name: the name of pool, default is "mypool"
        :param pool_size: the size of pool, default is 3
        :return: connection pool
        """
        pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name=pool_name,
            pool_size=pool_size,
            pool_reset_session=True,
            **DB_SETTINGS)
        return pool

    def close(self, conn, cursor):
        """
        A method used to close connection of mysql.
        :param conn:
        :param cursor:
        :return:
        """
        cursor.close()
        conn.close()

    def execute(self, sql, args=None, commit=False):
        """
        Execute a sql, it could be with args and with out args. The usage is
        similar with execute() function in module pymysql.
        :param sql: sql clause
        :param args: args need by sql clause
        :param commit: whether to commit
        :return: if commit, return None, else, return result
        """
        # get connection form connection pool instead of create one.
        conn = self.pool.get_connection()
        cursor = conn.cursor()
        if args:
            cursor.execute(sql, args)
        else:
            cursor.execute(sql)
        if commit is True:
            conn.commit()
            self.close(conn, cursor)
            return None
        else:
            res = cursor.fetchall()
            self.close(conn, cursor)
            return res


class DbAccessor(object):

    pool = None

    def configure_connection(self):
        self.pool = MySQLPool()

    def get_wind_speed_data(self, date_start, date_end):
        if not self.pool:
            self.configure_connection()
        print(date_start)
        print(date_end)
        sql = "SELECT * FROM wind_speed_measurement WHERE date_created > %s AND date_created < %s"
        params = (date_end, date_start)

        query_result = self.pool.execute(sql, params)
        print(sql.format(params))
        print(query_result)
        results = []
        for (record_id, wind_speed, date_created) in query_result:
            results.append({"wind_speed": wind_speed, "date_created": date_created})

        return results

    def insert_wind_speed_data(self, wind_speed):
        if not self.pool:
            self.configure_connection()

        sql = "INSERT INTO wind_speed_measurement (`wind_speed`,`date_created`) VALUES(%s, NOW())"
        params = (round(float(wind_speed), 2),)
        self.pool.execute(sql, params, True)

    def get_wind_gust_measurement(self, date_start, date_end):
        if not self.pool:
            self.configure_connection()
        sql = "SELECT * fROM wind_guest_measurement WHERE date_created > %s AND date_created < %s"
        params = (date_start, date_end)

        query_result = self.pool.execute(sql, params)

        results = []
        for (record_id, wind_gust, date_created) in query_result:
            results.append({"wind_gust": wind_gust, "date_created": date_created})

        return results

    def insert_wind_gust_data(self, wind_gust):
        if not self.pool:
            self.configure_connection()

        sql = "INSERT INTO wind_gust_measurement (`wind_gust`,`date_created`) VALUES(%s, NOW())"
        params = (round(float(wind_gust), 2),)
        self.pool.execute(sql, params, True)

    def insert_passive_measurement(self, temp, humidity, pressure):
        if not self.pool:
            self.configure_connection()

        sql = "INSERT INTO passive_measurement (`temperature`, `humidity`, `pressure`,`date_created`) VALUES(%s,%s,%s,NOW())"
        params = (round(float(temp),2), round(float(humidity),2), round(float(pressure),2))

        self.pool.execute(sql, params, True)

    def get_passive_measurement_data(self, date_start, date_end):
        if not self.pool:
            self.configure_connection()
        sql = "SELECT * FROM passive_measurement WHERE date_created > %s AND date_created < %s"
        params = (date_end, date_start)

        query_result = self.pool.execute(sql, params)

        results = []
        for (record_id, temp, humidity, pressure, date_created) in query_result:
            results.append({"temperature": temp,
                            "pressure": pressure,
                            "humidity": humidity,
                            "date_created": date_created})


