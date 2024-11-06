from PyQt6 import uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from conexion import Conexion

class InformeCuotas(QMainWindow):
    def __init__(self, menuUsuarios, id_usuario):
        super().__init__()
        uic.loadUi("views/InformeCuotas.ui", self)
        self.menuUsuarios = menuUsuarios
        self.db = Conexion()
        self.id_usuario = id_usuario  # ID del usuario que inicia sesión
        self.iniGui()

    def iniGui(self):
        self.btnRegresar.clicked.connect(self.regresarAlMenu)
        self.btnCrearPagoCuota.clicked.connect(self.registrarPago)

        # Cargar los préstamos en el comboBox
        self.cargarPrestamos()

        # Autocompletar `txtFechaPago` con la fecha actual y deshabilitar el campo
        fecha_actual = QDate.currentDate().toString("dd-MM-yyyy")
        self.txtFechaPago.setText(fecha_actual)
        self.txtFechaPago.setEnabled(False)  # Deshabilitar el campo para evitar ediciones

        # Conectar el cambio de selección del préstamo para actualizar el valor
        self.comboBoxPrestamos.currentIndexChanged.connect(self.actualizarValorPrestamo)
        self.txtValorPago.setEnabled(False)

    def cargarPrestamos(self):
        """Carga los préstamos del usuario en el comboBox."""
        try:
            conn = self.db.connect()
            cursor = conn.cursor()

            # Consulta para obtener los préstamos del usuario, uniendo SolicitudPrestamos con Prestamos
            cursor.execute("""
                SELECT p.numeroPrestamos, p.ValorPorMes 
                FROM Prestamos p
                INNER JOIN SolicitudPrestamo sp ON p.codigoSolicitud = sp.codigo
                WHERE sp.Usuario = ?
            """, (self.id_usuario,))

            prestamos = cursor.fetchall()

            # Limpiar comboBox y añadir los préstamos
            self.comboBoxPrestamos.clear()
            for prestamo in prestamos:
                id_prestamo, monto = prestamo
                self.comboBoxPrestamos.addItem(f"Préstamo {id_prestamo}", monto)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudieron cargar los préstamos: {e}")
        finally:
            self.db.close()


    def actualizarValorPrestamo(self):
        """Actualiza el valor del préstamo seleccionado en el campo de valor."""
        monto = self.comboBoxPrestamos.currentData()  # Obtener el monto del préstamo seleccionado
        if monto:
            self.txtValorPago.setText(str(monto))

    def regresarAlMenu(self):
        # Cierra la ventana actual y muestra el menú principal
        self.close()
        self.menuUsuarios.show()

    def registrarPago(self):
        """Registra el pago de una cuota y valida los campos del formulario."""
        num_prestamo = self.comboBoxPrestamos.currentText().split()[1]  # Obtener el id del préstamo seleccionado
        num_cuota = self.txtPagoCuota.text()
        fecha_pago = self.txtFechaPago.text()  # Ya contiene la fecha actual deshabilitada
        valor_pago = self.txtValorPago.text()

        if not num_prestamo or not num_cuota or not valor_pago:
            QMessageBox.warning(self, "Error", "Todos los campos deben ser completados.")
            return

        # Validación del valor a pagar
        if float(valor_pago) <= 0:
            QMessageBox.warning(self, "Error", "El valor a pagar debe ser mayor que cero.")
            return

        # Validar si el pago se realizó antes del día 10 del mes
        fecha_pago_obj = QDate.fromString(fecha_pago, "dd-MM-yyyy")
        if fecha_pago_obj.day() > 10:
            # Si es después del día 10, marcar como moroso
            self.marcarComoMoroso(num_cuota)

        # Registrar la cuota pagada en la base de datos
        try:
            conn = self.db.connect()
            cursor = conn.cursor()

            # Insertar un registro en la tabla de Cuotas (esto supone que creas la cuota en la base de datos)
            cursor.execute("""
                INSERT INTO Cuotas (idPrestamo, numCuota, fechaVencimiento, valorPagado, fechaDePago, idEstado)
                VALUES (?, ?, ?, ?, ?, (SELECT idEstado FROM EstadoCuota WHERE estado = 'Pagado'))
            """, (num_prestamo, num_cuota, fecha_pago, valor_pago, fecha_pago))

            conn.commit()
            QMessageBox.information(self, "Éxito", "Pago registrado exitosamente.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al registrar el pago: {e}")
        finally:
            self.db.close()

    def marcarComoMoroso(self, num_cuota):
        """Marca la cuota como morosa si el pago es posterior al 10 de cada mes."""
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Cuotas 
                SET idEstado = (SELECT idEstado FROM EstadoCuota WHERE estado = 'Moroso')
                WHERE numCuota = ?
            """, (num_cuota,))
            conn.commit()
            QMessageBox.warning(self, "Aviso", "El pago se registró tarde, el empleado será marcado como moroso.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al marcar como moroso: {e}")
        finally:
            self.db.close()
