from pathlib import Path
from unittest.mock import patch

#Absolute path - c:\Programs Files
#Relative path is same pat as your program

path=Path()
#print(path.exists())
#make Directory
#print(path.mkdir())
#delete directory
#print(path.rmdir())
#search directory

#search *- all .py file type

for file in path.glob('*'):
    print(file)