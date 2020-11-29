## Responsables

| Nombre | Rol|
| -------- | --------------------- |
| Dan      | Dueño del proceso     |
| Lisieux  | Autor                 |

## Objetivo
Realizar una inspección al código fuente de un componente de un proyecto de software, de acuerdo a una checklist de código, para así encontrar posibles defectos y dar paso a su resolución

## Entradas
1. [Reporte de inspección de código](https://docs.google.com/spreadsheets/d/1MRa1gjtF_DUqVybsPa9u1NTLnkQr5NAtyJtS0Q0poz4/edit#gid=0)
2. Componente a inspeccionar
3. [Guía de entorno de verificación](https://github.com/novaDepto/Nova/wiki/Gu%C3%ADa-de-entorno-de-verificaci%C3%B3n)

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
      <td rowspan="8">Preparación</td>
      <td>Copia y pega el <strong><a href="https://docs.google.com/spreadsheets/d/1MRa1gjtF_DUqVybsPa9u1NTLnkQr5NAtyJtS0Q0poz4/edit#gid=0">Reporte de inspección</a></strong>.</td>
      <td rowspan="3">Todo el equipo</td>
      <td rowspan="8">VER, PPQA</td>
    </tr>
    <tr>
      <td>Selecciona a los integrantes del departmaneto que realizarán la inspección.</td>
    </tr>
    <tr>
      <td>Define los roles que tomará cada integrante durante la inspección.</td>
    </tr>
    <tr>
      <td>Agenda la inspección siguiendo la <strong><a href="https://github.com/novaDepto/Nova/wiki/Gu%C3%ADa-para-agendar-eventos">Guía para agendar eventos</a></strong>.</td>
      <td>Miembro del departamento</td>
    </tr>
    <tr>
      <td>En la hoja <strong>Resumen</strong>, escribe los componentes a inspeccionar.</td>
      <td rowspan="4">Autor del código</td>
    </tr>
    <tr>
      <td>Identifica los archivos que corresponden al componente a inspeccionar.</td>
    </tr>
    <tr>
      <td>Escribe las líneas de código y Agile Points que conforman el componente.</td>
    </tr>
    <tr>
      <td>Entrega a los inspectores los archivos necesarios para inspeccionar el componente <strong>(Consulta las Precondiciones en la <a href="https://github.com/novaDepto/Nova/wiki/Gu%C3%ADa-de-entorno-de-verificaci%C3%B3n">Guía del Entorno de Verificación)</a><strong>.</td>
    </tr>
    <tr>
      <td rowspan="5">Inspección</td>
      <td>Asiste a la sesión de inspección.</td>
      <td>Integrantes de la inspección</td>
      <td rowspan="5">VER, PPQA</td>
    </tr>
    <tr>
      <td>Abre el <strong><a href="https://docs.google.com/spreadsheets/d/1MRa1gjtF_DUqVybsPa9u1NTLnkQr5NAtyJtS0Q0poz4/edit#gid=0"> Reporte de inspección </a></strong> y los archivos de código del componente a inspeccionar. </td>
      <td>Inspectores</td>
    </tr>
    <tr>
      <td>Indica el inicio de la inspección.</td>
      <td>Moderador</td>
    </tr>
    <tr>
      <td>Mide el tiempo de la inspección. Cuando el tiempo termine, avisa a los demás integrantes de la inspección.</td>
      <td>Asistente</td>
    </tr>
    <tr>
      <td> Por cada rubro de la hoja <strong>Checklist de inspección</strong>, lee el código del componente y registra los defectos que vayas encontrando en tu <strong>hoja correspondiente</strong>.</td>
      <td>Inspectores</td>
    </tr>
    <tr>
      <td rowspan="2">Discusión</td>
      <td> Al terminar el tiempo de la inspección, copia los defectos encontrados por cada inspector en la hoja <strong>Historial</strong>. Anota la persona que encontró el defecto y revisa si otros inspectores también lo encontraron. </td>
      <td>Moderador</td>
      <td rowspan="2">VER, PPQA</td>
    </tr>
    <tr>
      <td>Discute si cada defecto encontrado es un defecto, y determina su tipo y severidad.</td>
      <td>Inspectores</td>
    </tr>
    <tr>
      <td rowspan="4">Finalización</td>
      <td>Registra el total de defectos encontrados. En la columna <em># Incidencias</em>, anota cuántos inspectores encontraron el mismo defecto.</td>
      <td rowspan="4">Moderador</td>
      <td rowspan="4">VER, PPQA, MA</td>
    </tr>
    <tr>
      <td>En la hoja <strong>Resumen</strong>, rellena las métricas de la inspección.</td>
    </tr>
    <tr>
      <td>Estima cuántos defectos hay en el producto con la técnica de Catch-Recatch: <strong>(A*B)/C</strong-></td>
    </tr>
    <tr>
      <td>Calcula la densidad de defectos (KLOC).</td>
    </tr>
    <tr>
      <td rowspan="2">Comunicación</td>
      <td>Pasa los defectos al <strong><a href="https://docs.google.com/spreadsheets/d/1RpU0kmGCRSH35LN6ZTPPkAXsNAeiS_OLvBdqoJsp060/edit#gid=868244246">log de defectos</a></strong> de tu equipo.</td>
      <td>Autor del código</td>
      <td rowspan="2">VER, PPQA, MA</td>
    </tr>
    <tr>
      <td>Comunica los resultados al PO, AO y TL del equipo dueño del componente para que se corrijan los defectos.</td>
      <td>Moderador</td>
    </tr>
    <tr>
      <td rowspan="2">Actualización de Checklist</td>
      <td> Determina si se deben actualizar las checklists del <strong><a href="https://docs.google.com/spreadsheets/d/1c6FRhE9Fm7sWP4pWwGucm6aBd6LtCEgJ2KAb7Hz2inY/edit#gid=1461386475"> Reporte de Pair Review </a></strong> para que el equipo desarrollador detecte los defectos en un futuro.</td>
      <td rowspan="2">Moderador</td>
      <td rowspan="2">VER, PPQA, MA, PMC</td>
    </tr>
     <tr>
      <td> Determina si se deben actualizar las checklists del <strong><a href="https://docs.google.com/spreadsheets/d/1MRa1gjtF_DUqVybsPa9u1NTLnkQr5NAtyJtS0Q0poz4/edit#gid=0"> Reporte de inspección de código </a></strong> para futuras inspecciones.</td>
    </tr>
  </tbody>
</table>

## Salidas
1. Reporte de inspección actualizado
2. Log de defectos del equipo desarrollador actualizado
3. Checklist de inspección actualizada

## Métricas
1. Número total de defectos
2. Densidad estimada de defectos (KLOC)
3. Número de defectos estimados en el producto
4. Esfuerzo total de la inspección

***
Versión 1.1
