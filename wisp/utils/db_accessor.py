import mysql.connector.pooling
import os

DB_SETTINGS = {
    "host": "localhost",
    "user": os.environ["WISP_DB_USERNAME"],
    "port": 3306,
    "password": os.environ["WISP_DB_PASSWORD"],
    "database": "weather"
}


class MySQLPool(object):

    def __init__(self):
        self.pool = self.create_pool()

    def create_pool(self, pool_name="pool", pool_size=3):
        pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name=pool_name,
            pool_size=pool_size,
            pool_reset_session=True,
            **DB_SETTINGS)
        return pool

    def close(self, conn, cursor):
        cursor.close()
        conn.close()

    def execute(self, sql, args=None, commit=False):
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

    def get_wind_speed_measurements(self, date_start, date_end):
        if not self.pool:
            self.configure_connection()
        sql = "SELECT * FROM wind_speed_measurement WHERE date_created > %s AND date_created < %s"
        params = (date_start, date_end)

        query_result = self.pool.execute(sql, params)
        results = []
        for (record_id, wind_speed, date_created) in query_result:
            results.append({"wind_speed": float(wind_speed), "date_created": date_created})

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
        sql = "SELECT * fROM wind_gust_measurement WHERE date_created > %s AND date_created < %s"
        params = (date_start, date_end)

        query_result = self.pool.execute(sql, params)

        results = []
        for (record_id, wind_gust, date_created) in query_result:
            results.append({"wind_gust": float(wind_gust), "date_created": date_created})

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
        params = (date_start, date_end)

        query_result = self.pool.execute(sql, params)

        results = []
        for (record_id, temp, humidity, pressure, date_created) in query_result:
            results.append({"temperature": float(temp),
                            "pressure": float(pressure),
                            "humidity": float(humidity),
                            "date_created": date_created})
        return results


