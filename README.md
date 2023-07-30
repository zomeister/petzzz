# PetZZZ


## `pip`, `Pipfile`, and `Pipfile.lock`

### `ipdb`
For **debugging** purposes:
- to invoke, use `ipdb.set_trace()` method
- to change debugging processs/execution, edit & run the `lib/debug.py` file.
- 
### `pytest`
For **testing** purposes.

### `sqlalchemy`
For **database** purposes and management.
- Allows interaction with database

### `alembic`
For **migration** purposes and management.
I think it's for managing changes in databases and facilitating correspondance within different dbs. But I really don't know.
- create database
- create schema
- configure application
- create migrations
- CRUD operations
    - CREATE data - `.commit()` method
    - REQUEST data - `.query()` method
    - UPDATE data - `.update()` and `.commit()` method
    - DELETE data - `.delete()` method
### `faker`
For data generation.
- `.first_name()`, `.last_name()`

### `rich`
For font formatting.
### `textual`
For formatting text.

## Some Commands
1. `pipenv install && pipenv shell` -> install dependencies
2. lib/`python cli.py` || `python debug.py` || `python.seed.py` -> run file
3. lib/`alembic upgrade head && alembic revision --autogenerate -m '<message>'`  -> migrations