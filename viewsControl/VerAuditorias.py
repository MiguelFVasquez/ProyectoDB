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
        self.btnBuscar.clicked.connect(self.buscarPorCedula)
        self.tableWidgetAuditorias.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

    def buscarPorCedula(self):
        """Busca auditorías filtradas por la cédula."""
        cedula = self.txtCedula.text()  # Obtiene el texto ingresado en el campo de búsqueda
        self.cargarAuditorias(cedula)  # Llama a cargarAuditorias con el filtro de cédula

    def regresarAlMenu(self):
        """Cerrar la ventana de auditorías y regresar al menú principal."""
        self.close()
        self.menu.show()

    def obtener_auditorias(self, cedula=None):
        """Obtiene la lista de auditorías de la base de datos, con filtro opcional por cédula."""
        auditorias = []
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            
            # Consulta que une las tablas de Auditorias, Empleados y Cargo
            # Se agrega un filtro opcional por cédula si se proporciona
            query = """
                SELECT 
                    e.idUsuario AS idUsuario, 
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
                    Cargo c ON e.idCargo = c.idCargo
            """
            
            # Si se proporciona un filtro de cédula, lo agregamos a la consulta
            if cedula:
                query += " WHERE e.cedula LIKE ?"
                cursor.execute(query, ('%' + cedula + '%',))  # Usa el comodín '%' para buscar coincidencias parciales
            else:
                cursor.execute(query)
            
            rows = cursor.fetchall()
            for row in rows:
                auditorias.append(row)
            return auditorias
        except Exception as e:
            print(f"Error al obtener auditorías: {e}")
            return []
        finally:
            self.db.close()


    def cargarAuditorias(self, cedula=None):
        """Carga las auditorías en la tabla, aplicando un filtro opcional por cédula."""
        self.tableWidgetAuditorias.setRowCount(0)  # Limpia la tabla
        auditorias = self.obtener_auditorias(cedula)  # Llama al método para obtener auditorías con el filtro de cédula

        for row_number, auditoria in enumerate(auditorias):
            self.tableWidgetAuditorias.insertRow(row_number)  # Inserta una nueva fila en la tabla
            for column_number, data in enumerate(auditoria):
                item = QTableWidgetItem(str(data))  # Coloca los datos de cada auditoría en las celdas correspondientes
                self.tableWidgetAuditorias.setItem(row_number, column_number, item)
