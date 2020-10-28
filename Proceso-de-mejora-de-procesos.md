## Responsables
Nombre     | Rol
-----------|------------------
Raymundo   | Dueño del proceso
Daniel Elias  | Autor

## Objetivo
1. Permitir la realización de cambios a los procesos para mejorar la forma de trabajo del departamento utilizando los principios de mejora continua: mejorar el flujo de valor, reducir los ciclos de retroalimentación y la experimentación

## Entradas
1. Un proceso en línea base de la wiki del departamento

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
      <td rowspan="3"> Asignación </td>
      <td>¿Eres el dueño/responsable del documento?</td>
      <td rowspan="3">Variable</td>
      <td>RSKM</td>
    </tr>
    <tr>
      <td>a) <strong>Sí</strong> = Realiza el cambio al documento.</td>
      <td>CM</td>
    </tr>
    <tr>
      <td>b) <strong>No</strong> = Avanza a la siguiente fase.</td>
      <td>OPF</td>
    </tr>
    <tr>
      <td rowspan="5">Proposición</td>
      <td>Comunica al dueño del proceso los cambios a implementar.</td>
      <td rowspan="3">Interesados en el cambio</td>
      <td rowspan="5">CM, OPF, PPQA</td>
    </tr>
    <tr>
      <td>Hacer el cambio propuesto al proceso y enviarlo como <strong> Pull Request </strong> siguiendo el <a href="https://github.com/novaDepto/Nova/wiki/Proceso-de-modificacion-de-linea-base"> Proceso de modificación de línea base</a> <strong>. También en tu Pull Request incluye el principio de mejora continua que se está aplicando con los cambios. </td>
    <tr>
      <td>Selecciona un grupo o muestra de personas que utilizarán el proceso con el cambio.</td>
    </tr>
    <tr>
      <td>Supervisa la ejecución del cambio en el grupo o muestra de personas.</td>
      <td rowspan="2">Encargados de OPF</td>
    </tr>
    <tr>
      <td>Evalúa los resultados obtenidos del cambio.</td>
    </tr>
    <tr>
      <td rowspan="1">Revisión</td>
      <td> El <a href="https://github.com/novaDepto/Nova/wiki/Politica-de-Configuration-Control-Board"> Configuration Control Board </a> pasa a la revisión del Pull Request utilizando el <a href="https://github.com/novaDepto/Nova/wiki/Proceso-para-institucionalizar-procesos-gu%C3%ADas-y-pol%C3%ADticas"> Proceso para Institucionalizar Procesos, Guías y Políticas.</a> y el <a href="https://github.com/novaDepto/Nova/wiki/Proceso-de-modificacion-de-linea-base"> Proceso de modificación de línea base</a> </td>
      <td rowspan="1">Configuration Control Board</td>
      <td rowspan="1">CM, PPQA</td>
    </tr>
    <tr>
      <td rowspan="2">Resolución</td>
      <td> Si el cambio es aprobado por los encargados de OPF Y el Configuration Control Board, entonces el Configuration Control Board enviará el proceso con los cambios a línea base de la wiki del departamento. Además se deberá de poner en comentario en el Pull Request nombres de los que revisaron y razón de la aprobación </td>
      <td rowspan="2">Configuration Control Board</td>
      <td rowspan="2">CM, OPF</td>
    </tr>
    <tr>
      <td> Si el cambio es rechazado, entonces se deberá documentar la razón en un comentario en el Pull Request especificando: nombres de los que revisaron y razón de rechazo. </td>
    </tr>
  </tbody>
</table>

## Salidas
En caso de aprobación:
1. Proceso en línea base de la wiki del departamento con las mejoras incluidas e institucionalizadas 

En caso de rechazo:
1. El registro de la razón del rechazo en un comentario en el Pull Request cerrado por el Configuration Control Board

## Métricas
1. Promedio de institucionalización de procesos.

***
versión 0.2b