@echo off

REM Clone submodule if it wasn't cloned (thanks GH)
if not exist Miitopia_Randomizer\MiitopiaRandomizer\ (
	cd Miitopia_Randomizer
	curl -Lo source.zip https://github.com/Kobazco/Miitopia_Randomizer/archive/refs/heads/master.zip
	tar -xf source.zip
	del source.zip
	robocopy /S /MOVE Miitopia_Randomizer-master .
	cd ..
)

py -m pip install sarc -q
set PYTHONPATH=./Miitopia_Randomizer
py bingogen.py
pause