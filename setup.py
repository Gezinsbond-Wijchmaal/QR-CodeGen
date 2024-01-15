import sys
from cx_Freeze import setup, Executable

# Voeg extra bestanden toe
files = ['pics', 'fonts', 'sounds']  # Voeg de paden naar uw bronmappen hier toe

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('start.py', base=base)
]

setup(
    name = 'GezinsbondTool',
    version = '1.0.0.1',
    description = 'Gezinsbond Tool Selecteerder',
    options = {'build_exe': {'include_files': files}},
    executables = executables
)
