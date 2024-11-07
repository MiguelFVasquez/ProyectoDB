from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget, QAbstractItemView
from conexion import Conexion 

class VerUsuarios(QMainWindow):
    def __init__(self,menu):
        super().__init__()
        uic.loadUi('views/verUsuarios.ui', self)
        self.menu = menu
        self.db = Conexion()  
        self.iniGui()
        self.cargarUsuarios()
    
    def iniGui(self):
        self.btnRegresar.clicked.connect(self.regresarAlMenu)
        self.btnActualizar.clicked.connect(self.cargarUsuarios)
        self.tableWidgetUsuarios.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers) 

    def regresarAlMenu(self):
        self.close()
        self.menu.show()

    def obtener_usuarios(self):
        """Obtiene la lista de usuarios, su cargo y sucursal de la base de datos."""
        usuarios = []
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            # Consulta que une las tablas de Usuarios, Cargos y Sucursales
            cursor.execute("""
                SELECT 
                    e.idUsuario AS idUsuario, 
                    e.nombre AS Nombre, 
                    e.cedula AS cedula,  
                    e.email AS email,
                    c.NombreCargo AS Cargo,  -- Nombre del cargo del usuario
                    c.Salario AS Salario,
                    s.Municipio AS Sucursal  -- Nombre de la sucursal a la que pertenece el usuario
                FROM 
                    Empleados e
                JOIN 
                    Cargo c ON e.idCargo = c.idCargo  -- Relaciona con la tabla Cargos
                JOIN 
                    Sucursales s ON e.idSucursal = s.idSucursal  -- Relaciona con la tabla Sucursales
            """)
            rows = cursor.fetchall()
            for row in rows:
                usuarios.append(row)
            return usuarios
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            return []
        finally:
            self.db.close()

    def cargarUsuarios(self):
        """Carga los usuarios en la tabla."""
        self.tableWidgetUsuarios.setRowCount(0)  # Limpia la tabla
        usuarios = self.obtener_usuarios()  # Llama al método para obtener los usuarios

        for row_number, usuario in enumerate(usuarios):
            self.tableWidgetUsuarios.insertRow(row_number)  # Inserta una nueva fila en la tabla
            for column_number, data in enumerate(usuario):
                item = QTableWidgetItem(str(data))  # Coloca los datos de cada usuario en las celdas correspondientes
                self.tableWidgetUsuarios.setItem(row_number, column_number, item)