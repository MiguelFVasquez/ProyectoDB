from PyQt6 import uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from conexion import Conexion

class InformeCuotas(QMainWindow):
    def __init__(self, menuUsuarios):
        super().__init__()
        uic.loadUi("views/InformeCuotas.ui", self)
        self.menuUsuarios = menuUsuarios
        self.db = Conexion()
        self.iniGui()

    def iniGui(self):
        self.btnRegresar.clicked.connect(self.regresarAlMenu)
        self.btnCrearPagoCuota.clicked.connect(self.registrarPago)

    def regresarAlMenu(self):
        # Cierra la ventana actual y muestra el menú principal
        self.close()
        self.menuUsuarios.show()

    # def obtener_cuotas(self):
    #     """Obtiene las cuotas pendientes de la base de datos para el usuario actual."""
    #     cuotas = []
    #     num_prestamo = self.txtNumeroPrestamo.text()  # Obtener el número de préstamo desde el formulario

    #     if not num_prestamo:
    #         QMessageBox.warning(self, "Error", "Debe ingresar un número de préstamo.")
    #         return cuotas  # Si no se ha ingresado un número de préstamo, retorna una lista vacía

    #     try:
    #         conn = self.db.connect()  # Conectar a la base de datos
    #         cursor = conn.cursor()
    #         cursor.execute(""" 
    #             SELECT 
    #                 c.idCuota AS idCuota, 
    #                 c.valorPagado AS ValorPagado, 
    #                 c.fechaDePago AS FechaDePago, 
    #                 c.numCuota, 
    #                 c.fechaVencimiento, 
    #                 ec.estado AS Estado
    #             FROM 
    #                 Cuotas c 
    #             JOIN 
    #                 EstadoCuota ec ON c.idEstado = ec.idEstado
    #             WHERE 
    #                 c.idPrestamo = ? AND c.idEstado != (SELECT idEstado FROM EstadoCuota WHERE estado = 'Pagado')
    #         """, (num_prestamo,))  # Filtra por el número de préstamo obtenido del formulario

    #         rows = cursor.fetchall()
    #         for row in rows:
    #             cuotas.append(row)
    #         return cuotas
    #     except Exception as e:
    #         print(f"Error al obtener cuotas: {e}")
    #         return []
    #     finally:
    #         self.db.close()

    def registrarPago(self):
        """Registra el pago de una cuota y valida los campos del formulario."""
        num_prestamo = self.txtNumeroPrestamo.text()
        num_cuota = self.txtPagoCuota.text()
        fecha_pago = self.dateEditFecha.date().toString("yyyy-MM-dd")
        valor_pago = self.txtValorPago.text()

        if not num_prestamo or not num_cuota or not valor_pago:
            QMessageBox.warning(self, "Error", "Todos los campos deben ser completados.")
            return

        # Validación del valor a pagar
        if float(valor_pago) <= 0:
            QMessageBox.warning(self, "Error", "El valor a pagar debe ser mayor que cero.")
            return

        # Validar si el pago se realizó antes del día 10 del mes
        fecha_pago_obj = QDate.fromString(fecha_pago, "yyyy-MM-dd")
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
