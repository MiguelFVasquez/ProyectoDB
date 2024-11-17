from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView
from conexion import Conexion

class VerPrestamosUsuarios(QMainWindow):
    def __init__(self, menu):
        super().__init__()
        uic.loadUi('views/VerPrestamosUsuarios.ui', self)
        self.menu = menu
        self.db = Conexion()
        self.iniGui()
        self.cargarPrestamosUsuarios()

    def iniGui(self):
        self.btnRegresar.clicked.connect(self.regresarAlMenu)
        self.btnActualizar.clicked.connect(self.cargarPrestamosUsuarios)  # Conectar botón de actualizar
        self.btnBuscar.clicked.connect(self.buscarPrestamosPorCedula)  # Conectar botón de búsqueda por cédula
        self.tableWidgetPrestamosUsuarios.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

    def regresarAlMenu(self):
        """Cerrar la ventana de préstamos y regresar al menú principal."""
        self.close()
        self.menu.show()

    def obtener_prestamos_usuarios(self, cedula=""):
        """Obtiene la lista de préstamos de usuarios, filtrados por cédula si es necesario."""
        prestamos = []
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            
            # Consulta SQL con JOIN entre las tablas necesarias y filtro opcional por cédula
            query = """
                SELECT 
                    e.idUsuario AS idUsuario, 
                    e.nombre AS NombreUsuario,
                    e.cedula AS CedulaUsuario,
                    c.NombreCargo AS Cargo,
                    sp.codigo AS idPrestamo,  -- Utilizamos el código de la tabla SolicitudPrestamo
                    sp.monto AS Monto,
                    pe.numeroMeses AS Meses,
                    es.estado AS EstadoPrestamo,
                    CONVERT(VARCHAR, sp.FechaSolicitud, 120) AS FechaCreacion  -- Tomamos la fecha de creación de la tabla SolicitudPrestamo
                FROM 
                    SolicitudPrestamo sp
                JOIN 
                    Empleados e ON sp.Usuario = e.idUsuario
                JOIN 
                    Cargo c ON e.idCargo = c.idCargo
                JOIN 
                    Periodo pe ON sp.periodo = pe.codigo
                JOIN 
                    Estado es ON sp.estado = es.codigo

            """
            
            # Si se pasa una cédula, se añade un filtro por ella
            if cedula:
                query += " WHERE e.cedula LIKE ?"
                cursor.execute(query, ('%' + cedula + '%',))
            else:
                cursor.execute(query)

            rows = cursor.fetchall()
            for row in rows:
                prestamos.append(row)
            
            return prestamos
        except Exception as e:
            print(f"Error al obtener préstamos de usuarios: {e}")
            return []
        finally:
            self.db.close()


    def cargarPrestamosUsuarios(self, cedula=None):
        """Carga los datos de préstamos de usuarios en la tabla."""
        self.tableWidgetPrestamosUsuarios.setRowCount(0)  # Limpia la tabla
        prestamos = self.obtener_prestamos_usuarios(cedula)  # Llama al método para obtener los datos

        for row_number, prestamo in enumerate(prestamos):
            self.tableWidgetPrestamosUsuarios.insertRow(row_number)  # Inserta una nueva fila en la tabla
            for column_number, data in enumerate(prestamo):
                item = QTableWidgetItem(str(data))  # Coloca los datos de cada préstamo en las celdas correspondientes
                self.tableWidgetPrestamosUsuarios.setItem(row_number, column_number, item)

    def buscarPrestamosPorCedula(self):
        """Busca los préstamos por cédula y actualiza la tabla."""
        cedula = self.txtCedula.text()  # Obtiene el texto de txtCedula
        self.cargarPrestamosUsuarios(cedula)  # Llama al método para obtener los datos filtrados (sin pasar los resultados)
