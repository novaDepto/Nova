## Responsables

| Nombre   | Rol               |
| -------- | ----------------- |
| Alexis | Dueño del proceso |
| Cristian | Autor             |
| Charlie     | Autor             |

## Objetivos

Desarrollar entendimiento a las necesidades y los requerimientos de quienes tengan la tarea de proveer los requerimientos del proyecto.

## Entradas

1. Listado de necesidades, pain points, del cliente
2. [Proceso para plan de Involucramiento de Stakeholders](https://github.com/novaDepto/Nova/wiki/Proceso-para-plan-de-Involucramiento-de-Stakeholders)

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
      <td rowspan="3">Identificación</td>
      <td>En el <a href="https://docs.google.com/spreadsheets/d/1o6jLgBaUGFCco-8gIZqd8Ng3zqUKfJYZudfaI9Bqu-0/edit#gid=846530107">plan de invoucramiento de stakeholders</a> identifica en la columna "proveedor de requisitos" a todos aquellos involucrados en el proyecto que sean los más apropiados para ser los proveedores de requisitos tomando como base los siguientes criterios.
      <ul>
        <li>Es quien da seguimiento y aprobará el proyecto al finalizar.</li>
        <li>Tiene la aprobación por parte de quien aprobará el proyecto al finalizar. </li>
        <li>Cuenta con un amplio conocimiento del uso que se la dará a la solución.</li>
        <li>Tiene conocimeinto detallado acerca del funcionamiento del negocio del socio formador.
        </li>
        <li>Tiene conocimiento detallado de las principales dolencias del socio formador o de su negocio.</li>
      </ul>
      <strong>Se sugiere que el PO sea el proveedor de requisitos a nombre del departamento.</strong>
      <td rowspan="2">PO</td>
      <td rowspan="2">REQM, VAL</td>
      </td>
    </tr>
    <tr>
      <td>Identifica las necesidades y dolencias princpales en la <a href="https://docs.google.com/spreadsheets/d/1o6jLgBaUGFCco-8gIZqd8Ng3zqUKfJYZudfaI9Bqu-0/edit#gid=1630941258">matriz de necesidades</a>.</td>
    </tr>
    <tr>
      <td>Identifica dependencias entre las necesidades.</td>
      <td rowspan="5">PO, TL</td>
      <td rowspan="4">REQM, PP, VAL</td>
    </tr>
    <tr>
      <td rowspan="4">Analisis</td>
      <td>Prioriza las necesidades que aporten más valor.</td>
    </tr>
      <tr>
      <td>Analiza si  la necesidad es posible de solucionar o existe un método alternativo.</td>
    </tr>
    <tr>
      <td>Escoge una necesidad y enlista los requisitos funcionales/no funcionales en la herrmienta utilizada (hoja de cálculo, Jira, Github, etc) por el equipo para monitorear el proyecto.
      </td>
    </tr>
    <tr>
      <td>Identifica y analiza los posibles riesgos de aceptar algun requisito siguiendo el <a href="https://github.com/novaDepto/Nova/wiki/Proceso-de-gesti%C3%B3n-de-riesgos">proceso de gestión de riesgos</a>.
      </td>
      <td rowspan="1">REQM, PP, RSKM, VAL</td>
    </tr>
    <tr>
      <td rowspan="1">Revisión de requisitos</td>
      <td>Comunica con el equipo y decidan si se acepta o no. Para aceptar un requisito, verifica que el requisito:
        <ul>
            <li>Aporte valor a la solución</li>
            <li>Es necesario para cumplir los objetivos del proyecto</li>
            <li>Es realizable de acuerdo con las habilidades técnicas del equipo</li>
            <li>Es claro y no se presta a distintas interpretaciones</li>
            <li>No compromete la salud del equipo</li>
            <li>No entra en conflicto con otro requisito</li>
            <li>Será posible determinar si fue satisfecho</li>
          </ul>
      </td>
      <td rowspan="1">PO, TODOS</td>
      <td rowspan="1">REQM, VAL</td>
    </tr>
	 <tr>
      <td rowspan="1">Aceptación de requisitos</td>
      <td>
       Verifica la lista de requisitos con los stakeholders, explicando las necesidades que se solucionan. (De ser necesario un cambio, ejecuta este proceso nuevamente)
      </td>
      <td rowspan="1">PO, TODOS</td>
      <td rowspan="1">REQM, VAL</td>
    </tr>
  </tbody>
</table>

## Salidas
1) Lista de Requisitos funcionales/No funcionales

## Métricas
1) Valor Ganado de la Plantilla de Planeación-Monitoreo de la Iteración.

***
versión 1.3

