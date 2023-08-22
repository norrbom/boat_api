SHELL := /bin/bash

SECRET_KEY ?=$$(openssl rand -base64 32)

.PHONY: clean
clean:
	rm -fr ./venv

.PHONY: install
install:
	python3 -m venv ./venv
	. ./venv/bin/activate && \
	pip install -r requirements.txt

.PHONY: test
test:
	python3 -m venv ./venv
	. ./venv/bin/activate && \
	python -m pytest -vv

.PHONY: fmt
fmt:
	. ./venv/bin/activate && \
	black boat_api

.PHONY: mypy
mypy:
	. ./venv/bin/activate && \
	mypy boat_api

.PHONY: run
run:
	python3 -m venv ./venv
	. ./venv/bin/activate && \
	export SECRET_KEY=$(SECRET_KEY) && \
	python -m boat_api.main

.PHONY: run-wsgi
run-wsgi:
	python3 -m venv ./venv
	. ./venv/bin/activate && \
	export SECRET_KEY=$(SECRET_KEY) && \
	gunicorn --config ./gunicorn.conf.py boat_api.main:app