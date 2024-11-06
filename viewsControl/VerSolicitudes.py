from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget, QAbstractItemView
from conexion import Conexion 

class VerSolicitudes(QMainWindow):
    def __init__(self,menuUsuarios,Usuario):
        super().__init__()
        uic.loadUi("views/VerSolicitudes.ui",self)
        self.menuUsuarios = menuUsuarios
        self.Usuario = Usuario
        self.db = Conexion()  
        self.iniGui()
        self.cargarSolicitudes()

    def iniGui(self):
        self.btnRegresar.clicked.connect(self.regresarAlMenu)
        self.btnActualizar.clicked.connect(self.cargarSolicitudes)
        self.tableWidgetPrestamos.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

    def regresarAlMenu(self):
        # Cierra la ventana actual y muestra el menú principal
        self.close()
        self.menuUsuarios.show()

    def obtener_prestamos(self):
        """Obtiene los préstamos pendientes de la base de datos para el usuario actual."""
        prestamos = []
        try:
            conn = self.db.connect()  # Conectar a la base de datos
            cursor = conn.cursor()
            # Filtra los préstamos según el usuario actual y solo selecciona los pendientes
            cursor.execute(""" 
                SELECT 
                    sp.codigo AS idSolicitud, 
                    sp.monto AS Monto, 
                    p.numeroMeses AS Periodo, 
                    es.estado AS Estado, 
                    sp.FechaSolicitud AS FechaCreacion 
                FROM 
                    SolicitudPrestamo sp 
                JOIN 
                    Estado es ON sp.estado = es.codigo
                JOIN 
                    Periodo p ON sp.periodo = p.codigo
                WHERE 
                    sp.Usuario = ?  -- Filtrar por el usuario actual                  
            """, (self.Usuario,))  # Pasar el ID del usuario actual

            rows = cursor.fetchall()
            for row in rows:
                prestamos.append(row)
            return prestamos
        except Exception as e:
            print(f"Error al obtener préstamos: {e}")
            return []
        finally:
            self.db.close()

    def cargarSolicitudes(self):
        """Carga las solicitudes pendientes en la tabla."""
        self.tableWidgetPrestamos.setRowCount(0)  # Limpia la tabla
        solicitudes = self.obtener_prestamos()  # Cambia obtener_solicitudes a obtener_prestamos

        for row_number, solicitud in enumerate(solicitudes):
            self.tableWidgetPrestamos.insertRow(row_number)
            for column_number, data in enumerate(solicitud):
                item = QTableWidgetItem(str(data))
                self.tableWidgetPrestamos.setItem(row_number, column_number, item)  # Asegúrate de que el nombre de la tabla sea correcto
