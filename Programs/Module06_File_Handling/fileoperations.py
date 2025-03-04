import os
from pathlib import Path

print(os.path.basename(r"C:\Users\gdevid\OneDrive - athenahealth\Backup\Devid\Training\PythonTutorial\Module6_File_Handling\fileoperations.py"))

print(os.path.abspath(r"..\fileoperations.py"))

print(os.getcwd())
print(Path.cwd())
print(os.path.dirname(__file__))
