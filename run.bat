@echo off
py -m pip install sarc -q
set PYTHONPATH=./Miitopia_Randomizer
py bingogen.py
pause