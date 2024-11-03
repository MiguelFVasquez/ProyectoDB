from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from conexion import Conexion  # Importar la clase de conexión

class RegistrarEmpleado(QMainWindow):
    def __init__(self, menu):
        super().__init__()
        uic.loadUi("views/registrarEmpleado.ui", self)
        self.menu = menu 
        self.iniGui()

        self.btnCrearEmpleado.clicked.connect(self.crearEmpleado)

        # Crear una instancia de la conexión a la base de datos
        self.db = Conexion()
        self.salario = 0

        # Cargar datos comboBox
        self.cargarSucursales()
        self.cargarCargos()


    def iniGui(self):
        # Conectar el botón de regresar al menú
        self.btnRegresar.clicked.connect(self.regresarAlMenu)

    def cargarSucursales(self):
        conexion = self.db.connect()
        if conexion:
            try:
                cursor = conexion.cursor()
                # Consulta para obtener las sucursales
                cursor.execute("SELECT idSucursal, NombreSucursal FROM Sucursales")
                sucursales = cursor.fetchall()

                # Limpiar el ComboBox antes de llenarlo
                self.comboBoxSucursal.clear()

                # Llenar el ComboBox con los nombres de las sucursales y sus ids
                for id_sucursal, nombre in sucursales:
                    self.comboBoxSucursal.addItem(nombre, id_sucursal)  # Almacenar id en el segundo parámetro
                cursor.close()

                self.comboBoxSucursal.setCurrentIndex(-1)

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al cargar las sucursales: {str(e)}")
                print(f"Error al cargar las sucursales: {str(e)}")  # Asegúrate de que se imprima el error
            finally:
                self.db.close()
        else:
            QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos")

    def cargarCargos(self):
        conexion = self.db.connect()
        if conexion:
            try:
                cursor = conexion.cursor()
                # Consulta para obtener los cargos
                cursor.execute("SELECT idCargo, NombreCargo FROM Cargo")
                cargos = cursor.fetchall()

                # Limpiar el ComboBox antes de llenarlo
                self.comboBoxCargo.clear()
                
                # Llenar el ComboBox con los nombres de los cargos y sus ids
                for id_cargo, nombre_cargo in cargos:
                    self.comboBoxCargo.addItem(f"{nombre_cargo}", id_cargo)
                cursor.close()

                self.comboBoxCargo.setCurrentIndex(-1)

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al cargar los cargos: {str(e)}")
                print(f"Error al cargar los cargos: {str(e)}")
            finally:
                self.db.close()
        else:
            QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos")

    def regresarAlMenu(self):
        self.close()
        self.menu.show()

    def crearEmpleado(self):
        cedula = self.txtCedula.text().strip()
        nombre = self.txtNombre.text().strip()
        clave = self.txtContrasenia.text().strip()
        email = self.txtEmail.text().strip()
        id_cargo = self.comboBoxCargo.currentData()  # Obtener idCargo desde el comboBox
        id_sucursal = self.comboBoxSucursal.currentData()

        # Validaciones
        if not cedula:
            QMessageBox.warning(self, "Advertencia", "El campo de cédula no puede estar vacío")
            return
        elif not nombre:
            QMessageBox.warning(self, "Advertencia", "El campo de nombre no puede estar vacío")
            return
        elif not clave:
            QMessageBox.warning(self, "Advertencia", "El campo de contraseña no puede estar vacío")
            return
        elif not email:
            QMessageBox.warning(self, "Advertencia", "El campo de correo electrónico no puede estar vacio")
        elif id_sucursal is None:
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar una sucursal")
            return
        elif id_cargo is None:
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar un cargo")
            return

        conexion = self.db.connect()
        if conexion:
            try:
                cursor = conexion.cursor()
                # Inserción de datos del empleado
                query = """
                    INSERT INTO Empleados (cedula, clave, nombre, idCargo, idSucursal, email)
                    VALUES (?, ?, ?, ?, ?, ?)
                """
                cursor.execute(query, (cedula, clave, nombre, id_cargo, id_sucursal, email))
                conexion.commit()
                cursor.close()
                QMessageBox.information(self, "Éxito", "Empleado creado con éxito")
                print(f"Empleado creado con cédula: {cedula}, nombre: {nombre}, idCargo: {id_cargo}")
                self.limpiarCampos()
            except Exception as e:
                conexion.rollback()
                QMessageBox.critical(self, "Error", f"Error al crear el empleado: {e}")
                print(f"Error al crear el empleado: {e}")
            finally:
                self.db.close()
        else:
            QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos")

    def limpiarCampos(self):
        self.txtCedula.clear()
        self.txtNombre.clear()
        self.txtContrasenia.clear()
        self.txtEmail.clear()
        self.comboBoxCargo.setCurrentIndex(-1)
        self.comboBoxSucursal.setCurrentIndex(-1)
