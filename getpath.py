# this is a little function that gets a path 
# that has been inputed into the Windows 
# command line via drag and drop

import os

def getpath():

	valid_path = False 

	while valid_path == False:
		
		file_path = input()
			
		if file_path.startswith('"') and file_path.endswith('"'):
			file_path = file_path[1:-1]

		if os.path.exists(file_path):
			valid_path = True
		else:
			print("Invalid path, please try again!")

	return file_path