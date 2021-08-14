TOP_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
SHELL := /bin/bash

tests:	init
	@cd ${TOP_DIR} && \
	source ${TOP_DIR}/.venv/bin/activate && \
	pip install -r ./requirements.txt

init:
	@cd ${TOP_DIR} && \
	if [ ! -d "${TOP_DIR}/.venv/" ]; then \
		virtualenv -p python3 ${TOP_DIR}/.venv/; \
	fi && \
	source ${TOP_DIR}/.venv/bin/activate && \
	PYTHONPATH=${TOP_DIR}:${TOP_DIR}/tests python3 -B -m unittest discover -s ${TOP_DIR}/tests/ -t ${TOP_DIR} -p '*_test.py'
