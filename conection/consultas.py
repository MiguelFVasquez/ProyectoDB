from conection.conexion import obtener_conexion

def obtener_usuarios():
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Usuarios;")
            usuarios = cursor.fetchall()
            for usuario in usuarios:
                print(usuario)
            cursor.close()
        except Exception as e:
            print('Error al ejecutar la consulta:', e)
        finally:
            conexion.close()
    else:
        print("No se pudo establecer la conexión con la base de datos.")

def insertar_usuario(id_usuario, nombre_usuario, clave, nivel):
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = f"INSERT INTO Usuarios(idUsuario, nombreUsuario, clave, nivel) VALUES ('{id_usuario}', '{nombre_usuario}', '{clave}', '{nivel}');"
            cursor.execute(consulta)
            conexion.commit()
            print("Usuario insertado correctamente.")
            cursor.close()
        except Exception as e:
            print('Error al insertar el usuario:', e)
        finally:
            conexion.close()
    else:
        print("No se pudo establecer la conexión con la base de datos.")