# Patch 1 - Bread

This assumes you have pipenv setup. Look [here](https://github.com/pypa/pipenv) for setup instructions.

## How to run tests

```bash
pipenv install -d
pipenv shell
pip install -e app/

./test
```

## How to run the server

_this does requite sqlite3 to be installed on your pc_

_also repeat the pipenv set up from above_

```bash
# set up some vars
export FLAG=123
export FLAG_SECRET=123
# create a db 
touch test.db
sqlite3 test.db < setup.sql
# link the db
export DB_CONNECTION_STRING='sqlite:////some/absolute/path/to/the/above/test.db'
python3 run.py
```
