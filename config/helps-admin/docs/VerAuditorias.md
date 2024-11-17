# **Ver Auditorías de Acceso**

Esta sección permite observar las auditorías de acceso al sistema por parte de los empleados. La información se presenta en una tabla que detalla las entradas y salidas registradas.

---

## Tabla de Auditorías de Acceso

La tabla muestra los siguientes datos:

1. **ID del Empleado**: 
    - **Descripción:** Identificador único del empleado.  
    - **Formato:** Número entero autogenerado por el sistema.  
    - **Ejemplo:** `1`, `20`.

2. **Nombre del Empleado**: 
    - **Descripción:** Nombre completo del empleado.  
    - **Formato:** Cadena de texto.  
    - **Ejemplo:** `Juan Pérez`.

3. **Cédula del Empleado**:  
    - **Descripción:** Número de identificación único del empleado.  
    - **Formato:** Número entero sin caracteres especiales.  
    - **Ejemplo:** `1023456789`.

4. **Cargo**:  
    - **Descripción:** Cargo del empleado dentro de la empresa.  
    - **Formato:** Texto predefinido en el sistema.  
    - **Ejemplo:** `Operario`, `Administrativo`.

5. **Ingreso al Sistema**: 
    - **Descripción:** Fecha y hora en que el empleado ingresó al sistema.  
    - **Formato:** Fecha y hora en formato `DD/MM/AAAA HH:MM`.  
    - **Ejemplo:** `15/11/2024 08:30`.

6. **Salida del Sistema**:
    - **Descripción:** Fecha y hora en que el empleado cerró sesión en el sistema.  
    - **Formato:** Fecha y hora en formato `DD/MM/AAAA HH:MM`.  
    - **Ejemplo:** `15/11/2024 17:00`.

---

## Visualización de la Tabla

Para acceder a esta información:

1. Ve al módulo **Auditorías de Acceso** en el sistema.
2. Se cargará una tabla que muestra todos los registros de entrada y salida de los empleados.

---

## Ejemplo de Tabla

| ID Empleado | Nombre       | Cédula      | Cargo      | Ingreso al Sistema   | Salida del Sistema    |
|-------------|--------------|-------------|------------|----------------------|-----------------------|
| 1           | Juan Pérez   | 1023456789  | Operario    | 15/11/2024 08:30    | 15/11/2024 17:00     |
| 2           | Ana Gómez    | 1034567890  | Administrativo  | 15/11/2024 09:00    | 15/11/2024 18:00     |

---

## Características

1. **Visualización Completa:**  
   - Muestra todos los accesos registrados en el sistema, incluyendo la hora de ingreso y salida.

2. **Busqueda por cedula:**  
   - Puedas usar el filtro de busqueda por cedula para encontrar las auditorias de acceso de un empleado.

---

## Restricciones

- Este apartado es **solo de consulta**, no se pueden editar ni eliminar los registros.

---

## Consejos para el Usuario

- Revisa esta sección periódicamente para supervisar los horarios de acceso y salida de los empleados.
- Utiliza el filtro por cedula disponible para localizar registros específicos más fácilmente.

---


