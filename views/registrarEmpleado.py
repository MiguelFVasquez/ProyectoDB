from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from conexion import Conexion  # Importar la clase de conexión

class RegistrarEmpleado(QMainWindow):
    def __init__(self):
        super(RegistrarEmpleado, self).__init__()
        uic.loadUi("views/registrarEmpleado.ui", self)

        # Predefinir los cargos en el ComboBox
        self.comboBoxCargo.addItems(["Operarios", "Administrativo", "Ejecutivo", "Otros"])

        # Conectar el botón para crear empleado
        self.btnCrearEmpleado.clicked.connect(self.crearEmpleado)

        # Crear una instancia de la conexión a la base de datos
        self.db = Conexion()

    def crearEmpleado(self):
        # Obtener los valores ingresados
        cedula = self.txtCedula.text().strip()
        nombre = self.txtNombre.text().strip()
        clave = self.txtContrasenia.text().strip()
        cargo = self.comboBoxCargo.currentText()
        salario= 1500000

        # Validaciones simples
        if not cedula:
            QMessageBox.warning(self, "Advertencia", "El campo de cédula no puede estar vacío")
            return
        elif not nombre:
            QMessageBox.warning(self, "Advertencia", "El campo de nombre no puede estar vacío")
            return
        elif not clave:
            QMessageBox.warning(self, "Advertencia", "El campo de contraseña no puede estar vacío")
            return

        # Conectar a la base de datos e insertar el empleado
        conexion = self.db.connect()
        if conexion:
            try:
                cursor = conexion.cursor()

                # Consulta SQL para insertar el empleado (asumiendo que el ID es auto-incremental)
                query = """
                    INSERT INTO Empleados (cedula,clave,nombre,cargo,salario)
                    VALUES (?, ?, ?, ?, ?)
                """
                cursor.execute(query, (cedula,clave,nombre,cargo,salario))
                conexion.commit()  # Confirmar la transacción
                cursor.close()

                # Mostrar mensaje de éxito
                QMessageBox.information(self, "Éxito", "Empleado creado con éxito")
                print(f"Empleado creado con cédula: {cedula}, nombre: {nombre}, cargo: {cargo}")

            except Exception as e:
                conexion.rollback()  # Revertir la transacción en caso de error
                QMessageBox.critical(self, "Error", f"Error al crear el empleado: {e}")
                print(f"Error al crear el empleado: {e}")

            finally:
                self.db.close()  # Cerrar la conexión a la base de datos
        else:
            QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos")
