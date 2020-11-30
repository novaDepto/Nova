
## Responsables
| Nombre         | Rol           |
| -------------- | ------------- |
| Juan Alcántara | Dueño de la guía |
| Peter González | Autor         |
| Juan Alcántara | Autor         |

## Objetivo
Guiar sobre el uso de control de versiones a través del flujo denominado: NovaFlow

## ¿Qué es NovaFlow?
![novaflow][novaflow]

Es un modelo de manejo de ramas ideado para el departamento de Nova donde se 
busca la __simplicidad__, __eficacia__ y __orden__.

Está inspirado por los modelos de Driessen (GitFlow) y por los del equipo 
inicial de GitHub (GitHub Flow). La combinación de lo positivos de ambos modelos
 nos permite tener un flujo de trabajo donde se confía en el equipo sin poner en
 riesgo la calidad del producto final.

## Ramas

### Permanentes

#### _master_

En esta rama sólo debe existir el código que está listo para ser lanzado a 
_producción_. La idea es tener una rama que ya haya pasado por todo el _flujo de
 pruebas_ y que además fue **validada por los stakeholders**.
 __NO SE PERMITEN CONTRIBUCIONES DIRECTAS__ en esta rama. Todas las 
contribuciones se deben agregar a través de _Pull Requests_ con aprobación de 
otros miembros del equipo.

A partir de esta rama van salir los despliegues a producción aplicando 
herramientas de CI/CD.

#### _staging_
En esta rama va a estar todo el trabajo que está en _proceso_. 
__NO SE REALIZAN _COMMITS_ DIRECTOS__ sobre la rama, sino que se van integrando 
las ramas temporales. La idea de esta rama es poder correr _pruebas unitarias 
automatizadas_ para **verificar que no se rompió alguna funcionalidad** cuando 
se integra el código.

Cuando se crea un _Pull Request_ hacia _staging_, se van a correr pruebas y **es
responsabilidad de quien haga ese _Pull Request_** avisar del defecto y de 
liderear el esfuerzo para repararlo. **No es necesario la aprobación de otro
integrante del equipo** para completar el _Pull Request_, el mismo developer 
tiene la autorización para completarlo él mismo.

De esta rama es que van a surgir los _Pull Requests_ hacia `master`. 
Estos _Pull Requests_ tienen que pasar la **validación de stakeholder** antes de 
aprobarse la integración.

#### Temporales
##### _*/branch_

| Prefijo | Descripción | Ejemplo |
| ------- | ----------- | ------- |
| setup   | Esta rama es utilizada para hacer modificaciones al **ambiente de desarrollo.**| `setup/django` |
| feature | Esta rama es utilizada para el **desarrollo** de las _user stories_ o _features_ de la aplicación. **Es importante poner el nombre o id de la user story para identificar el propósito de la rama**. | `feature/login_facebook` |
| fix     | Esta rama es utilizada para **arreglar errores** en el código que rompen la aplicación. Por ejemplo:  devuelve un error 404 cuando debería regresar un error 500. | `fix/login_facebook` |
| refactor    | Esta rama es utilizada para **cambiar y mejorar la lógica** utilizada en un _feature_. Generalmente estos cambios son necesarios después de la _validación de usabilidad_ con el cliente. | `refactor/login_facebook`
| docs    | Esta rama es utilizada para la subida o modificación de **documentos** en el repositorio. | `docs/readme`


## ¿Por qué NovaFlow?

### Continuous Deployment
La definición de las [ramas](#Ramas) [permanentes](#Permanentes) nos indica en 
los momentos en los que se realizan las _pruebas automatizadas_ y el 
_despliegue_ a los diferentes _ambientes de producción_. Al pasar por varios 
puntos de validación, se asegura que el código y la funcionalidad que llegan al
 usuario final se encuentran sin errores.

### Métricas
Utilizar este modelo de manejo de ramas puede ser utilizado para un análisis más
 profundo. Al mantener un [estándar](#Temporales) se puede **_automatizar_ la 
extracción de información** para el análisis de nuestro progreso y mejora en la 
calidad del código.

#### Ejemplo: Medición de eficiencia de Pair Programming
| User story  | Integrantes | Pair programming | Cantidad de commits | Cantidad de bugs | Tiempo dedicado | Tiempo bugs
|-------------|-------------|------------------|--------------------|------------------|-------------------------|----
| 1 | Peter, Juan | Sí | 12 | 6 | 04:15:12 | 00:20:54
| 2 | Peter, Juan | Sí | 11 | 3 | 03:24:12 | 00:16:20

[novaflow]: ./media/guia_nova_flow_flow.png

***
versión 2.0