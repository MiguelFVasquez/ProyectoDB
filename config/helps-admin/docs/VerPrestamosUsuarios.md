# **Ver Préstamos de Empleados**

En esta sección, puedes visualizar los préstamos solicitados por los empleados registrados en el sistema. La información se presenta en una tabla detallada con opción de búsqueda por cédula.

---

## Tabla de Préstamos

La tabla muestra los siguientes datos para cada solicitud de préstamo:

1. **ID del Empleado**: 
    - **Descripción:** Identificador único del empleado asociado al préstamo.  
    - **Formato:** Número entero.  
    - **Ejemplo:** `1`, `15`.

2. **Nombre del Empleado**: 
    - **Descripción:** Nombre completo del empleado que solicitó el préstamo.  
    - **Formato:** Cadena de texto.  
    - **Ejemplo:** `Juan Pérez`.

3. **Cédula del Empleado**:  
    - **Descripción:** Número de identificación del empleado.  
    - **Formato:** Número entero sin caracteres especiales.  
    - **Ejemplo:** `1023456789`.

4. **Cargo**:  
    - **Descripción:** Cargo del empleado dentro de la empresa.  
    - **Formato:** Texto predefinido en el sistema.  
    - **Ejemplo:** `Operario`, `Administrativo`.

5. **ID del Préstamo**:
    - **Descripción:** Identificador único de la solicitud de préstamo.  
    - **Formato:** Número entero.  
    - **Ejemplo:** `1`, `18`.

6. **Monto**:
    - **Descripción:** Cantidad de dinero solicitada en el préstamo.  
    - **Formato:** Número con decimales en la moneda correspondiente.  
    - **Ejemplo:** `$10,000,000`.

7. **Meses**:
    - **Descripción:** Número de meses para los cuales se solicitó el préstamo.  
    - **Formato:** Número entero.  
    - **Ejemplo:** `24`, `48`.

8. **Estado**:  
    - **Descripción:** Estado actual de la solicitud de préstamo.  
    - **Formato:** Texto predefinido en el sistema.  
    - **Opciones comunes:**:  
        - **Pendiente:** La solicitud está en espera de aprobación.  
        - **Aprobado:** La solicitud fue aprobada.  
        - **Rechazado:** La solicitud fue rechazada.  

9. **Fecha de Creación**:  
    - **Descripción:** Fecha en que se generó la solicitud de préstamo.  
    - **Formato:** Fecha en formato `DD/MM/AAAA`.  
    - **Ejemplo:** `15/11/2024`.

---

## Funcionalidades de la Tabla

### Visualización General
- La tabla muestra todos los préstamos registrados en el sistema.

### Búsqueda por Cédula
- Usa la barra de búsqueda para filtrar los préstamos por el número de cédula de un empleado.
- **Cómo buscar:**
  1. Introduce el número de cédula en el campo de búsqueda.
  2. La tabla mostrará únicamente las solicitudes de préstamo asociadas a esa cédula.

---

## Ejemplo de Tabla

| ID Empleado | Nombre       | Cédula      | Cargo     | ID Préstamo | Monto        | Meses | Estado     | Fecha de Creación |
|-------------|--------------|-------------|-----------|-------------|--------------|-------|------------|--------------------|
| 1           | Juan Pérez   | 1023456789  | Operario  | 1001        | $5,000,000   | 12    | Aprobado   | 10/10/2024        |
| 2           | Ana Gómez    | 1034567890  | Administrativo    | 1002        | $2,500,000   | 24    | Pendiente  | 12/11/2024        |

---

## Restricciones

- **Solo visualización:** No es posible editar ni eliminar registros desde esta sección.

---

## Consejos para el Usuario

1. **Búsqueda eficiente:** Asegúrate de ingresar el número de cédula completo y sin espacios para obtener resultados precisos.
2. **Estados de préstamos:** Consulta el significado de cada estado en la sección de ayuda si tienes dudas.


