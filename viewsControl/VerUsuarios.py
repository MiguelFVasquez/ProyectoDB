from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView, QMessageBox
from conexion import Conexion

class VerUsuarios(QMainWindow):
    def __init__(self, menu):
        super().__init__()
        uic.loadUi('views/verUsuarios.ui', self)
        self.menu = menu
        self.db = Conexion()
        self.iniGui()
        self.cargarUsuarios()

    def iniGui(self):
        self.btnRegresar.clicked.connect(self.regresarAlMenu)
        self.btnActualizar.clicked.connect(self.cargarUsuarios)
        self.btnEliminar.clicked.connect(self.eliminarUsuario)  # Conectar botón de eliminar
        self.btnBuscar.clicked.connect(self.buscarPorCedula)  # Conectar botón de búsqueda
        self.tableWidgetUsuarios.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

    def regresarAlMenu(self):
        self.close()
        self.menu.show()

    def obtener_usuarios(self, cedula=None):
        """Obtiene la lista de usuarios, su cargo y sucursal de la base de datos."""
        usuarios = []
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            if cedula:
                query = """
                    SELECT 
                        e.idUsuario AS idUsuario, 
                        e.nombre AS Nombre, 
                        e.cedula AS Cedula,  
                        e.email AS Email,
                        c.NombreCargo AS Cargo, 
                        c.Salario AS Salario,
                        s.Municipio AS Sucursal
                    FROM 
                        Empleados e
                    JOIN 
                        Cargo c ON e.idCargo = c.idCargo
                    JOIN 
                        Sucursales s ON e.idSucursal = s.idSucursal
                    WHERE 
                        e.idEstado = 1 AND e.cedula = ?  -- Filtro por cédula
                """
                cursor.execute(query, (cedula,))
            else:
                query = """
                    SELECT 
                        e.idUsuario AS idUsuario, 
                        e.nombre AS Nombre, 
                        e.cedula AS Cedula,  
                        e.email AS Email,
                        c.NombreCargo AS Cargo, 
                        c.Salario AS Salario,
                        s.Municipio AS Sucursal
                    FROM 
                        Empleados e
                    JOIN 
                        Cargo c ON e.idCargo = c.idCargo
                    JOIN 
                        Sucursales s ON e.idSucursal = s.idSucursal
                    WHERE 
                        e.idEstado = 1  -- Solo usuarios con estado ACTIVO
                """
                cursor.execute(query)

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
        usuarios = self.obtener_usuarios()
        for row_number, usuario in enumerate(usuarios):
            self.tableWidgetUsuarios.insertRow(row_number)
            for column_number, data in enumerate(usuario):
                item = QTableWidgetItem(str(data))
                self.tableWidgetUsuarios.setItem(row_number, column_number, item)

    def buscarPorCedula(self):
        """Filtra los usuarios por cédula ingresada en la barra de búsqueda."""
        cedula = self.txtCedula.text().strip()
        if not cedula:
            QMessageBox.warning(self, "Advertencia", "Ingrese una cédula para buscar.")
            return

        usuarios = self.obtener_usuarios(cedula=cedula)
        if not usuarios:
            QMessageBox.information(self, "Resultado", f"No se encontró ningún usuario con la cédula {cedula}.")
            return

        self.tableWidgetUsuarios.setRowCount(0)  # Limpia la tabla
        for row_number, usuario in enumerate(usuarios):
            self.tableWidgetUsuarios.insertRow(row_number)
            for column_number, data in enumerate(usuario):
                item = QTableWidgetItem(str(data))
                self.tableWidgetUsuarios.setItem(row_number, column_number, item)

    def eliminarUsuario(self):
        """Cambia el estado de un usuario seleccionado a INACTIVO."""
        selected_row = self.tableWidgetUsuarios.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Advertencia", "Por favor, seleccione un usuario de la tabla.")
            return

        idUsuario = self.tableWidgetUsuarios.item(selected_row, 0).text()
        nombreUsuario = self.tableWidgetUsuarios.item(selected_row, 1).text()

        respuesta = QMessageBox.question(
            self,
            "Confirmación",
            f"¿Está seguro de que desea desactivar al usuario '{nombreUsuario}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if respuesta == QMessageBox.StandardButton.Yes:
            try:
                conn = self.db.connect()
                if conn is None:
                    QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos.")
                    return

                cursor = conn.cursor()
                cursor.execute("UPDATE Empleados SET idEstado = 2 WHERE idUsuario = ?", (idUsuario,))
                conn.commit()

                QMessageBox.information(self, "Éxito", f"El usuario '{nombreUsuario}' ha sido desactivado.")
                self.cargarUsuarios()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo desactivar al usuario. Error: {e}")
            finally:
                if conn is not None:
                    self.db.close()
