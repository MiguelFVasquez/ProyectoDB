# **Como crear un empleado**

Este apartado describe el proceso para registrar un nuevo empleado en el sistema, incluyendo los campos requeridos y las funcionalidades disponibles.

---

## Campos del formulario

El formulario de registro de empleado incluye los siguientes campos:

1. **Cédula**:  
    - **Descripción:** Número de identificación único del empleado.  
    - **Formato:** Número entero sin espacios ni caracteres especiales.  
    - **Ejemplo:** `1023456789`.

2. **Nombre**:  
    - **Descripción:** Nombre completo del empleado.  
    - **Formato:** Cadena de texto (alfanumérico).  
    - **Ejemplo:** `Juan Pérez`.

3. **Contraseña**: 
    - **Descripción:** Clave de acceso para el empleado.  
    - **Formato:** Texto con un mínimo de 8 caracteres, incluyendo al menos un número y un carácter especial.  
    - **Ejemplo:** `Ju4nP3r3z!`.

4. **Email**:
    - **Descripción:** Dirección de correo electrónico del empleado para notificaciones sobre el sistema y solicitudes de préstamo.  
    - **Formato:** Correo electrónico válido.  
    - **Ejemplo:** `juan.perez@empresa.com`.

5. **Sucursal**:
    - **Descripción:** Combobox para seleccionar la sucursal donde trabaja el empleado.  
    - **Opciones:** Las sucursales existentes en el sistema.  
    - **Ejemplo:**:  
        - Sucursal Quimbaya  
        - Sucursal Filandia  

6. **Cargo**:
    - **Descripción:** Combobox para seleccionar el cargo del empleado en la empresa.  
    - **Opciones:** Los cargos disponibles según la configuración del sistema.  
    - **Ejemplo:** :
        - Operario  
        - Administrativo

---

## Proceso de Registro

1. Accede al módulo de **Empleados** en el sistema.
2. Haz clic en el botón **Crear Empleado**.
3. Completa los campos obligatorios según las siguientes indicaciones:
   - **Cédula:** Ingresa el número de cédula del empleado.  
   - **Nombre:** Ingresa el nombre completo del empleado.  
   - **Contraseña:** Define una contraseña segura.  
   - **Email:** Proporciona el correo electrónico del empleado.  
   - **Sucursal:** Selecciona la sucursal desde el combobox.  
   - **Cargo:** Selecciona el cargo desde el combobox.
4. Verifica que los datos ingresados son correctos.
5. Haz clic en el botón **Crear** para registrar al empleado.

---

## Validaciones

- La **cédula** debe ser única en el sistema. Si intentas registrar un empleado con una cédula existente, se mostrará un error.  
- El **email** debe ser válido y único.  
- La **contraseña** debe cumplir con los requisitos mínimos de seguridad.  
- Tanto la **sucursal** como el **cargo** deben seleccionarse de las opciones disponibles.

---

## Notificaciones

Después de registrar al empleado:
- Se enviará un correo electrónico al email proporcionado con las credenciales de acceso y un enlace para cambiar la contraseña en caso necesario.

