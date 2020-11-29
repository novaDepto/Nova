## Responsables
Nombre     | Rol
-----------|------------------
Charlie    | Dueño del proceso
Lisieux    | Autor
Raymundo   | Autor

## Objetivos
1. Verificar el código realizado antes de mergearlo a develop
2. Asegurar la calidad de los productos de trabajo del proyecto

## Entradas
1. Pull Request a develop

## Consideraciones importantes
1. Los proyectos usan '**pylint**' y '**eslint**' para detectar errores en el código y asegurar que  siga estándares de codificación, por lo que la verificación de estos productos de trabajo usando debe atenerse **solamente a aspectos que dichas herramientas no cubren.** 
2. Los equipos pueden añadir o cambiar componentes del entorno de verificación recomendado en la <a href="https://github.com/novaDepto/Nova/wiki/Gu%C3%ADa-de-entorno-de-verificaci%C3%B3n">Guía del Entorno de Verificación</a> dependiendo de sus necesidades.

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
      <td rowspan="3">Preparación</td>
      <td>Comunica al equipo que hay un Pull Request en el repositorio.</td>
      <td>Integrante del equipo</td>
      <td rowspan="3">VER</td>
    </tr>
    <tr>
      <td>Decide quiénes realizarán la Pair Review.</td>
      <td>Equipo</td>
    </tr>
    <tr>
      <td>Prepara el entorno del Pair Review.
      <p>(<strong>Consulta la <a href="https://github.com/novaDepto/Nova/wiki/Gu%C3%ADa-de-entorno-de-verificaci%C3%B3n">Guía del Entorno de Verificación<strong></a> para más información).</p>
      </td>
      <td>Pair Reviewer</td>
    </tr>
    <tr>
      <td rowspan="2">Verificación</td>
      <td> Verifica el código siguiendo el <strong><a href="https://docs.google.com/spreadsheets/d/1c6FRhE9Fm7sWP4pWwGucm6aBd6LtCEgJ2KAb7Hz2inY/edit#gid=1461386475"> Reporte de Pair Review</a></strong>.</td>
      <td rowspan="2">Pair Reviewer</td>
      <td rowspan="2">VER</td>
    </tr>
    <tr>
      <td>Documenta los defectos encontrados en el Log de defectos.</td>
    </tr>
    <tr>
      <td rowspan="3">Comunicación</td>
      <td>Comunica a la pareja solicitante los resultados de la Pair Review.</td>
      <td rowspan="3">Pair Reviewer</td>
      <td rowspan="3">VER</td>
    </tr>
    <tr>
      <td>a) <strong>Aprobado</strong> = Realiza el merge de la rama a develop.</td>
    </tr>
    <tr>
      <td>b) <strong>Rechazado</strong> = Comenta en el Pull Request las correcciones que se le deben hacer al código y pega el link del Reporte de Pair Review.</td>
    </tr>
    <tr>
      <td>Seguimiento</td>
      <td> Si el Pull Request fue rechazado, entonces se podrá verificar nuevamente <strong>siempre y cuando se hayan realizado las correcciones de la revisión aterior.</strong></td>
      <td>Pair Reviewer</td>
      <td>VER, PMC</td>
    </tr>
  </tbody>
</table>

## Salidas
1. Reporte de Pair Review
2. Pull Request aprobado/rechazado

## Métricas
1. Defectos encontrados por fase

***
Versión 1.1
