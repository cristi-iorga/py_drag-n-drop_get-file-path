# py_drag-n-drop_get-file-path

A simple function for getting a file/folder path via drag and drop in the windows command line

Example of use in a python exec. file which runs without a GUI:

\\

import getpath

print("Drag and drop a file here and press Enter: ")

file_path = getpath.getpath()

open(file_path, 'r') \...\ etc.

\\

There probably is a better way to do this, but I'm a rookie and I'm proud of this :)
