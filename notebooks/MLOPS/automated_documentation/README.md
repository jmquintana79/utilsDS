# Automated Documentation

## interrogate (ESSENTIAL)

- https://interrogate.readthedocs.io/en/latest/index.html
- It will check and warn you if you have failed to write docstrings for your code.
- Sin informacion, solo muestra la metrica final:
`> interrogate {path}`
- Con informacion basica de cada script: 
`> interrogate -v {path}`
- Con informacion mas ampliada de cada script:
`> interrogate -vv {path}`


## pydocstyle (NO SO NECESSARY)

- https://pypi.org/project/pydocstyle/
- It is a static analysis tool for checking compliance with Python docstring conventions.
> NOTA: Lo veo demasiado, es demasiado estricto. No lo veo tan necesario.
`> pydocstyle {path}`


## pdoc3 (ESSENTIAL)

- https://pdoc3.github.io/pdoc/
- Generador de documentacion automatica muy muy util. 

### Opciones de comando
```
main command:
> pdoc <options> <module path>

optional arguments:
  -h, --help            show this help message and exit
  -f, --force           Overwrite any existing generated (--output-dir) files.
  --html                When set, the output will be HTML formatted.
  --pdf                 When set, the specified modules will be printed to standard output, formatted in Markdown-Extra, compatible with most Markdown- (to-HTML-)to-PDF
                        converters.
  -o DIR, --output-dir DIR
                        The directory to output generated HTML/markdown files to (default: ./html for --html).
  --http HOST:PORT      When set, pdoc will run as an HTTP server providing documentation for specified modules. If you just want to use the default hostname and port
                        (localhost:8080), set the parameter to :.
  --skip-errors         Upon unimportable modules, warn instead of raising.
```
> NOTA: El comando `--pdf` no me ha funcionado bien pues no ha generado ningun fichero. Creo que es necesario instalaciones y configuraciones adicionales para conseguirlo.

## Ejemplo de uso

`> pdoc --html --output-dir docs --force <path module>`