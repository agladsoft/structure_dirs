import os
from functools import partial
from __init__ import list_dirs, root_directory

concat_root_path: partial = partial(os.path.join, root_directory)
make_directory: partial = partial(os.makedirs, exist_ok=True)

for path_items in map(concat_root_path, list_dirs):
    make_directory(path_items)
