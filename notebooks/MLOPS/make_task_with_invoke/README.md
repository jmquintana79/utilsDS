# Make Tasks

En entornos *Linux*, una herramienta muy poderosa es el uso de *Makefiles* para lanzar tareas predeterminadas que involucran comandos del sistema (ej. ejecucion de scripts), todo ello de una manera muy sencilla.

El problema es que en *Windows* por ejemplo *make* no esta disponible. En *MacOs* si que es posible pero requiere una instalacion. 

Despues de probar diferentes alternativas, como por ejemplo *Snakemake*, he encontrado una altertativa mas prometedora: [Invoke](https://docs.pyinvoke.org/en/stable/).

## Alternativas

### Snakemake

- Snakemake es interesante, pero creo que es mas valido para construir y sobretodo ejecutar *pipelines* para *Data Analysis*.
- Es un poco viejo y no muy usado.
- Su uso es sencillo pero la construccion de *pipelines* mas complicados (meter bucles por ej) es un poco tricky.
- Funciona muy bien su paralelizacion. 
- En si no lo veo util para herramienta de *make tasks*.

### Invoke

- Es 100% Python y facil de usar.
- Si que es una herramienta de herramientas de *make tasks* , tareas que son faciles de implementar usando el poder de Python.
- Tiene un sencillo ejecutador de comandos del sistema (valido para *Windows*, *Linux*, etc).
- Ademas, permite establecer la ejecucion de tareas previas por defecto cuando ejecutas una tarea en cuestion.
- Las tareas son guardadas en un script *tasks.py*. Este *script* hace las veces de *Makefile*. No obstante, no hace falta incluir todas las tareas en este fichero, sino que se puede definir en diferentes ficheros y estos ser centralizados e invocados a traves de *tasks.py* (mediante el uso de *namespaces*).
- Ademas se puede construir un programa/libreria a-doc con la funcionalidad de *invoke* que permite por decirle asi customizar el "producto".
- Por tanto esta libreria es util para:
    - Make task commands.
    - Run shells commands.

#### References

- [Welcome to Invoke!](https://www.pyinvoke.org)
- [Getting started](https://docs.pyinvoke.org/en/stable/getting-started.html)
- [Invoking tasks](https://docs.pyinvoke.org/en/stable/concepts/invoking-tasks.html)