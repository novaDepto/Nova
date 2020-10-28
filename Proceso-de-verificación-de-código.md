## Responsables
Nombre     | Rol
-----------|------------------
Charlie    | Dueño del proceso
Lisieux    | Autor
Raymundo   | Autor

## Objetivos
1. Asegurar la verificación de los productos de trabajo del proyecto
2. Asegurar la calidad de los productos de trabajo del proyecto

## Entradas
1. Productos de trabajo no revisados

## Consideraciones importantes
1. Los proyectos usan '**pylint**' y '**eslint**' para detectar errores en el código y asegurar que  siga estándares de codificación, por lo que la verificación de estos productos de trabajo usando debe atenerse **solamente a aspectos que dichas herramientas no cubren.** 
2. Los equipos pueden añadir o cambiar componentes del entorno de verificación recomendado en la <a href="">**Guía del Entorno de Verificación**</a> dependiendo de sus necesidades.

## Proceso
<table>
  <thead>
    <tr>
      <th>Fase</th>
      <th>Actividades</th>
      <th>Encargado</th>
      <th>Áreas CMMI</th>
    </tr>
  </thead>
  <tbody>
      <tr>
      <td>Selección</td>
      <td>Selecciona los archivos de código a verificar. </td>
      <td>Pareja solicitante</td>
      <td>REQM, VER</td>
    </tr>
    <tr>
      <td rowspan="3">Preparación</td>
      <td>Comunica al equipo que tienes código para verificar. </td>
      <td>Pareja solicitante</td>
      <td rowspan="3">VER</td>
    </tr>
    <tr>
      <td>Decide quiénes realizarán la Pair Review.
      </td>
      <td>Equipo</td>
    </tr>
    <tr>
      <td>Prepara el entorno de verificación.
      <p>(<strong>Consulta la <a href="https://github.com/novaDepto/Nova/wiki/Gu%C3%ADa-de-entorno-de-verificaci%C3%B3n">Guía del Entorno de Verificación<strong></a> para más información).</p>
      </td>
      <td>Pareja verificadora</td>
    </tr>
    <tr>
      <td rowspan="3">Verificación</td>
      <td>Realiza la verificación del código siguiendo el <a href="https://docs.google.com/spreadsheets/d/1WccrRu2iMWX6y1USG_k5nElfajfu6ACS1L11QNGuKN0/edit#gid=39101311"><strong>Reporte de Verificación</strong></a>.</td>
      <td rowspan="3">Pareja de verificación</td>
      <td rowspan="3">VER</td>
    </tr>
    <tr>
      <td>Documenta qué criterios de código son aprobados.
      </td>
    </tr>
    <tr>
      <td>Documenta qué criterios de código necesitan corregirse.</td>
    </tr>
    <tr>
      <td rowspan="3">Comunicación</td>
      <td>Comunica a la pareja solicitante los resultados de la verificación. </td>
      <td rowspan="3">Pareja de verificación</td>
      <td rowspan="3">VER</td>
    </tr>
    <tr>
      <td>Indica los criterios de código que deben corregirse.
      </td>
    </tr>
    <tr>
      <td>Guarda el Reporte de Verificación en el lugar correspondiente.</td>
    </tr>
    <tr>
      <td>Seguimiento</td>
      <td>La pareja solicitante puede pedir una nueva verificación <strong>siempre y cuando hayan realizado las correcciones registradas en la  anterior.</strong></td>
      <td>Pareja solicitante</td>
      <td>VER, PMC</td>
    </tr>
    
  </tbody>
</table>

## Salidas
1. Reporte de Verificación
2. Producto de trabajo verificado

## Métricas
1. Tasa de aceptación de productos
2. Criterios de código menos aceptados

***
versión 0.1a
