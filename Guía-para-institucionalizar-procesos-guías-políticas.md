## Responsables
Nombre         | Rol
-------------- | -----
Juan Alcántara | Dueño de la guía    |
Juan Alcántara | Autor
Pedro González | Autor
Alonso Oropeza | Autor
Yafté Gallegos | Autor
Daniel Elias | Autor

## Objetivo
El objetivo de esta guía es **orientar** y **facilitar** la participación en el
[proceso] definido para institucionalizar procesos, guías y políticas.

## Recomendaciones sobre el documento
1. No tiene que estar perfecto, puede ser un borrador. El objetivo de este
proceso es apoyarnos mutuamente para mejorar la calidad del departamento.

0. **Recuerda agregar un _link_ en el archivo __Sidebar_**. Así cuando se 
apruebe el documento y se suba en automático a la wiki, se pueda acceder con 
rapidez a este. 

0. **Recuerda poner el Identificador único del documento** siguiendo la
[Guía de manejo de la configuración](https://github.com/novaDepto/Nova/wiki/Gu%C3%ADa-de-manejo-de-configuraci%C3%B3n) y guiándote en la numeración del
documento de [Listado y control de documentos wiki](https://docs.google.com/spreadsheets/d/1zb8at9oXi9vS-wS0yP7s6vCBlLSLcxMHLbA9aJRmJCI/edit?usp=sharing)

0. **Github automáticamente despliega el nombre del archivo cómo el _título del
documento_. Por lo que no hay que poner un título en el archivo para evitar que
se repita este**.

0. Es muy importante que en los documentos se defina un **_objetivo_** que 
aporte al departamento. **No realices documentos por ocio porque también 
involucra tiempo de tus compañeros.**


## ¿Cómo publico mis documentos para revisión?
### Iniciar _Pull Request_
Iniciar un _pull request_ es algo bastante sencillo:
1. Debes **publicar la rama** en la cual estás trabajando tu documento al
_[repositorio remoto]_. **Recuerda que es una rama por documento y que no
publicamos directamente a la wiki**.

0. Ya con la rama publicada, selecciona la sección de `Pull requests`.

0. Posteriormente presiona el botón de `New pull request`.

0. Te preguntará sobre la _rama base_ y la _rama a comparar_. La primera **tiene
que ser la rama _master_**. La segunda es la rama que publicaste en el paso 1.

0. Ahora presionas el botón `Create pull request`.

0. Antes de iniciar el pull request te solicitará un título y una descripción.

    1. **En el título**: escribe el título de tu archivo, en caso de que sea una
       corrección, indica claramente que es sólo para una corrección (p.e. 
       Corrección: Falta de ortografía en el menú principal).

    2. **En la descripción**: escribe el objetivo del documento, y una breve
       descripción de este.

0. Finalmente confirma la creación presionando `Create pull request`.

### Solicitar revisión a un encargado de área
1. Al crear un proceso, política o guía que sea relacionada con una área del
departamento recomendamos que se solicite la aprobación de un encargado de esta.
Para pedir una revisión en un _pull request_, selecciona el símbolo de ajustes
de la sección de `Reviewers`. En caso de que no aparezca el usuario de la 
persona, solicita que un librarian lo agregue como **colaborador**.

2. Además, agrega a tu pull request la etiqueta de **Review Required**.
Para agregar labels solo da click al checkbox de tu pull request, y selecciona el label en el dropdown de labels
que aparece a la izquierda de tu pantalla.

![reviewers][reviewers]

### Realizar correcciones o cambios
1. Después de una revisión, puede que te soliciten cambios. Realiza los cambios
necesarios en la **rama en la que publicaste tu borrador del documento**. Al
volver a publicar esta rama, el _pull request_ se actualizará.

2. Además, agrega a tu pull request la etiqueta de **Requested Changes Fixed**.

## ¿Cómo hacer revisiones a propuestas de mis compañeros?
### Revisar cambios
Para revisar los cambios que realizó mi compañero:
1. Busca y selecciona el _pull request_ en la sección de `Pull requests`.

2. Selecciona la pestaña de `Files changed`

3. Si deseas ver un _preview_ de cómo se verían los archivos, presiona el botón
de archivo al lado izquierdo del _checkbox_ `viewed`.
![preview][preview]

### Comentar líneas en específico
Si deseas comentar en algunas lineas en específico:
1. En la pestaña de `Files changed`, en la visualización de código, al hacer
hover sobre el símbolo de `+` de la línea se visualiza un botón con el símbolo
`+`de color azúl. Presiona dicho botón para enmarcar la línea. Deja presionado 
y arrastra hacia abajo para seleccionar más lineas.

2. Al soltar el click izquierdo del ratón emerge una pestaña en dónde puedes
escribir tu comentario. 

3. Al terminar de escribirlo selecciona `add single comment`

![comentario][comentario]

### Solicitar cambios
1. Para solicitar cambios: realiza los pasos 1 y 2 de **Comentar líneas en
específico**. Ahora empezarás un _review_ con el botón de `Start a review`. Con
este _review_ podrás agregar varios comentarios en diferentes partes del
documento. Para **finalizar** el _review_ presiona el botón de `Finish your
review` en la parte superior derecha, selecciona el _checkbox_ de `Request
changes`, y finalmente `Submit review`.

2. Además, agrega al pull request la etiqueta de **Changes Requested**.

![cambios]

3. Cuando se hagan los cambios que pediste te llegará una notificación a tu correo,
y en la conversación del _pull request_ desplegará un mensaje sobre un nuevo
_commit_.

### Aprobar el documento
1. Para aprobar un documento: En la sección de `Files changed`, en la parte
superior derecha, presiona `Review changes`. Recomendamos que dejes un 
comentario que felicite al autor del documento para subir la moral :). 
Finalmente selecciona el _checkbox_ de `Approve` y sube la validación con el
botón de `Submit review`.

2. Además, se recomienda que cuando el documento ya esté aprobado se añada la etiqueta **Approved** y/o 
**Communication Required** al pull request.

![aprobar][aprobar]

[proceso]: https://github.com/novaDepto/Nova/wiki/Proceso-para-definir-un-proceso
[repositorio remoto]: https://github.com/novaDepto/Nova
[reviewers]: media/guia_institucionalizar_reviewers.png
[preview]: media/guia_institucionalizar_preview.png
[comentario]: media/guia_institucionalizar_comentario.png
[cambios]: media/guia_institucionalizar_cambios.png
[aprobar]: media/guia_institucionalizar_aprobar.png

***
versión 1.0