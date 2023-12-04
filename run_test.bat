@echo off
pytest -v -s test_lab6.py

pylint lab6.py

pylint test_lab6.py