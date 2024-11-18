# Developer guide
## API key
Create a file `api_key` in the project's root directory in which is stored your personal API key.  
Make sure there is not empty line.

## Dependencies
### Install dependencies
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

### Add a dependency
```bash
pip install my_dependency
pip freeze > requirements
```
