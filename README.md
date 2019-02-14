# PROTOTYPING FLASK APP
Very basic web application for testing small features before moving to a bigger project.


## Requirements
- Python 3
- Virtual Environment (optional)

## Installation
```bash
$ virtualenv -ppython3 venv
$ pip install -rrequirements.txt
```

## Execution
```bash
$ gunicorn --workers=1 app.wsgi
```

## Author and licensing
Jagoba Pérez-Gómez <jagobapg@pm.me>

Apache 2 License
