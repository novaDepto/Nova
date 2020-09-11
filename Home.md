![](https://raw.githubusercontent.com/novaDepto/Nova/master/Desarrollo%20de%20departamento/Marketing%20y%20comunicaci%C3%B3n/Imagen%20Corporativa/Im%C3%A1genes/NOVA_banner.jpg)

# Bienvenido a la wiki de Nova!
Aquí podras encontrar la documentación correspondiente a procesos, políticas, marcos de referencia, estándares, y guías que se viven en el departamento.

## Repos de los equipos

[OB_Capital](https://github.com/novaDepto/OB_Capital)

[PugSeal](https://github.com/novaDepto/PugSeal)

***

## Información General
Nova
> Sustantivo femenino del latín _nova_ que significa nuevo. Una nova es una explosión termonuclear causada por un desequilibrio entre la gravedad de una estrella y su combustible nuclear. A pesar de que una nova ocurre cuando una estrella se acerca a su fin, suelen dejar una enana blanca​ en su lugar. Estas son las estrellas más estables del universo y pueden brillar por billones de años, de ahí el nombre, **nova**.

Visión
> Dar a conocer el potencial del desarrollo de software en México, mediante soluciones competitivas a escala internacional.

Misión

> Ofrecer soluciones eficaces y escalabales a nuestros clientes, entregando productos de calidad y generando un alto grado de satisfacción.

Valores
> Perseverancia, flexibilidad, humildad y comprensión.

## GitHub flow
Con el fin de **simplificar** continious delivery evitamos GitFlow y GitLabFlow. A su vez descartamos flujos arriesgados (aunque contemporáneos) como OneFlow o CactusFlow. Github flow es sencillo y permite desarrollo ágil y constante. Para más info te invito a revisar el siguiente [video](https://www.youtube.com/watch?v=2Xagp86uOuI).
1. Crear una rama de feature a partir de master.
2. Cualquier cambio en la rama debe reportarse con un commit. Los commit serán en inglés siguiendo verbo en infinitivo + lo que se hizo.
3. Abres un pull request que permitira que los demás sepan y revisen que cambió. Se pueden abrir muchos issues para dar feedback a quien hizo el pull request.
4. Despliegas la feature (ojo no esto no quiere decir que se despliega master) se despliega la feature que quiere decir se puede probar, hacer hotfixes en caso de que algo truene y hacer rollout en caso necesario, todo esto para minimizar riesgos.
6. Una vez que todo funciona como debe y cumple los estándares de calidad se **mergea** a master.