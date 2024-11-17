# **Crear Sucursales**

Esta sección permite registrar nuevas sucursales de la empresa. Cada sucursal debe estar ubicada en uno de los municipios del departamento del Quindío, Colombia.

---

## Formulario de Creación de Sucursales

El formulario para crear una nueva sucursal incluye los siguientes campos:

### 1. **Nombre de la Sucursal**
   - **Descripción:** Nombre asignado a la sucursal, el cual debe coincidir con el municipio donde se encuentra ubicada.  
   - **Formato:** Cadena de texto.  
   - **Restricción:** El nombre debe ser igual al nombre del municipio seleccionado en el campo "Municipio".  
   - **Ejemplo:** Si el municipio es `Armenia`, el nombre de la sucursal debe ser `Armenia`.

### 2. **Dirección**
   - **Descripción:** Dirección específica donde se encuentra la sucursal dentro del municipio seleccionado.  
   - **Formato:** Cadena de texto alfanumérica.  
   - **Ejemplo:** `Calle 12 #8-45`.

### 3. **Municipio**
   - **Descripción:** Municipio del departamento del Quindío donde estará ubicada la sucursal.  
   - **Formato:** Selección a través de un **ComboBox** con una lista predefinida de los municipios del Quindío.  
   - **Opciones Disponibles:**  
     - Armenia  
     - Calarcá  
     - Circasia  
     - Córdoba  
     - Filandia  
     - Génova  
     - La Tebaida  
     - Montenegro  
     - Pijao  
     - Quimbaya  
     - Salento  

---

## Reglas de Validación

- **Coincidencia de Nombre y Municipio:**  
  El valor ingresado en "Nombre de la Sucursal" debe coincidir con el municipio seleccionado en el campo "Municipio".  

- **Dirección Obligatoria:**  
  La dirección no puede estar vacía ni contener caracteres inválidos.

- **Municipio Seleccionado:**  
  Se debe seleccionar un municipio de la lista proporcionada; no se permiten valores personalizados.

---

## Pasos para Crear una Nueva Sucursal

1. Dirígete a la sección **Crear Sucursales** en el módulo de configuración del sistema.
2. Llena los campos del formulario con la información requerida:
   - Ingresa el **nombre** de la sucursal.
   - Proporciona la **dirección** exacta.
   - Selecciona el **municipio** desde el ComboBox.
3. Verifica que toda la información sea correcta.
4. Haz clic en el botón **Guardar** para registrar la sucursal.

---

## Ejemplo de Formulario

| Campo               | Ejemplo                  |
|---------------------|--------------------------|
| **Nombre de Sucursal** | Sucursal Armenia                 |
| **Dirección**       | Calle 12 #8-45          |
| **Municipio**       | Armenia                 |


