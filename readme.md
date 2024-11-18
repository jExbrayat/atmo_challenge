# Developer guide
## Install dependencies
`cd` in the project's root directory  

Create a virtual environment
```bash
python -m venv .venv
```

Activate the virtual environment
```bash
source .venv/bin/activate
```
Or launch Python / pip with the following
```bash
.venv/bin/python
.venv/bin/pip
```

Install the required dependencies
```bash
pip install -r requirements.txt
```

## Add a dependency
```bash
pip install my_dependency
pip freeze > requirements
```
