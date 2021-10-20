from collections import defaultdict
from os import umask

# In a more innocent time of my 
# life, I would create collections 
# as values under a related key.
# For example, I would glob a set of 
# files, and group the paths into a list 
# based on the first 12 digits of the 
# file name (unit id). To do this, I create
# an empty dictionary, check if a key was present,
# and either append the list or update the 
# dictionary with a new key and list with the
# first value.

import pathlib

unit_paths = {}
for file_path in pathlib.Path('somepath').glob('*.csv'):
    unit_id = file_path.stem[:12]
    if unit_id in unit_paths:
        unit_paths[unit_id].append(file_path)
    else:
        unit_paths.update(
            {unit_id: [file_path]}
        )

# With defaultdict, you initialize
# the dict with a default value of list,
# and you can dramatically simplify the code.

from collections import defaultdictdefaultdict

dunit_paths = defaultdict(list)

for file_path in pathlib.Path('somepath').glob ('*.csv'):
    unit_id = file_path.stem[:12]
    dunit_paths[unit_id].append(file_path)

