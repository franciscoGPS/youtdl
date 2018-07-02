import os.path as path
import ipdb
import csv
class Filesystem():
	#This method stores the passed data to the default video id's file

	def __init__(self, filename, open_mode):
		self.open_mode = open_mode
		self.file = filename

	def save_default( self, txt, EOL="" ):
		save_path = path.dirname(path.abspath(__file__))
		name_of_file = self.file
		completeName = path.join(save_path, name_of_file+".txt")
		file1 = open(completeName, self.open_mode)
		file1.write(txt+""+EOL+"\n")
		file1.close()

	def print_path(self):
		save_path = path.dirname(path.abspath(__file__))
		completeName = path.join(save_path, self.file+".txt")
		print(completeName)


	def file_to_list(self):
		#list_of_lists = []
		save_path = path.dirname(path.abspath(__file__))
		completeName = path.join(save_path, self.file+".txt")
		file1 = open(completeName, self.open_mode)
		#list_of_lists = file1.splitlines()
		list_of_songs = [line.split('\n') for line in file1.readlines()]
		file1.close()
		return list_of_songs

	def make_ids_table(self, file_name, array):
		save_path = path.dirname(path.abspath(__file__))
		completeName = path.join(save_path, self.file+".txt")
    	
		file1 = open(completeName, self.open_mode)
		csvWriter = csv.writer(file1,delimiter=',')
		csvWriter.writerows(array)
		file1.close()
    	
    	


