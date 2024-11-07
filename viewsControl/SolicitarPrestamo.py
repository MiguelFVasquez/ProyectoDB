from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from conexion import Conexion  # Clase de conexión
from datetime import datetime
from config.EmailService import EmailService

class SolicitarPrestamo(QMainWindow):
    def __init__(self, menuUsuarios, Usuario):
        super().__init__()
        uic.loadUi("views/SolicitarPrestamo.ui", self)
        self.menuUsuarios = menuUsuarios
        self.Usuario = Usuario  # ID del empleado que hace la solicitud
        self.db = Conexion()  # Instancia de conexión a la base de datos
        self.iniGui()
        self.cargarPeriodos()  # Cargar períodos en el comboBox

    def iniGui(self):
        # Configurar los botones
        self.btnSolicitar.clicked.connect(self.crearSolicitud)
        self.btnRegresar.clicked.connect(self.regresarAlMenu)

    def regresarAlMenu(self):
        # Cierra la ventana actual y muestra el menú principal
        self.close()
        self.menuUsuarios.show()

    def cargarPeriodos(self):
        # Cargar períodos desde la base de datos y agregar al comboBox
        conexion = self.db.connect()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT codigo, numeroMeses FROM Periodo")
                periodos = cursor.fetchall()
                for codigo, numeroMeses in periodos:
                    self.comboBoxCargo.addItem(str(numeroMeses), codigo)
                cursor.close()

                # Establecer índice no seleccionado
                self.comboBoxCargo.setCurrentIndex(-1)

            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudieron cargar los períodos: {str(e)}")
            finally:
                self.db.close()
        else:
            QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos")

    def crearSolicitud(self):
        # Obtener monto y período seleccionado
        monto = self.txtMonto.text().strip()
        if not monto.isdigit():
            QMessageBox.warning(self, "Error", "Por favor, ingrese un monto válido.")
            return
        monto = int(monto)
        periodo_codigo = self.comboBoxCargo.currentData()  # Código del período seleccionado
        fecha_actual = datetime.now().strftime('%Y-%m-%d')  # Fecha de creación actual

        # Conectar a la base de datos y verificar el cargo del usuario
        conexion = self.db.connect()
        if conexion:
            try:
                cursor = conexion.cursor()
                
                # Consulta para obtener el idCargo, nombre y email del empleado
                cursor.execute("SELECT idCargo, nombre, email FROM Empleados WHERE idUsuario = ?", (self.Usuario,))
                resultado = cursor.fetchone()
                
                if resultado is None:
                    QMessageBox.warning(self, "Error", "Empleado no encontrado.")
                    return
                
                idCargo, nombre_usuario, email_usuario = resultado
                
                # Consulta para obtener el NombreCargo usando el idCargo
                cursor.execute("SELECT NombreCargo FROM Cargo WHERE idCargo = ?", (idCargo,))
                resultado_cargo = cursor.fetchone()
                
                if resultado_cargo is None:
                    QMessageBox.warning(self, "Error", "Cargo no encontrado.")
                    return
                
                NombreCargo = resultado_cargo[0]
                
                # Definir los límites de acuerdo al cargo
                limites_cargo = {
                    "Operarios": 10000000,
                    "Administrativo": 15000000,
                    "Ejecutivo": 20000000,
                    "Otros": 12000000
                }
                
                # Obtener el límite según el NombreCargo
                limite_monto = limites_cargo.get(NombreCargo, 0)

                print(f"Cargo: {NombreCargo}, Límite: {limite_monto}")
                
                # Validar el monto
                if monto > limite_monto:
                    print("El monto excede el límite permitido para el cargo.")
                    QMessageBox.warning(self, "Solicitud rechazada", f"El monto solicitado excede el límite permitido para su cargo ({NombreCargo}).")
                    return

                # Insertar la solicitud ya que el monto es válido
                query = """
                    INSERT INTO SolicitudPrestamo (Usuario, Estado, monto, periodo, FechaSolicitud)
                    VALUES (?, ?, ?, ?, ?)
                """
                cursor.execute(query, (self.Usuario, 1, monto, periodo_codigo, fecha_actual))
                conexion.commit()

                # Mostrar mensaje de éxito y limpiar campos
                QMessageBox.information(self, "Éxito", "Solicitud de préstamo registrada correctamente.")
                self.limpiarCampos()
                
                # Enviar email de confirmación utilizando datos de la base de datos
                EmailService.emailMessages(
                    asunto="Solicitud generada con éxito!",
                    email=email_usuario,  # Usar el email obtenido de la base de datos
                    nombre=nombre_usuario,  # Usar el nombre obtenido de la base de datos
                    mensaje="Tu solicitud se ha creado y se encuentra en estado pendiente. Pronto te enviaremos más información."
                )
                QMessageBox.information(self, "Correo enviado", "Se le ha enviado un correo con la información.")

            except Exception as e:
                conexion.rollback()  # Revertir la transacción en caso de error
                QMessageBox.critical(self, "Error", f"Ocurrió un error al registrar la solicitud: {str(e)}")
            finally:
                self.db.close()
        else:
            QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos")

    def limpiarCampos(self):
        # Limpiar el campo de monto después de registrar
        self.txtMonto.clear()
        self.comboBoxCargo.setCurrentIndex(-1)  # Restablecer el comboBox
