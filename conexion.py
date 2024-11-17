import pyodbc

class Conexion:
    def __init__(self):
        # self.server = 'DESKTOP-ICU1JM4\\SQLEXPRESS'
        # self.bd = 'db_data'
        # self.username = 'juan'
        # self.password = 'juanmiguel'
        self.conexion = None
        self.server = 'DARKDEV\SQLEXPRESS'
        self.bd = 'db_data'
        self.username = 'sa'
        self.password = 'camilo'

    def connect(self):
        try:
            self.conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER=' + self.server +
                                           ';DATABASE=' + self.bd + ';UID=' + self.username + ';PWD=' + self.password)
            #print('Conexión exitosa')
            return self.conexion
        except Exception as e:
            print(f"Error al conectarse a la base de datos: {e}")
            return None

    def close(self):
        if self.conexion is not None:
            try:
                self.conexion.close()
                #print("Conexión cerrada correctamente.")
            except pyodbc.ProgrammingError as e:
                print(f"La conexión ya estaba cerrada o no válida: {e}")
            finally:
                self.conexion = None 

