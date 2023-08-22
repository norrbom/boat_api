SHELL := /bin/bash

.PHONY: test build run

SECRET_KEY ?=$$(openssl rand -base64 32)

clean:
	rm -fr ./venv

install:
	python3 -m venv ./venv
	. ./venv/bin/activate && \
	pip install -r requirements.txt

test:
	python3 -m venv ./venv
	. ./venv/bin/activate && \
	python -m pytest -vv

fmt:
	. ./venv/bin/activate && \
	black boat_api

mypy:
	. ./venv/bin/activate && \
	mypy boat_api

run:
	python3 -m venv ./venv
	. ./venv/bin/activate && \
	export SECRET_KEY=$(SECRET_KEY) && \
	python -m boat_api.main

run-wsgi:
	python3 -m venv ./venv
	. ./venv/bin/activate && \
	export SECRET_KEY=$(SECRET_KEY) && \
	gunicorn --config ./gunicorn.conf.py boat_api.main:app