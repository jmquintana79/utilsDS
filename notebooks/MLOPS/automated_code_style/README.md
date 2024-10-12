# Automated Code Style

## black (ESSENTIAL and alternative to ruff)
Code style formatting automatically.
Possible in pre-commit.
https://black.readthedocs.io/en/stable/
`> black main.py`

## ruff (ESSENTIAL and alternative to black allthough more complete)
Code style linting for checking and formatting automatically.
It is more completed than black because not only include formatting, checking as well.
Possible in pre-commit and poetry.
https://pypi.org/project/ruff/
```
ruff check                              # check in current folder
ruff check <script or folder path>      # check on selected path
ruff format                             # automatically format in current folder
ruff format <script or folder path>     # automatically format on selected path
```

## mypy (INTERESTING FOR TYPES and then FOR DOCSTRINGS)
Mypy is a static type checker.
It is not working for me. Always return a success message:
> mypy main.py
However, forzing a strict mode, working more strongly:
`> mypy --strict main.py`

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
