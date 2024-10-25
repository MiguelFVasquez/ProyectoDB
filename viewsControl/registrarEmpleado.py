from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtCore import QPropertyAnimation
from conexion import Conexion  # Importar la clase de conexión

class RegistrarEmpleado(QMainWindow):  # Hereda de QMainWindow para evitar la ventana negra
    def __init__(self, menu):
        super().__init__()  # Llama al constructor de QMainWindow
        uic.loadUi("views/registrarEmpleado.ui", self)  # Cargar el archivo UI correctamente en el mismo nivel del QMainWindow
        self.menu = menu 
        self.iniGui()

        # Predefinir los cargos en el ComboBox
        self.comboBoxCargo.addItems(["Operarios", "Administrativo", "Ejecutivo","Tesorero", "Otros"])

        # Conectar el cambio de selección en el ComboBox a una función
        self.comboBoxCargo.currentIndexChanged.connect(self.asignarSalarioPorCargo)

        # Conectar el botón para crear empleado
        self.btnCrearEmpleado.clicked.connect(self.crearEmpleado)

        # Crear una instancia de la conexión a la base de datos
        self.db = Conexion()

        # Variable para almacenar el salario
        self.salario = 0

    def iniGui(self):
        # Conectar el botón de regresar al menú
        self.btnRegresar.clicked.connect(self.regresarAlMenu)

    def regresarAlMenu(self):
        # Cierra la ventana actual y vuelve al menú principal
        self.close()
        self.menu.show()

    def asignarSalarioPorCargo(self):
        # Obtener el cargo seleccionado
        cargo = self.comboBoxCargo.currentText()

        # Asignar salario según el cargo
        if cargo == "Operarios":
            self.salario = 10000000
        elif cargo == "Administrativo":
            self.salario = 15000000
        elif cargo == "Ejecutivo":
            self.salario = 20000000
        elif cargo == "Tesorero":
            self.salario = 25000000  # Asignar un salario para el tesorero
        elif cargo == "Otros":
            self.salario = 12000000

        # Mostrar el salario asignado (puedes actualizar una etiqueta si lo deseas)
        print(f"Salario asignado: {self.salario}")

    def crearEmpleado(self):
        # Obtener los valores ingresados
        cedula = self.txtCedula.text().strip()
        nombre = self.txtNombre.text().strip()
        clave = self.txtContrasenia.text().strip()
        cargo = self.comboBoxCargo.currentText()

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

                # Consulta SQL para insertar el empleado
                query = """
                    INSERT INTO Empleados (cedula, clave, nombre, cargo, salario)
                    VALUES (?, ?, ?, ?, ?)
                """
                cursor.execute(query, (cedula, clave, nombre, cargo, self.salario))
                conexion.commit()  # Confirmar la transacción
                cursor.close()

                # Mostrar mensaje de éxito
                QMessageBox.information(self, "Éxito", "Empleado creado con éxito")
                print(f"Empleado creado con cédula: {cedula}, nombre: {nombre}, cargo: {cargo}, salario: {self.salario}")

                self.limpiarCampos()

            except Exception as e:
                conexion.rollback()  # Revertir la transacción en caso de error
                QMessageBox.critical(self, "Error", f"Error al crear el empleado: {e}")
                print(f"Error al crear el empleado: {e}")

            finally:
                self.db.close()  # Cerrar la conexión a la base de datos
        else:
            QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos")

    def limpiarCampos(self):
        # Limpiar los campos de texto
        self.txtCedula.clear()
        self.txtNombre.clear()
        self.txtContrasenia.clear()
        # Restablecer el ComboBox al primer elemento
        self.comboBoxCargo.setCurrentIndex(0)
