# Automated Code Style

## black (ESSENTIAL)
Code style formatting automatically.
https://black.readthedocs.io/en/stable/
`> black main.py`

## flake8 (NO ESSENTIAL BUT INTERESTING KEEP IN MIND)
Static code analysis, just for warning, not repearing automatically.
https://flake8.pycqa.org/en/latest/index.html#quickstart
`> flake8 main.py`

## pylint (NO ESSENTIAL BUT INTERESTING KEEP IN MIND)
Static code analysis to force coding stardards and detect errors.
For me, it is very similar than flake8 with maybe some different checks.
I like a lot and finally return a rate.
https://github.com/pylint-dev/pylint
`> pylint main.py`

## mypy
Mypy is a static type checker.
It is not working for me. Always return a success message:
> mypy main.py
However, forzing a strict mode, working more strongly:
`> mypy --strict main.py`
