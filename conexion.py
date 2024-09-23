import pymssql
import pyodbc

server = 'DESKTOP-ICU1JM4\SQLEXPRESS'
bd = 'db_banco'
username= 'juan'
password= 'juanmiguel'

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+server+';DATABASE='
                              + bd+';UID='+username+';PWD='+password)
    print('Conexión exitosa')

except:
    print('erro al intentar conectarse')    

#Consulta a la base de datos

cursor = conexion.cursor()
cursor.execute("SELECT * FROM Usuarios;")
#cursor.execute("insert into Usuarios(idUsuario,nombreUsuario,clave,nivel) values ('4','Miguel','4444','Operario');")

#FORMA #2

usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario) #Podemos usar print(usuario[1]) para ver solo el campo del nombre y asi con el resto de atributos

cursor.commit()
cursor.close()
conexion.close()

""""
1. Usuarios
2. Prestamo
    - DetallePrestamo
    - Solicitud
3. Ciudad
4. Sucursal
5. PagoCuotas   

"""