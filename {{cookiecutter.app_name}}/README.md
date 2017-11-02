# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Run locally
Project uses python 3.6; To install check Dockerfile.
Install requirements
`pip install -r requirements.txt`

To start the service `{{cookiecutter.service_name}}`

run `python service/{{cookiecutter.service_name}}.py`

then `http://localhost:5000/` should return swagger UI with exist endpoints 

### Tests

just run `pytest` in main catalog


## Docker
### Build
`docker build -t ms-spel{{cookiecutter.service_name}}lchecker .`

### Run
`docker run -d -p 5000:5000 --name ms-{{cookiecutter.service_name}}-c --rm ms-{{cookiecutter.service_name}}`

#### Tests in Docker
`docker run -p 5000:5000 --name ms-{{cookiecutter.service_name}}-c --rm ms-{{cookiecutter.service_name}} python -m pytest tests`
