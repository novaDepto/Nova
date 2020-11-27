## Responsables

| Nombre  | Rol   |
|---------|-------|
| Juan Alcántara| Dueño del proceso |
| Juan Alcántara| Autor |

## Objetivo
Mantener una gestión y control de los cambios que sufren las [líneas base](https://github.com/novaDepto/Nova/wiki/Politica-de-lineas-base) día con día, para que el departamento tenga fácil acceso a las últimas versiones de los [elementos de la configuración](https://github.com/novaDepto/Nova/wiki/Politica-de-elementos-de-la-configuracion)

## Entradas
1. Línea base
2. Un cambio a uno de los elementos de la configuración de la línea base

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
      <td>Análisis</td>
      <td> Identifica los archivos que van a sufrir un cambio para incluirlos
      en la solicitud y utilizando la <a
      href="https://github.com/novaDepto/Nova/wiki/Gu%C3%ADa-de-versionado">
      Guía de versionado</a> identifica los cambios de versión
      necesarios.</td>
      <td>Autor del cambio</td>
      <td>CM, REQM</td>
    </tr>
    <tr>
      <td> Implementación </td>
      <td> Crea un <strong>Pull Request</strong> hacia el repositorio de los
      archivos afectados. En caso de ser un repositorio de código sigue la <a
      href="https://github.com/novaDepto/Nova/wiki/Gu%C3%ADa-de-Nova-Flow">
      Guía de NovaFlow </a> y en caso de ser un repositorio de documentación,
      e.g. Wiki, sigue la <a
      href="https://guides.github.com/introduction/flow/">Guía de GitHub
      Flow</a>. Si es un cambio a un proceso sigue el <a href="https://github.com/novaDepto/Nova/wiki/Proceso-de-mejora-continua"> Proceso de Mejora Continua </a> </td>
      <td> Autor del cambio</td>
      <td> CM, REQM, RM</td>
    </tr>
    <tr>
      <td rowspan="2"> Verificación y validación </td>
      <td>En el <strong> Pull Request </strong> describe la justificación para
      realizar el cambio.</td>
      <td> Autor del Cambio </td>
      <td> CM, REQM </td>
    </tr>
    <tr>
      <td>Notifica a tu equipo de la nueva solicitud para que puedan apoyarte
      con sus <em>reviews</em>. </td>
      <td>Autor del cambio</td>
      <td>CM, REQM, VAL, VER </td>
    </tr>
    <tr>
      <td> Corrección y Mejora </td>
      <td>Realiza las modificaciones necesarias a partir de los
      <em>reviews</em> de tus compañeros.</td>
      <td>Autor del cambio</td>
      <td>CM, REQM, VAL, VER</td>
    </tr>
    <tr>
      <td rowspan="2"> Publicación </td>
      <td>Haz <em>merge</em> de los cambios.</td>
      <td>Autor del cambio o team member</td>
      <td>CM, REQM, VAL, VER</td>
    </tr>
    <tr>
      <td>Comunica el cambio al equipo involucrado
      <td>Autor del cambio</td>
      <td>CM, REQM, PP</td>
    </tr>
  </tbody>
</table>

## Salidas
1. **Pull Request** aprobado y _mergeado_.
2. Línea base con sus modificaciones.

## Métricas
1. Tiempo de revisión de cambios.
2. _Breakdown_ por categoría de cambios, i.e. si fueron _fixes_, adiciones,
eliminaciones, etc.

***
versión 1.0