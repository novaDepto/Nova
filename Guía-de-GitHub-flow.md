## ¿Por qué usar este flujo de trabajo?
Con el fin de **simplificar** continious delivery evitamos GitFlow y GitLabFlow. A su vez descartamos flujos arriesgados (aunque contemporáneos) como OneFlow o CactusFlow. Github flow es sencillo y permite desarrollo ágil y constante. Para más info te invito a revisar el siguiente [video](https://www.youtube.com/watch?v=2Xagp86uOuI).

## ¿Cómo funciona?
1. Crear una rama de feature a partir de master.
2. Cualquier cambio en la rama debe reportarse con un commit. Los commit serán en inglés siguiendo verbo en infinitivo + lo que se hizo.
3. Abres un pull request que permitira que los demás sepan y revisen que cambió. Se pueden abrir muchos issues para dar feedback a quien hizo el pull request.
4. Despliegas la feature (ojo no esto no quiere decir que se despliega master) se despliega la feature que quiere decir se puede probar, hacer hotfixes en caso de que algo truene y hacer rollout en caso necesario, todo esto para minimizar riesgos.
6. Una vez que todo funciona como debe y cumple los estándares de calidad se **mergea** a master.