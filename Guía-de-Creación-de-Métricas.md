## Responsables

| Nombre | Rol              |
| ------ | ---------------- |
| Daniel | Dueño de la guía |
| Irving | Autor            |
| Juan    | Autor            |

## Contenido

## ¿Qué es una métrica?

Es una **medida cuantificable** que nos permite **rastrear y evaluar el estado de un proceso**.

En el área del software, las métricas nos permiten conocer el tamaño del reto al que como desarrolladores de software nos enfrentamos y poder tomar decisiones de acuerdo a la tendencia de los resutados.

## Tipos de métricas
* **Escalares**: Números concretos y aislados. Dan poca o nula información. 
Ejemplo: numero de defectos: **34**<br><br>
* **Tendencia**: Números escalares vistos a través del tiempo, Dan mucha información y facilitan la toma de decisiones. Ejemplo: 

![](https://i.imgur.com/mV4hIa1.png)
<br>
* **Listas**: Enumeración de registros, permíten tener información detallada de las métricas, al igual que las tendencias son útiles para tomar decisiones. 
Ejemplos: lista de defectos, lista de cosas que se hicieron bien/mal, etc.
---

## ¿Cómo crear una métrica?

### 1. Define una Meta
Desarrolla una Meta identificando un conjunto de objetivos de calidad y/o productividad, a nivel departamento, de proyecto o personal; por ejemplo, satisfacción del cliente, entrega a tiempo, mejora del rendimiento.

Estos objetivos son necesarios para cumplir con la meta, identifica lo que se quiere lograr en cuestión de procesos, productos o recursos.

El objetivo debe:
* Ser específico: ¿Qué espero lograr?
* Ser medible: ¿Se puede demostrar con números el avance/logro del objetivo?

**Ejemplo de un objetivo:
Mejorar la puntualidad del procesamiento de solicitudes de cambio**


### 2. Desarrolla Preguntas
A partir del objetivo desarrolla un conjunto de preguntas para caracterizar la forma en la que la evaluación o el logro del objetivo específico será realizado.

Respondiendo estas preguntas uno debe ser capaz de concluir si el objetivo es alcanzado además de poder cuantificarlos.

**Ejemplo de preguntas:**
Objetivo: Mejorar la puntualidad del procesamiento de solicitudes de cambio
**¿Cuál es la velocidad de procesamiento de la solicitud de cambio actual?
¿Está mejorando el rendimiento del proceso?**


### 3. Específica las métricas
Asocia un conjunto de datos con cada pregunta, de manera que puedan responderla de forma cuantitativa.

Las métricas deben considerar las siguientes características:

* Debe ser consistente y objetiva (no debe ser ambigua).
* Fácil y rentable de obtener.
* Capaz de ser validada por su precisión y fiabilidad.
* Fácil de adaptar a los proyectos.
* Tener una unidad de medida específica (valor ganado, %costo de cálidad, % varianza de esfuerzo, etc).

Una vez cumpla con las caractetísticas anteriores la métrica debe tener:

* **Nombre:** Una forma de identificar la métrica.
* **Meta y objetivos:** La meta y objetivos de ésta.
* **Preguntas:** Las preguntas que debe responder la métrica
* **Fórmula:** De qué forma se calcula la métrica.
* **Ubicación:** El documento donde se registrarán los datos de dicha métrica.

**Ejemplo de métricas:**
Objetivo: Mejorar la puntualidad del procesamiento de solicitudes de cambio
Preguntas: ¿Cuál es la velocidad de procesamiento de la solicitud de cambio actual?
¿Está mejorando el rendimiento del proceso?
**(Tiempo de ciclo medio actual/Tiempo de ciclo promedio) * 100**

***
versión 1.0