## Responsables
Nombre     | Rol
-----------|------------------
Raymundo   | Dueño de la guía
Charlie    | Autor

## Objetivo
1. Asegurar la preparación del entorno de verificación.

## Inspección
<table>
  <thead>
    <tr>
      <th>Atributo</th>
      <th>Descripción</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Petición</td>
      <td>Programada.</td>
    </tr>
    <tr>
      <td>Input</td>
      <td>Sesión de inspección de código.</td>
    </tr>
    <tr>
      <td rowspan="3">Precondiciones</td>
      <td>El código debe estar terminado y funcionando.</td>
    </tr>
    <tr>
      <td>Los inspectores deben tener acceso al repositorio del proyecto.</td>
    </tr>
    <tr>
      <td>Los inspectores deben tener acceso a la matriz de trazabilidad.</td>
    </tr>
    <tr>
      <td>Herramienta</td>
      <td><strong><a href="https://docs.google.com/spreadsheets/d/1MRa1gjtF_DUqVybsPa9u1NTLnkQr5NAtyJtS0Q0poz4/edit#gid=0">Reporte de inspección de código</strong>.</td>
    </tr>
    <tr>
      <td rowspan="2">Actividades</td>
      <td>Revisar el código siguiendo la Checklist de Inspección.</td>
    </tr>
    <tr>
      <td>Documentar los defectos encontrados en el código.</td>
    </tr>
    <tr>
      <td rowspan="2">Output</td>
      <td>Resumen de la inspección</td>
    </tr>
    <tr>
      <td>Historial de defectos</td>
    </tr>
    <tr>
      <td>Postcondiciones</td>
      <td>Los defectos deben documentarse en el Backlog de defectos.</td>
    </tr>
    <tr>
      <td rowspan="5">Roles</td>
      <td><strong>Autor del código</strong> = Atiende las dudas de los inspectores.</td>
    </tr>
    <tr>
      <td><strong>Moderador</strong> = Dirige el curso de la inspección.</td>
    </tr>
    <tr>
      <td><strong>Asistente</strong> = Cronometra el tiempo de la inspección.</td>
    </tr>
    <tr>
      <td><strong>Inspector</strong> = Rellena el Reporte de inspección.</td>
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
      <td>Petición</td>
      <td>A demanda.</td>
    </tr>
    <tr>
      <td>Input</td>
      <td>Pull Request en repositorio del equipo</td>
    </tr>
    <tr>
      <td rowspan="3">Precondiciones</td>
      <td>El código debe estar terminado y funcionando.</td>
    </tr>
    <tr>
      <td>La pareja verificadora debe tener acceso al repositorio del proyecto.</td>
    </tr>
    <tr>
      <td>La pareja verificadora debe tener acceso a la matriz de trazabilidad.</td>
    </tr>
    <tr>
      <td>Herramienta</td>
      <td><strong><a href="https://docs.google.com/spreadsheets/d/1c6FRhE9Fm7sWP4pWwGucm6aBd6LtCEgJ2KAb7Hz2inY/edit#gid=1461386475">Reporte de Pair Review</strong>.</td>
    </tr>
    <tr>
      <td rowspan="2">Actividades</td>
      <td>Revisar el código siguiendo la Checklist de Frontend y Backend.</td>
    </tr>
    <tr>
      <td>Documentar los defectos encontrados en el código.</td>
    </tr>
    <tr>
      <td rowspan="2">Output</td>
      <td>Reporte de Pair Review rellenado</td>
    </tr>
    <tr>
      <td>Pull Request aprobado/rechazado</td>
    </tr>
    <tr>
      <td>Postcondiciones</td>
      <td>Los defectos deben documentarse en el Backlog de defectos.</td>
    </tr>
    <tr>
      <td>Roles</td>
      <td>La pareja decide si revisar y documentar a la vez o asignarse roles para realizar cada una.</td>
  </tbody>
</table>

**NO SE RECOMIENDA** verificar código de diferentes historias de usuario porque puede generar confusión y un desarrollo en cascada que va en contra de los principios del desarrollo ágil.

***
Versión 1.2
