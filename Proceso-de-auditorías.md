## Responsables

Nombre     | Rol
-----------|------------------
Daniel Elias| Dueño del proceso
Javier Mendez| Autor
Lisieux Serrano| Autor
Carlos Becerra | Autor

## Objetivo
Definir el proceso para planear, agendar y ejecutar una auditoría, así como informar a los involucrados sobre los resultados de esta evaluación objetiva, las no conformidades y la resolución de las mismas. Esto con el fin de:

1. Brindar un mecanismo para evaluar objetivamente procesos y productos de trabajo.
2. Encontrar y comunicar las no conformidades encontradas en los procesos y productos de trabajo realizados.
3. Asegurar la resolución de las no conformidades encontradas en la auditoría.
4. Asegurar la calidad de los procesos y productos de trabajo del departamento.

## Entradas
1. [Plantilla de auditorías](https://docs.google.com/document/d/1XE7jKV1uRT5Wy6qZtacqW8aur6fFNJAW1batOYKg3No/edit)
2. [Control de auditorías y no conformidades](https://docs.google.com/spreadsheets/d/1XoZIS9bOkvG00JPGWq24f4WuB-bdESkBypvnKAiDHEM/edit#gid=0)

## Proceso

<table>
  <thead>
    <tr>
      <th>Fase</th>
      <th>Actividades</th>
      <th>Encargado</th>
      <th>Áreas del CMMI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">Análisis</td>
      <td>Definir el objetivo de la auditoría</td>
      <td>Personas auditando</td>
      <td>PPQA, CM</td>
    </tr>
    <tr>
      <td>Definir la <a href="https://github.com/novaDepto/Nova/wiki/Politica-de-lineas-base">línea base </a> a ser auditada</td>
      <td>Personas auditando</td>
      <td>PPQA, CM</td>
    </tr>
    <tr>
      <td>Definir los procesos y/o productos de trabajo a ser auditados. Estos deben de ser <a href="https://github.com/novaDepto/Nova/wiki/Politica-de-elementos-de-la-configuracion"> elementos de la configuración </a> </td>
      <td>Personas auditando</td>
      <td>PPQA, CM</td>
    </tr>
    <tr>
      <td>Definir el nombre de la auditoría</td>
      <td>Personas auditando</td>
      <td>PPQA, CM</td>
    </tr>
    <tr>
    <tr>
      <td rowspan="1">Diseño de rúbricas</td>
      <td>Definir una rúbrica o checklist de lo que debe cumplir cada proceso o producto a evaluar. En caso de ser un proceso se debe seguir la <a href="https://docs.google.com/spreadsheets/d/1QJwNEmHbWxy-EtVOlrlfLJfTQPJb6k8ikunp39Yk8-Y/edit#gid=0"> Checklist de institucionalización de procesos </a> En caso de ser un producto como código fuente se debe de seguir el <a href="https://github.com/novaDepto/Nova/wiki/Proceso-de-Pair-Review"> Proceso de Pair Review </a></td> 
      <td>Personas auditando</td>
      <td>PPQA, REQM, CM, VER</td>
    </tr>
    <tr>
      <td rowspan="2">Calendarización de la auditoría</td>
      <td>Agregar bloques de tiempo en el calendario para las auditorías. Seguir la <a href="https://github.com/novaDepto/Nova/wiki/Gu%C3%ADa-para-agendar-eventos">guía para agendar eventos</a></td>
      <td>Personas auditando</td>
      <td>PPQA, CM</td>
    </tr>
    <tr>
    <td>Las auditorías pueden realizarse directamente sobre los productos, pero en caso de necesitar más información sobre los mismos se puede citar a los dueños o responsables para que estén presentes durante la auditoría. En el caso de la auditoría de procesos se recomienda citar a los dueños y responsables. </a></td>
      <td>Encargados del proceso/producto</td>
      <td>PPQA, CM</td>
    <tr>
      <td rowspan="2">Realización de la Auditoría</td>
      <td>Inspeccionar los procesos o productos con base en las checklists correspondientes. </td>
      <td>Personas auditando</td>
      <td>PPQA, CM</td>
    </tr> 
    </tr>
    <tr>
      <td>Registrar las no conformidades que se van encontrando en la hoja de no conformidades de la auditoría que se encuentra en el documento de <a href="https://docs.google.com/spreadsheets/d/1XoZIS9bOkvG00JPGWq24f4WuB-bdESkBypvnKAiDHEM/edit#gid=0"> Control de auditorías y no conformidades</a> </td>
      <td>Personas auditando</td>
      <td>PPQA, CM</td>
    </tr>
    <tr>
      <td>Revisión</td>
      <td>
        Escribir las recomendaciones que se le darán a los encargados del producto/proceso auditado
      </td>
      <td>Personas auditando</td>
      <td>PPQA, CM</td>
    </tr>
    <tr>
      <td>Verificación</td>
      <td>Revisar el documento generado asegurándose que:
      <ul>
        <li>El documento de auditoría tenga todas sus secciones completadas.</li>
        <li>El documento no tenga faltas de ortografía o redacción.</li>
        <li>Que las no conformidades encontradas hayan sido registradas.</li>
      </ul></td>
      <td>Personas auditando</td>
      <td>PPQA, CM</td>
    </tr>
    <tr>
      <td rowspan="2">Comunicación de resultados de la auditoría</td>
      <td>Enviar y notificar por Slack a los encargados del producto/proceso la entrega de resultados</td>
      <td>Personas auditando</td>
      <td>PPQA</td>
    </tr>
    <td>En caso de presentar no conformidades, agendar una fecha límite para la resolución de las mismas.</td>
      <td>Personas auditando</td>
      <td>PPQA, CM</td>
    </tr>
    <tr>
      <td rowspan="2">Seguimiento</td>
      <td>Corregir las no conformidades encontradas para la fecha definida para su corrección</td>
      <td>Encargados del producto/proceso</td>
      <td>PPQA, CM</td>
    </tr>
    <tr>
      <td>Notificar de los cambios realizados y añadir los datos a las estadísticas pertinentes</td>
      <td>Encargados del producto/proceso</td>
      <td>PPQA, MA, CM</td>
    </tr>
  </tbody>
</table>

## Salidas
1. Documento de auditoría completo con los resultados de la misma y las no conformidades encontradas.
2. Documento de gestión de no conformidades actualizado.
3. Resolución de no conformidades

## Métricas
1. Registro del tiempo tomado tras realizar todo el proceso para una auditoría, incluyendo todas las fases del proceso.
2. No-conformidades registradas y categorizadas

## Glosario
1. No conformidad: se refiere a una desviación en la ejecución de un proceso o no cumplir con uno de los puntos de las checklists de los productos.

***
versión 2.0