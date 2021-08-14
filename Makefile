TOP_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
SHELL := /bin/bash

tests:	init
	@cd ${TOP_DIR} && \
	source ${TOP_DIR}/.venv/bin/activate && \
	PYTHONPATH=${TOP_DIR}/gcloud/aio:${TOP_DIR}/tests python3 -B -m unittest discover -s ${TOP_DIR}/tests/ -p '*_test.py'

init:
	@cd ${TOP_DIR} && \
	if [ ! -d "${TOP_DIR}/.venv/" ]; then \
		pip3 install virtualenv; \
		python3 -m virtualenv -p python3 ${TOP_DIR}/.venv/; \
	fi && \
	source ${TOP_DIR}/.venv/bin/activate && \
	pip install -r ./requirements.txt -r requirements-dev.txt

dist:   tests
	source ${TOP_DIR}/.venv/bin/activate && \
	python3 ${TOP_DIR}/setup.py sdist bdist_wheel

clean:
	cd ${TOP_DIR} && \
	rm -rf dist/ *.egg-info/

upload: clean dist
	cd ${TOP_DIR} && \
	source ${TOP_DIR}/.venv/bin/activate && \
	twine upload dist/*
