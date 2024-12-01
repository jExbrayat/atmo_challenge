# Developer guide
## API key
Create a file `api_key` in the project's root directory in which is stored your personal API key.  
Make sure there is not empty line.

## Dependency management using Poetry

### Install Poetry
```bash
pip install poetry
```

### Install dependencies
```bash
cd project/root/folder/
poetry install
```
or
```bash
python -m poetry install
```
This command will create a virtual environment and install the user's dependencies in it.  

### Run script or Python module
```bash
poetry run python script.py
poetry run nb-clean ...
```

### Add dependency
```bash
poetry add matplotlib
poetry lock
```

See the complete documentation on https://python-poetry.org/.

## Continuous integration
These steps must be followed before committing.  
*Make sure to have installed dependencies priorly.*

### Clean notebooks
Ensure notebooks metadata are cleaned to avoid merge conflicts.  
```bash
poetry run nb-clean clean . --preserve-cell-outputs --remove-empty-cells
poetry run nb-clean check . --preserve-cell-outputs --remove-empty-cells
```
The first command cleans all notebooks in the source directory `.`.  
The second command outputs nothing if all went well.