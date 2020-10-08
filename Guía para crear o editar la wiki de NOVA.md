# Guía para crear o editar la wiki de NOVA
## Objetivo

Enseñar a crear o editar apartados en la [wiki de NOVA](https://github.com/novaDepto/Nova/wiki) así como las herramientas necesarias para hacerlo.

## Markdown

* Es un lenguaje ligero qué nos permitirá convertir texto marcado como este, en documentos XHTML. [Consulta la guía.](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Editores

* Editor local: Pueden usar el editor con el qué se sientan más cómodos, recomendamos [Typora](https://typora.io/) es un editor para usar Markdown de forma local, ya sea para MacOS, Windows Linux.
* Editor colaborativo online: [HackMD](https://hackmd.io/) es un editor de Markdown que puede ser editado por varias personas al mismo tiempo.

## Pasos a seguir

### Typora
1. Descarga [Typora](https://typora.io/) para tu sistema operativo.
2. Instalar Typora
3. Clonar el repositorio de Github de NOVA en algún directorio de tu preferencia
`git clone https://github.com/novaDepto/Nova.wiki.git`
4. Si ya tienes el repositorio, te colocas en tu rama y la actualizas con la rama *master* 
`git pull origin master`
5. Abre Typora y abre el archivo *.md* que quieras modificar.
6. Al terminar de modificarlo haz los siguientes comandos a tu rama 
`git add *`
`git commit -m "Modificación de proceso 'Proceso para crear procesos' "`
`git push origin RamaQueQuieroPushear`
7. Hacer pullrequest
8. Comúnicate con los encargados de la wiki para que autoricen el cambio.

### HackMD
1. Accede al sitio de HackMD y crea una cuenta. Una vez creada te redirigira a *My Workspace*
2. Selecciona *New note*
3. Para poder invitar a otros colaboradores selecciona el icono de compartir ubiado en la esquina superior derecha donde se mostrara el link. Una vez que accedan, la nota aparecera en *My workspace* en el apartado de  *Collaborative* 
4. Una vez terminado selecciona *Push to Github* y selecciona el repositorio asi como la rama en la que seran publicados.
5. En *Select file* escribe el nombre del archivo si estas modificando uno existente selecciona el archivo.
6. Selecciona *Push*.
