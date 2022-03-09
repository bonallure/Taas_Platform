import mysql.connector
import null


def connect_to_database():
    # Try/except block to validate connection
    try:
        db = mysql.connector.connect(user='developer', password='Team11_developer', host='localhost',
                                     database='team11_demand')
    except Exception as e:
        raise Exception(e)

    db = mysql.connector.connect(user='developer', password='Team11_developer', host='localhost',
                                 database='team11_demand')
    return db


class DatabaseUtil:
    def __init__(self):
        self.connection = connect_to_database()
        if self.connection.is_connected():
            database_info = self.connection.get_server_info()
            print("NOW CONNECTED TO MYSQL SERVER v", database_info)
            self.cursor = self.connection.cursor()
            print("You are connected to the database")
        else:
            raise Exception('You are not connected to the database')

    def insert_user(self, user):
        assert user != {}, 'user cannot be empty'
        sql = """INSERT INTO TaasUser (email, FName, LName, DOB, username, password) VALUES (%s,%s,%s,%s,
                %s,%s) """
        print(sql)
        val = (user['email'], user['FName'], user['LName'], user['DOB'], user['username'], user['password'])

        self.cursor.execute(sql, val)
        self.connection.commit()
        print(self.cursor.rowcount, "was inserted")

    def insert_order(self, order):
        sql = "INSERT INTO Orders (order_id, price, date_created, date_processed, date_fulfilled, service_type," \
              " address, is_confirmed, is_complete, is_paid, dispatch_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s)"
        location = order["geolocation"]
        val = (order["order_id"], order["price"], order["date_created"], order["date_processed"],
               order["date_fulfilled"], order["service_type"], order['address'], order["is_confirmed"],
               order["is_complete"], order["is_paid"], order["dispatch_id"])

        self.cursor.executemany(sql, val)
        self.connection.commit()
        print(self.cursor.rowcount, "was inserted")

    def insert_vehicle(self, vehicle):
        sql = "INSERT INTO Vehicle (vin, odometer, speed, route, isEquipped, location_longitude, " \
              "location_latitude, make, model, trip_time) VALUES (%s, %s) "
        location = vehicle["geolocation"]
        val = (vehicle["plate_num"], vehicle["odometer"], vehicle["speed"], vehicle["route"],
               vehicle["is_equipped"], location[0], location[1], vehicle["make"], vehicle["model"],
               vehicle["tripTime"])
        print(sql)
        self.cursor.executemany(sql, val)
        self.commit()
        print(self.cursor.rowcount, "was inserted")

    def update_vehicle_location(self, vin, location):
        sql = "UPDATE Vehicle set longitude =%s, latitude =%s where plate_num =%s"
        longitude = location[0]
        latitude = location[1]
        self.cursor.executemany(sql, (longitude, latitude, vin))
        self.connection.commit()
        print(self.cursor.rowcount, "was inserted")

    def insert_dispatch(self, dispatch):
        sql = "INSERT INTO Dispatch (dispatch_id, time_of_reception, time_of_completion, " \
              "processing_time, origin_longitude, origin_latitude, destination_longitude, destination_latitude, " \
              "is_dispatched, eta, duration, distance, order_id, plate_num) VALUES (%s, %s, %s," \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        val = (dispatch["dispatch_id"], dispatch["time_of_reception"], dispatch["time_of_completion"],
               dispatch["processing_time"], dispatch["origin_longitude"], dispatch["origin_latitude"],
               dispatch["destination_longitude"], dispatch["destination_latitude"], dispatch["dispatched"],
               dispatch["eta"], dispatch["duration"], dispatch["distance"], dispatch["order_id"],
               dispatch["plate_num"])
        print(sql)
        self.cursor.executemany(sql, val)
        self.commit()
        print(self.cursor.rowcount, "was inserted")

    def read_dispatch(self, order_id):
        select_statement = "SELECT * FROM Dispatches WHERE order_id=%s"
        try:
            self.cursor.execute(select_statement, order_id)
        except Exception as e:
            print(e)
        finally:
            result = self.cursor.fetchone()
            return result

    def read_dispatches(self):
        select_statement = "SELECT * FROM Dispatches"
        try:
            self.cursor.execute(select_statement)
        except Exception as e:
            print(e)
        finally:
            result = self.cursor.fetchone()
            return result

    def read_user(self, user_name, password):
        select_statement = "SELECT * FROM TaasUser WHERE userName=%s AND password=%s"
        user = {}
        user_tuple = ()
        try:
            self.cursor.execute(select_statement, (user_name, password))
        except Exception as e:
            print(e)
        finally:
            result = self.cursor.fetchone()
            user_tuple = result

        assert user_tuple != (), 'user not found'
        user['email'] = user_tuple[0]
        user['FName'] = user_tuple[1]
        user['LName'] = user_tuple[2]
        user['DOB'] = user_tuple[3]
        user['userName'] = user_tuple[4]
        user['password'] = user_tuple[4]

        return user

    def read_users(self):
        select_statement = "SELECT * FROM TaasUser"
        try:
            self.cursor.execute(select_statement)
        except Exception as e:
            print(e)
        finally:
            result = self.cursor.fetchone()
            return result

    def read_order(self, user_id):
        select_statement = "SELECT * FROM Orders WHERE user_id=%s"
        try:
            self.cursor.execute(select_statement, user_id)
        except Exception as e:
            print(e)
        finally:
            result = self.cursor.fetchone()
            return result

    def read_orders(self):
        select_statement = "SELECT * FROM Orders"
        try:
            self.cursor.execute(select_statement)
        except Exception as e:
            print(e)
        finally:
            result = self.cursor.fetchone()
            return result

    def read_vehicle(self, vin):
        select_statement = "SELECT * FROM Vehicles WHERE vin=%s"
        try:
            self.cursor.execute(select_statement, vin)
        except Exception as e:
            print(e)
        finally:
            result = self.cursor.fetchone()
            return result

    def read_vehicles(self):
        select_statement = "SELECT * FROM Vehicles"
        try:
            self.cursor.execute(select_statement)
        except Exception as e:
            print(e)
        finally:
            result = self.cursor.fetchone()
            return result

    def close_connection(self):
        self.connection.close()
        print("MySQL connection is closed")

    def read_vehicle_location(self, vin):
        select_statement = "SELECT longitude, latitude FROM Vehicles WHERE vin=%s"
        try:
            self.cursor.execute(select_statement, vin)
        except Exception as e:
            print(e)
        finally:
            result = self.cursor.fetchone()
            return result

    def get_available_vehicle(self):
        select_statement = "SELECT * FROM Vehicles WHERE en_route=False"
        try:
            self.cursor.execute(select_statement)
        except Exception as e:
            print(e)
        finally:
            result = self.cursor.fetchone()
            # make sure we only send 1 vehicle back
            return result
