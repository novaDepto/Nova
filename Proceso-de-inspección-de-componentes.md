## Responsables

| Nombre | Rol|
| -------- | -------- |
| Dan     | Dueño del proceso     |
| Lisieux | Autor|

## Objetivo
Realizar una inspección al código fuente de un componente de un proyecto de software, de acuerdo a una checklist de código, para así encontrar posibles defectos y dar paso a su resolución

## Entradas
1. [Reporte de inspección](https://docs.google.com/spreadsheets/d/1c6FRhE9Fm7sWP4pWwGucm6aBd6LtCEgJ2KAb7Hz2inY/edit?usp=sharing)
2. Componente a ser inspeccionado

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
      <td rowspan="6">Preparación</td>
      <td>Copiar y pegar el <a href="https://docs.google.com/spreadsheets/d/1c6FRhE9Fm7sWP4pWwGucm6aBd6LtCEgJ2KAb7Hz2inY/edit?usp=sharing">Reporte de inspección</a> a la carpeta de la iteración actual </td>
      <td>Miembro del departamento</td>
      <td>VER, PPQA</td>
    </tr>
    <tr>
      <td>Definir roles y anotar responsables para:
        <li> Responsable del componente
        <li> Un moderador
        <li> La persona que tomará el tiempo
        <li> Inspectores </td>
      <td>Miembro del departamento</td>
      <td>VER, PPQA</td>
    </tr>
    <tr>
      <td> Agendar la sesión de inspección utilizando la <a href="https://github.com/novaDepto/Nova/wiki/Gu%C3%ADa-para-agendar-eventos">Guía para agendar evento</a> </td>
      <td>Miembro del departamento</td>
      <td>VER, PPQA</td>
    </tr>
    <tr>
      <td> Identificar los archivos de código que corresponden al componente  </td>
      <td>Responsable del componente </td>
      <td>VER, PPQA </td>
    </tr>
    <tr>
      <td> Definir la unidad de medida del tamaño del componente y su tamaño. Este corresponde al total de líneas de código que corresponden al componente </td>
      <td>Responsable del componente</td>
      <td>VER PPQA</td>
    </tr>
    <tr>
      <td> Preparar el componente poniendo a disposición de los inspectores todos los archivos necesarios para correr el componente e inspeccionarlo</td>
      <td>Responsable del componente</td>
      <td>VER, PPQA</td>
    </tr>
    <tr>
      <td rowspan="4">Inspección</td>
      <td> El responsable del componente, inspectores, moderador y persona que toma el tiempo se reunen en la fecha y hora acordada</td>
      <td>Moderador</td>
      <td>VER, PPQA</td>
    </tr>
    <tr>
      <td> Los inspectores abren la <a href="https://docs.google.com/spreadsheets/d/1E_izcL8uxgLuaBweOwx9BvzihSYBKjuGjGuQ7ilZv24/edit#gid=1351407982"> Checklist de código </a> , <a href="https://docs.google.com/spreadsheets/d/1c6FRhE9Fm7sWP4pWwGucm6aBd6LtCEgJ2KAb7Hz2inY/edit?usp=sharing"> Reporte de inspección </a>y los archivos de código del componente que será inspeccionado. </td>
      <td>Moderador, persona que toma el tiempo</td>
      <td>VER, PPQA</td>
    </tr>
    <tr>
      <td> El moderador indica el inicio de la inspección y la persona que toma el tiempo comienza a medirlo. Cuando el tiempo termine, la persona encargada de medir el tiempo avisará a todos los involucrados en la inspección.</td>
      <td>Moderador, persona que toma el tiempo</td>
      <td>VER, PPQA</td>
    </tr>
    <tr>
      <td> Por cada rubro de la checklist de código, los inspectores leen el código del componente y registran los defectos que van encontrando en su hoja correspondiente del <a href="https://docs.google.com/spreadsheets/d/1c6FRhE9Fm7sWP4pWwGucm6aBd6LtCEgJ2KAb7Hz2inY/edit?usp=sharing">Reporte de inspección</a> </td>
      <td>Moderador, persona que toma el tiempo</td>
      <td>VER, PPQA</td>
    </tr>
    <tr>
      <td rowspan="2">Discusión </td>
      <td> Al terminar el tiempo de inspección, se copian los defectos encontrados por cada inspector a una sola hoja de log de defectos en el mismo reporte de inspección. Se anota la persona que encontró el defecto y si otro inspector también lo encontró. </td>
      <td>Moderador</td>
      <td>VER, PPQA</td>
    </tr>
    <tr>
      <td> Entre los involucrados de la inspección se discute si cada defecto encontrado es en realidad un defecto. Se revisa la severidad, el tipo de defecto </td>
      <td>Involucrados en la inspección</td>
      <td>VER, PPQA</td>
    </tr>
    <tr>
      <td rowspan="4">Finalización</td>
      <td> Se registra el total de defectos encontrados. En la columna de incidencias se anota cuántos inspectores encontraron el mismo defecto</td>
      <td>Moderador</td>
      <td>VER, PPQA, MA</td>
    </tr>
    <tr>
      <td> En la hoja de resumen de inspección se llenan las métricas de acuerdo a los datos obtenidos de la inspección</td>
      <td>Moderador</td>
      <td>VER, PPQA, MA</td>
    </tr>
    <tr>
      <td> Se utiliza la técnica catch-recatch para calcular cuántos defectos se estima que hay en el producto con la fórmula: (A*B)/C</td>
      <td>Moderador</td>
      <td>VER, PPQA, MA</td>
    </tr>
    <tr>
      <td> Se calcula la densidad de defectos (KLOC)</td>
      <td>Moderador</td>
      <td>VER, PPQA, MA</td>
    </tr>
    <tr>
      <td rowspan="2">Comunicación</td>
      <td> Los defectos se anotan en el <a href="https://docs.google.com/spreadsheets/d/1RpU0kmGCRSH35LN6ZTPPkAXsNAeiS_OLvBdqoJsp060/edit#gid=868244246"> log de defectos del equipo  </a>que es dueño del componente</td>
      <td>Moderador</td>
      <td>VER, PPQA, MA</td>
    </tr>
    <tr>
      <td> Se le comunica al PO, AO y TL del equipo dueño del componente para que el equipo pase a su corrección </td>
      <td>Moderador</td>
      <td>Áreas CMMI</td>
    </tr>
    <tr>
      <td rowspan="2">Actualización de checklists</td>
      <td> Con los nuevos defectos y métricas se puede dar paso a actualizar las <a href="https://docs.google.com/spreadsheets/d/1E_izcL8uxgLuaBweOwx9BvzihSYBKjuGjGuQ7ilZv24/edit#gid=1351407982"> Checklists de verificación </a>checklists de verificación para detectar estos mismos defectos por los mismos desarrolladores del componente </td>
      <td>Moderador</td>
      <td>VER, PPQA, MA</td>
    </tr>
    <tr>
      <td> Se le comunica al PO, AO y TL del equipo dueño del componente para que el equipo pase a su corrección </td>
      <td>Moderador</td>
      <td>Áreas CMMI</td>
    </tr>
  </tbody>
</table>

## Salidas
1. Reporte de inspección lleno
2. Log de defectos del equipo desarrollador del componente actualizado
3. Checklists de verificación actualizadas

## Métricas
1. Número total de defectos
2. Densidad estimada de defectos (KLOC)
3. Número de defectos estimados en el producto
4. Esfuerzo total de la inspección

***
versión 0.1b