# Testing with *pytest*

- Crear en la carpeta `test/` la **misma estructura de carpetas** que en `src/`. Hacer **lo mismo con los python scripts a ser testados** pero incluyendo delante al prefijo *test_*.
- Dentro de cada script *test_*, incluir como minimo tantas **funciones de testeo** con prefijo *test_* como funciones hay que estar en el correspondiente python script. 
- No obstante, no es necesario tener una sola funcion de testing por cada funcion a ser testada. Si alguna de estas funciones se vuelve demasiado grande, es mejor crear varias mas peques para mejorar en legibilidad.
- Las herramientas probadas han sido:
    1. **Validaciones de una funcion** con un *assert* para ver que los outputs son correctos.
    2. **Validacion de una excepcion fuera de control**:
    ```
    with pytest.raises(Exception): ## case of an unknowledged exception
        # function with an exception without any try except (out of control)  
    ```
    3. **Validacion de una excepcion conocida (en este caso *ValueError*) y bajo control**:
    ```
    with pytest.raises(ValueError): ## case of an unknowledged exception
        # function with an exception (in this case *ValueError*) with a try except (controled)  
    ```
- Primero se iran haciendo **test unitarios**, es decir, de funciones independientes para luego hacer test mas complicados, **test de integraccion** de workflows.

> NOTA: **Conviene desarrollar codigo / sus respectivas funciones de testing al mismo tiempo. No solo se ahorra tiempo sino el tener que pensar en el testing ayuda en el design de la funcion a desarrollar**.