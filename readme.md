#  Principles of information security 
## Damn Vulnerable Flask App 

### Create and access virtual environment
```bash
virtualenv VE
# windows
.\VE\Scripts\activate
# linux 
source ./VE/bin/activate
deactivate
```

### Check Your Environment
```bash
pip install -r requirements.txt
```

### Starting up
```bash
# first setup .env, and start
python secure.py
# and navigate to localhost:8000/migrate 
python vulnerable.py
```

### .env example
```bash
DATABASE=saf
DB_USER=xslizik
PASSWORD=1234
HOST=localhost
PORT=5432
```