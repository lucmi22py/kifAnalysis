import csv
import os
import pprint

class kif_handle_class:
	dst_full_path = "hogehoge.txt"
	dst_path = dst_full_path.split('.')[0]
	dst_file = dst_full_path.split('.')[1]
	
	def __init__(self, full_path):
		self.full_path = full_path
		dst_path = "hoge"
		src_path = "fuga"
		
	def csv_control(full_path, src_path):
		with open(full_path) as f:
		reader = csv.reader(f)
		for row in reader:
			print (row)

print(kif_handle_class.dst_file)
