![](https://raw.githubusercontent.com/novaDepto/Nova/master/Desarrollo%20de%20departamento/Marketing%20y%20comunicaci%C3%B3n/Imagen%20Corporativa/Im%C3%A1genes/NOVA_banner.jpg)
# Bienvenido a la wiki de Nova!
Aquí podras encontrar la documentación correspondiente a procesos, políticas, marcos de referencia, estándares, y guías que se viven en el departamento.
## Repos de los equipos
[OB_Capital](https://github.com/novaDepto/OB_Capital)

[PugSeal](https://github.com/novaDepto/PugSeal)
***
## Información General
Nova
>Sustantivo femenino del latín _nova_ que significa nuevo. Una nova es una explosión termonuclear causada por un desequilibrio entre la gravedad de una estrella y su combustible nuclear. A pesar de que una nova ocurre cuando una estrella se acerca a su fin, suelen dejar una enana blanca​ en su lugar. Estas son las estrellas más estables del universo y pueden brillar por billones de años, de ahí el nombre, **nova**.

Visión

> Dar a conocer el potencial del desarrollo de software en México, mediante soluciones competitivas a escala internacional.

Misión

> Ofrecer soluciones eficaces y escalabales a nuestros clientes, entregando productos de calidad y generando un alto grado de satisfacción.

Valores
> Perseverancia, flexibilidad, humildad y comprensión.

***

## GitHub flow
Con el fin de **simplificar** continious delivery evitamos GitFlow y GitLabFlow. A su vez descartamos flujos arriesgados (aunque contemporáneos) como OneFlow o CactusFlow. Github flow es sencillo y permite desarrollo ágil y constante. Para más info visita la [documentación](https://guides.github.com/introduction/flow/).
Production se refiere a la rama de producción del sofware en general y master es la que usan los skateholders en términos de github.
1. Crea una rama a partir de master (lo que esta aquí es siempre desplegable), recuerda usar un **nombre descriptivo** del feature a desarrollar.
2. Cualquier cambio en la rama debe reportarse con un commit. Los commit serán en inglés siguiendo verbo en infinitivo + lo que se hizo.
3. Abres un pull request que permitira que los demás sepan y revisen que cambió. Se pueden abrir muchos issues para dar feedback a quien hizo el pull request.
4. Se realiza el proceso de retroalimentación y mejora continua en el pull request, se revisa el código hasta que cumpla con las normas de calidad estipuladas.
5. Despliegas a producción para hacer las últimas pruebas antes de mergear a master. Si tu rama causa problemas puedes hacer roll back desplegando la rama de master a producción.
6. Una vez mergeado, los pull request conservan un histórico de cambios que permiten saber quién, cuando y qué se mergeo a master. Además los issues son resueltos al mergear el pull request a master, es recomendable usar enumeración para relacionar issue-pull request. Por ejemplo closed #33.
## Guías
## Políticas
## Procesos
## Comité de ética
## Roles