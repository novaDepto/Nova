## Responsables

| Nombre  | Rol   |
|---------|-------|
|   Yaf    | Dueño del proceso |

## Objetivo
Definir los criterios a seguir en cada fase del desarrollo de una historia de usuario para **asegurar la calidad** de un producto de software.

## Entradas
1. Historia de usuario (US)

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
      <td rowspan="3">Análisis</td>
      <td>Realiza los test cases siguiendo <a href="https://docs.google.com/spreadsheets/d/1Tkbytq4iCU267aPgDj8ovtal7dWti_ZrTjLsHNSGnQU/edit#gid=416828571">la plantilla</a> </td>
      <td>Autor de la US</td>
      <td>REQM</td>
    </tr>
    <tr>
      <td>Verifica el análisis siguiendo la <a href="https://docs.google.com/spreadsheets/d/1IgZc7QfV-ERe5NN4mzPMR0jwJEriAZw02rgkx8LZxTk/edit#gid=267543590">hoja de definition of done</a>. En caso de encontrar un defecto, registralo en  el <a href="">log de defectos</a></td>
      <td>Autor de la US, Verificador</td>
      <td>REQM, VER</td>
    </tr>
    <tr>
      <td>Valida el análisis asegurandote de que el "para que" de la US se pueda lograr</td>
      <td>Product Owner</td>
      <td>REQM, VAL</td>
    </tr>
    <tr>
      <td rowspan="5">Diseño</td>
      <td>Realiza wireframes low fidelity pero asegurate de representar la estructura general de la US de manera clara y concisa</td>
      <td>Autor de la US</td>
      <td>REQM</td>
    </tr>
    <tr>
      <td>Realiza un diagrama de actividad o un algoritmo que describa de manera clara y conscisa la lógica requerida para completar la US<a></a></td>
      <td>Autor de la US</td>
      <td>REQM</td>
    </tr>
    <tr>
      <td>Realiza las modificaciones requeridas al MER, documenta el cambio en otro archivo y notifica al equipo</td>
      <td>Autor de la US</td>
      <td>REQM</td>
    </tr>
    <tr>
      <td>Verifica el diseño siguiendo la <a href="https://docs.google.com/spreadsheets/d/1IgZc7QfV-ERe5NN4mzPMR0jwJEriAZw02rgkx8LZxTk/edit#gid=267543590">hoja de definition of done</a>. En caso de encontrar un defecto, registralo en el <a href="">log de defectos</a></td>
      <td>Autor de la US, Verificador</td>
      <td>REQM, VER</td>
    </tr>
    <tr>
      <td>Valida el diseño asegurandote de qué el "para que" de la US se pueda lograr</td>
      <td>Product owner</td>
      <td>REQM, VAL</td>
    <tr>
      <td rowspan="5">Construcción</td>
      <td>Desarrolla el backend de la US</td>
      <td>Autor de la US</td>
      <td>REQM</td>
    </tr>
    <tr>
        <td>Desarrolla le frontend de la US: GUI y lógica</td>
        <td>Autor de la US</td>
        <td>REQM</td>
    </tr>
    <tr>
        <td>Coloca un Pull Request con la implementación lista para ser revisada y notifica al equipo</td>
        <td>Autor de la US</td>
        <td>REQM</td>
    </tr>
    <tr>
        <td>Verifica la construcción en el PR siguiendo la <a href="https://docs.google.com/spreadsheets/d/1IgZc7QfV-ERe5NN4mzPMR0jwJEriAZw02rgkx8LZxTk/edit#gid=267543590">hoja de definition of done</a>.En caso de encontrar un defecto, registralo en  el <a href="https://docs.google.com/spreadsheets/d/1p7jjni0co6IECTxC1ZdccV9jmnQxoqOTV6jjng3B4EQ/edit#gid=1803474303">log de defectos</a></td>
        <td>Autor de la US, Verificador</td>
        <td>REQM, VER</td>
    </tr>
    <tr>
        <td>Valida la US con los stakeholders y/o usuarios finales</td>
        <td>Product owner</td>
        <td>REQM, VAL</td>
    </tr>
   <tr>
      <td rowspan="5">Pruebas</td>
      <td>Codifica los pruebas unitarias con base a los test cases definidos en el análisis</td>
      <td>Autor de la US</td>
      <td>REQM</td>
    </tr>
    <tr>
        <td>Diseña la prueba de usabilidad con el método de tu preferencia</td>
        <td>Autor de la US</td>
        <td>REQM</td>
    </tr>
    <tr>
        <td> Actualiza tu PR con un commit integrando las pruebas codificadas y notifica al equipo</td>
        <td>Autor de la US</td>
        <td>REQM</td>
    </tr>
    <tr>
    <td>Verifica las pruebas siguiendo la <a href="https://docs.google.com/spreadsheets/d/1IgZc7QfV-ERe5NN4mzPMR0jwJEriAZw02rgkx8LZxTk/edit#gid=267543590" >hoja de definition of done.</a>a En caso de encontrar un defecto, registralo en el <a href="https://docs.google.com/spreadsheets/d/1p7jjni0co6IECTxC1ZdccV9jmnQxoqOTV6jjng3B4EQ/edit#gid=297985474">log de defectos</a></td>
        <td>Autor de la US, Verificador</td>
        <td>REQM, VER</td>
    </tr>
    <tr>
        <td>En caso de no encontrar defectos, integra la US a la rama staging</td>
        <td>Verificador</td>
        <td>REQM</td>
    </tr>
    <tr>
      <td rowspan="5">Documentación</td>
      <td>Documenta la trazabilidad de la US en la<a> <a href="https://docs.google.com/spreadsheets/d/1iEOBChW8HzQvdpJSUsqMirMwRWsya-CJEX0GfbMqniA/edit#gid=0">matriz de trazabilidad</a></td>
      <td>Autor de la US</td>
      <td>REQM</td>
    </tr>
    <tr>
        <td>Documenta el funcionamiento de la US en el manual de usuario</td>
        <td>Autor de la US</td>
        <td>REQM</td>
    </tr>
    <tr>
        <td>Documenta cualquier cambio a la arquitectura en el manual de arquitectura</td>
        <td>Autor de la US</td>
        <td>REQM</td>
    </tr>
    <tr>
        <td>Valida el manual de usuario con el PO</td>
        <td>Autor de la US</td>
        <td>REQM, VAL</td>
    </tr>
    
  </tbody>
</table>

## Salidas
1. Historia de usuario terminada e integrada a la rama de desarrollo
2. Manual de usuario actualizado con la US
3. Manual de arquitectura actualizado
4. Log de defectos actualizado

## Métricas
1. Tiempo de ejecución del proceso

***
Versión 1.0
