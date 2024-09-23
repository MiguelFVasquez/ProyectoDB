import pymssql
import pyodbc
# conexion.py
import pyodbc

def obtener_conexion():
    server = 'DESKTOP-ICU1JM4\\SQLEXPRESS'
    bd = 'db_banco'
    username = 'juan'
    password = 'juanmiguel'

    try:
        conexion = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL server}; SERVER=' + server +
            ';DATABASE=' + bd +
            ';UID=' + username +
            ';PWD=' + password
        )
        print('Conexión exitosa')
        return conexion
    except Exception as e:
        print('Error al intentar conectarse:', e)
        return None

""""
1. Usuarios
2. Prestamo
    - DetallePrestamo
    - Solicitud
3. Ciudad
4. Sucursal
5. PagoCuotas   
"""