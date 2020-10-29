## Responsables

Nombre         | Rol
-------------- | ---------
Juan Alcántara        | Dueño de la guía    |
Juan Alcántara | Autor

## Objetivo
Guiar a los miembros del departamento sobre qué es el manejo de la configuración y cómo se logra en Nova

## ¿Cómo manejar la configuración?
En Nova es de suma importancia mantener constancia de los artefactos y los
cambios que sufren, así como poder ver la evolución de nuestro trabajo. El
buen manejo de la configuración nos permite a todos estar en la misma página y
que no existan dudas sobre la versión más reciente de cualquier documento
generado por el equipo. También se convierte en una ventana al pasado de Nova
en caso de que se quiera entender como se llegó a cierta conclusión y para
evitar obstáculos ya superados.

Para poder cumplir con ello se siguen las siguientes prácticas:

### Identificadores únicos
Con cualquier proyecto es común terminar generando cientos de documentos y es
en ese momento donde conviene tener un identificador único que tratar de
recordar el nombre de cada uno y poder hacerles referencia eficazmente.

Para armar estos identificadores tenemos la siguiente tabla:

Tipo de documento | Prefijo | Ejemplo
----------------- | ------- | -------
Diagrama          | DIA     | DIA09
Guía              | GUI     | GUI19
Política          | POL     | POL02
Proceso           | PRO     | PRO32
Wireframe         | WIR     | WIR79
Plantilla         | PLA     | PLA34
Documentos proporcionados por el stakeholder | STA | STA01
Manual de usuario        | MAN     | MAN02

\* En caso de faltar algún tipo de documento, incluir una definición en la guía
para evitar confusiones en el futuro<br>
\** La única excepción a esta regla es el código, ya que se esta gestión se
delega al sistema de control de versiones
\*** En caso de existir una colisión de prefijos, el documento más reciente
debe agarrar el próximo número disponible

En el caso de un proyecto en específico, se tiene que definir su prefijo. Por
recomendación se toman las __primeras tres letras__ del nombre del proyecto y
se concatena con un guión (-) al inicio del prefijo según la tabla anterior.
Por ejemplo, un diagrama para el proyecto Cannis Mayoris llevaría el prefijo:
__CANN-DIA09__

### Sistema de Control de Versiones
Todo ítem de trabajo que pueda evolucionar con el tiempo tiene que ser llevado
en un sistema de control de versiones (SCV) para poder mantener un registro constante
de los cambios que sufre. Nova utiliza la herramienta __Git__ para llevar este
control.

Algunos ejemplos de documentos que pueden ser llevados en un SCV son:
* _Wireframes_ y bocetos
* Descripción de historias de usuario y diagramas
* Código
* _Scripts_ de configuración
* Procesos, políticas y guías
* Manual de Arquitectura

Los mensajes para cada _commit_ deben de ser descriptivos para poder tener una
mejor idea del cambio realizado. Por ejemplo:
```
fix: Cambiar el título para corregir faltas ortográficas.
```

## Ver también
* [Guía para NovaFlow](https://github.com/novaDepto/Nova/wiki/Gu%C3%ADa-de-Nova-Flow)

***
versión 1.0