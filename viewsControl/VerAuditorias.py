from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView
from conexion import Conexion

class VerAuditorias(QMainWindow):
    def __init__(self, menu):
        super().__init__()
        uic.loadUi('views/verAuditorias.ui', self)
        self.menu = menu
        self.db = Conexion()
        self.iniGui()
        self.cargarAuditorias()

    def iniGui(self):
        self.btnRegresar.clicked.connect(self.regresarAlMenu)
        self.btnActualizar.clicked.connect(self.cargarAuditorias)
        self.tableWidgetAuditorias.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

    def regresarAlMenu(self):
        """Cerrar la ventana de auditorías y regresar al menú principal."""
        self.close()
        self.menu.show()

    def obtener_auditorias(self):
        """Obtiene la lista de auditorías (login y logout) de la base de datos."""
        auditorias = []
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            # Consulta que une las tablas de Auditorias, Empleados y Cargo
            cursor.execute("""
                SELECT 
                    a.idAuditoria AS idAuditoria, 
                    e.nombre AS NombreUsuario,
                    e.cedula AS CedulaUsuario,
                    c.NombreCargo AS Cargo,
                    CONVERT(VARCHAR, a.ingreso, 120) AS Ingreso,  -- Formato ISO con hora
                    CONVERT(VARCHAR, a.salida, 120) AS Salida   -- Formato ISO con hora
                FROM 
                    Auditorias a
                JOIN 
                    Empleados e ON a.idUsuario = e.idUsuario
                JOIN 
                    Cargo c ON e.idCargo = c.idCargo;
            """)
            rows = cursor.fetchall()
            for row in rows:
                auditorias.append(row)
            return auditorias
        except Exception as e:
            print(f"Error al obtener auditorías: {e}")
            return []
        finally:
            self.db.close()

    def cargarAuditorias(self):
        """Carga las auditorías en la tabla."""
        self.tableWidgetAuditorias.setRowCount(0)  # Limpia la tabla
        auditorias = self.obtener_auditorias()  # Llama al método para obtener las auditorías

        for row_number, auditoria in enumerate(auditorias):
            self.tableWidgetAuditorias.insertRow(row_number)  # Inserta una nueva fila en la tabla
            for column_number, data in enumerate(auditoria):
                item = QTableWidgetItem(str(data))  # Coloca los datos de cada auditoría en las celdas correspondientes
                self.tableWidgetAuditorias.setItem(row_number, column_number, item)
