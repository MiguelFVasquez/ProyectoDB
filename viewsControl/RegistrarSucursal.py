from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from conexion import Conexion  # Importar la clase de conexión

class RegistrarSucursal(QMainWindow):  # Hereda de QMainWindow
    def __init__(self, menu):
        super().__init__()  # Llama al constructor de QMainWindow
        uic.loadUi("views/registrarSucursales.ui", self)  # Cargar el archivo UI
        self.menu = menu 
        self.iniGui()
        # Conectar el botón para crear sucursal
        self.btnCrearSucursal.clicked.connect(self.crearSucursal)
        # Crear una instancia de la conexión a la base de datos
        self.db = Conexion()
        self.cargarMunicipios()

    def iniGui(self):
        self.btnRegresar.clicked.connect(self.regresarAlMenu)

    def regresarAlMenu(self):
        # Cierra la ventana actual y vuelve al menú principal
        self.close()
        self.menu.show()

    def cargarMunicipios(self):
        conexion = self.db.connect()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT idMunicipio, nombre FROM Municipios")
                municipios = cursor.fetchall()

                self.comboBoxMunicipios.clear()

                # Agregar el nombre del municipio al comboBox y asociar el id como "data"
                for idMunicipio, nombreMunicipio in municipios:
                    self.comboBoxMunicipios.addItem(nombreMunicipio, idMunicipio)
                cursor.close()

                self.comboBoxMunicipios.setCurrentIndex(-1)

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al cargar los municipios: {str(e)}")
                print(f"Error al cargar los municipios: {str(e)}")
            finally:
                self.db.close()
        else:
            QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos")

    def crearSucursal(self):
        # Obtener datos de los campos de entrada
        NombreSucursal = self.txtNombreSucursal.text().strip()
        Direccion = self.txtDireccionSucursal.text().strip()
        # Obtener el id del municipio seleccionado
        MunicipioId = self.comboBoxMunicipios.currentData()

        # Validar que los campos no estén vacíos
        if not NombreSucursal or not Direccion or MunicipioId is None:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
            return
        
        # Conectar a la base de datos e insertar la sucursal
        conexion = self.db.connect()  # Obtener conexión
        if conexion:
            try:
                cursor = conexion.cursor()

                # Consulta SQL para insertar la sucursal usando el id del municipio
                query = """
                    INSERT INTO Sucursales (NombreSucursal, Direccion, Municipio)
                    VALUES (?, ?, ?)
                """
                cursor.execute(query, (NombreSucursal, Direccion, MunicipioId))
                conexion.commit()  # Confirmar la transacción
                cursor.close()

                # Mostrar mensaje de éxito
                QMessageBox.information(self, "Éxito", "Sucursal registrada correctamente.")
                self.limpiarCampos()

            except Exception as e:
                conexion.rollback()  # Revertir la transacción en caso de error
                QMessageBox.critical(self, "Error", f"Ocurrió un error al registrar la sucursal: {str(e)}")
                print(f"Error al registrar la sucursal: {str(e)}")

            finally:
                self.db.close()  # Cerrar la conexión a la base de datos
        else:
            QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos")

    def limpiarCampos(self):
        # Limpiar los campos después de registrar
        self.txtNombreSucursal.clear()
        self.txtDireccionSucursal.clear()
        self.comboBoxMunicipios.setCurrentIndex(-1)
