# Boat API

The Boat API

## Installation

Create a venv and install packages

```sh
make install
```

## Start the Boat API in development mode with hot reloading

```sh
make run
```

## Start the Boat API in a production like mode

```sh
make run-wsgi
```

## Configuration

gunicorn.conf.py

```sh
workers = 2 # number of workers / Flask processes gunicorn starts
worker_class = 'gevent' # enables ansyc code in the Flask process
```
## API Endpoints examples

/api/v1/stations/100/59.40225,18.35317

## How to contribute?

- clone this repo or pull the latest changes
- create a new branch feature/\<feature\>
- run `make fmt mypy test` to auto format code, run static type checker and unit tests
- push the code and create a merge request to main branch
- get the pull request reviewed and approved, the branch should be removed once merged.
- create a new git tag version, following semantic versioning i.e. MAJOR.MINOR.PATCH