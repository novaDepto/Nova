## Responsables
Nombre     | Rol
-----------|------------------
Raymundo   | Autor

## Objetivo
1. Asegurar la preparación del entorno de verificación.

## Características
<table>
  <thead>
    <tr>
      <th>Atributo</th>
      <th>Descripción</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Selección de productos</td>
      <td>Se verifican los productos de trabajo que hayan sido completados.</td>
    </tr>
    <tr>
    <td>Se recomienda que se verifiquen los Work Items por <strong>historia de usuario.</strong></td>
    </tr>
    <tr>
      <td>Método de verificación</td>
      <td><strong>Pair Review.</strong></td>
    </tr>
    <tr>
      <td rowspan="2">Criterios de verificación</td>
      <td>Varían por producto de trabajo.</td>
    </tr>
    <tr>
      <td>Se encuentran en el Reporte de Verificación.</td>
    </tr>
    <tr>
    </tr>
    <tr>
      <td>Espacio de verificación</td>
      <td>La verificación se realiza en un canal de Discord separado de los usados por el equipo para trabajar.</td>
    </tr>
    <tr>
      <td rowspan="2">Herramienta de verificación</td>
      <td><a href="https://docs.google.com/spreadsheets/d/1WccrRu2iMWX6y1USG_k5nElfajfu6ACS1L11QNGuKN0/edit#gid=39101311"><strong>Reporte de Verificación</strong></a> = Registra los resultados, observaciones y correcciones a realizar a los productos de trabajo verificados.</td>
    </tr>
    <tr>
      <td>Se realiza un Reporte de Verificación por historia de usuario.</td>
    </tr>
  </tbody>
</table>

## Pair Review
<table>
  <thead>
    <tr>
      <th>Atributo</th>
      <th>Descripción</th>
    </tr>
  </thead>
  <tbody>
     <tr>
      <td>Tipo</td>
      <td>Inspección.</td>
    </tr>
    <tr>
      <td>Petición</td>
      <td>A demanda.</td>
    </tr>
    <tr>
      <td>Input</td>
      <td>Petición de verificación de un producto de trabajo.</td>
    </tr>
    <tr>
      <td>Precondiciones</td>
      <td>El producto de trabajo debe estar terminado.</td>
    </tr>
    <tr>
      <td>Output</td>
      <td>Producto de trabajo verificado.</td>
    </tr>
    <tr>
      <td rowspan="2">Actividades</td>
      <td>Inspeccionar el producto de trabajo.</td>
    </tr>
    <tr>
      <td>Documentar los resultados de la inspección.</td>
    </tr>
    <tr>
      <td>Seguimiento</td>
      <td>Se recomienda pedir una nueva Pair Review hasta que un producto de trabajo esté corregido según las observaciones de la verificación anterior.</td>
    </tr>
  </tbody>
</table>

## Sobre los productos de trabajo
1. Los productos de trabajo se dividen en dos grandes categorías:
* **Documentación**: Manuales/Diagramas
* **Código**: Base de datos, Frontend, Backend
2. Los productos de trabajo pueden tener criterios de verificación comunes y únicos.
3. **NO SE RECOMIENDA** verificar productos de trabajo de diferentes historias de usuario que sean del mismo tipo porque puede generar confusión y un desarrollo en cascada que va en contra de los principios del desarrollo ágil.

***
versión 0.2a
