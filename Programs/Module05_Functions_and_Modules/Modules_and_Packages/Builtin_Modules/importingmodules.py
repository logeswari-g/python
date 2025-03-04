# Syntax:
# from <packagename> import <module_name>
# datetime # (Package)
#     -> datetime (datetime.py) # (Module)
#         -> today() # Definition

from datetime import datetime

# Use asterisk(*) to import all modules and subpackages in a package
# from openpyxl import chart
# from openpyxl import styles
from openpyxl import *

# print(datetime.today()) # modulename.definitionname()

# import json
from json import encoder, decoder

text = '10"'
# jsonText = json.encoder.py_encode_basestring(text)
jsonText = encoder.py_encode_basestring(text)
print(jsonText)
