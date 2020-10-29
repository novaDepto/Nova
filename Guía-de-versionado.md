## Responsables
Nombre         | Rol
-------------- | -----
Juan Alcántara | Dueño de la guía    |
Juan Alcántara | Autor

## Objetivo
Guia al departamento sobre qué es el versionado, y que significa cada uno de los elementos de un número de versión, para lograr manejar la configuración y gestionar cambios de manera controlada

## Versiones
A veces es difícil determinar en que estado está un _codebase_ o los documentos
de una _wiki_ con tan sólo verlo. Es necesario saber si se trata de una versión
final, una versión lista para producción o si se trata tan sólo de una versión
en _beta_.

Nova utiliza números de versiones para poder obtener esta información de
inmediato. Esta guía busca aclarar cómo funcionan las versiones en el
departamento.

### Dos números y una letra
Las versiones están definidas por dos números separados por puntos y una letra
de sufijo: __x.y?__

* __x__: Este número representa la liberación o línea base a la que pertenece
    el ítem en cuestión. Esto quiere decir que todos los ítems de la primera
    liberación externa deben seguir el siguiente patrón: __1.y?__
* __y__: Este número representa una "liberación" interna y se refiere a cada
    vez que se integra __algo totalmente nuevo__ en el ítem en cuestión desde
    su última liberación. Es decir que si para la primera liberación es la
    quinta vez que se agrega algo totalmente nuevo (no un arreglo) debe seguir
    el siguiente patrón: __1.5?__
* __?__: Es la primera letra de la estabilidad del trabajo. Es decir que si
    todavía presenta __errores de verificación__ esto debe estar en __*alpha*__
    y si presenta __errores de validación__ esto debe estar en __*beta*__.
    Cuando se trate de una versión consumible no hay que colocar ningún
    prefijo. Es decir que si lo que hemos trabajado presenta algunos
    comentarios de _stakeholder_ y corresponde a la primera liberación con
    cinco partes nuevas, debería corresponder a la versión __1.5b__

__Nota:__ Todas las versiones de todos los artefactos deben partir del __0.1a__
donde se entiende que se trata de una versión inicial con detalles a pulir.

***
versión 1.0
