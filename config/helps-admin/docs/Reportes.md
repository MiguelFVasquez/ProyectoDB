# Generación de Reportes de Préstamos

Esta sección describe cómo utilizar las funcionalidades de generación de reportes en la aplicación. Los reportes disponibles son los siguientes:

1. **Reporte de Préstamos por Municipio**  
2. **Reporte de Préstamos por Sucursal**  
3. **Reporte General de Cuotas Morosas**

---

## 1. Reporte de Préstamos por Municipio

### Descripción
Genera un informe detallado del total de préstamos realizados en un municipio específico. Este reporte incluye:
- El total de préstamos realizados en el municipio seleccionado.
- El monto total prestado.

### Pasos para generar el reporte:
1. Seleccione un municipio en el **ComboBox** de municipios.
2. Haga clic en el botón correspondiente para generar el reporte.
3. Si no hay préstamos en el municipio seleccionado, se mostrará un mensaje de aviso.
4. Si el reporte es exitoso, se generará un archivo PDF en la carpeta `informes/ReportesAdmin`.

### Estructura del reporte:
- **Encabezado**: Nombre del municipio seleccionado.  
- **Cuerpo**:  
  - Total de préstamos.  
  - Monto total prestado.

**Ejemplo de archivo generado**:  
`reporte_prestamos_<nombre_municipio>.pdf`

---

## 2. Reporte de Préstamos por Sucursal

### Descripción
Genera un informe detallado del total de préstamos realizados en una sucursal específica. Este reporte incluye:
- El total de préstamos realizados en la sucursal seleccionada.
- El monto total prestado.

### Pasos para generar el reporte:
1. Seleccione una sucursal en el **ComboBox** de sucursales.
2. Haga clic en el botón correspondiente para generar el reporte.
3. Si no hay préstamos en la sucursal seleccionada, se mostrará un mensaje de aviso.
4. Si el reporte es exitoso, se generará un archivo PDF en la carpeta `informes/ReportesAdmin`.

### Estructura del reporte:
- **Encabezado**: Nombre de la sucursal seleccionada.  
- **Cuerpo**:  
  - Total de préstamos.  
  - Monto total prestado.

**Ejemplo de archivo generado**:  
`reporte_prestamos_<nombre_sucursal>.pdf`

---

## 3. Reporte General de Cuotas Morosas

### Descripción
Genera un informe que detalla las cuotas de préstamos en estado de morosidad. Este reporte se basa en cuotas que no han sido pagadas antes del día **10 de cada mes**, lo que las clasifica como "morosas". El reporte incluye:
- El total de cuotas en estado moroso.
- El monto total acumulado de dichas cuotas.
- El listado de empleados responsables con detalles básicos.

### Pasos para generar el reporte:
1. Acceda a la opción **Reporte General de Cuotas Morosas** en el menú correspondiente.
2. Haga clic en el botón para generar el reporte.
3. Si no hay cuotas morosas registradas, se mostrará un mensaje de aviso.
4. Si el reporte es exitoso, se generará un archivo PDF en la carpeta `informes/ReportesAdmin`.


### Notas adicionales
- Se considera que una cuota está en estado de morosidad si la fecha límite de pago (10 de cada mes) ha sido superada y el estado de la cuota no ha sido actualizado a **pagada**.

**Ejemplo de archivo generado**:  
`reporte_cuotas_morosas_general.pdf`

---

## Solución de Problemas

### Errores comunes
- **Advertencia: "Seleccione un municipio/sucursal"**  
  Asegúrese de seleccionar un elemento válido del ComboBox.

- **Error de conexión a la base de datos**  
  Verifique que la base de datos esté en funcionamiento y que las credenciales de acceso sean correctas.

- **Reporte vacío**  
  Esto ocurre si no hay datos de préstamos o cuotas morosas disponibles. En este caso, asegúrese de que existan registros en la base de datos y que las fechas estén correctamente configuradas.

---

### Ubicación de los reportes generados
Todos los reportes se guardan automáticamente en la carpeta:  
`informes/ReportesAdmin`

Si la carpeta no existe, será creada automáticamente al momento de generar el primer reporte.

---

Con estos pasos y descripciones, podrá generar fácilmente los reportes necesarios desde la aplicación. Si encuentra algún inconveniente, no dude en contactar al equipo de soporte.
