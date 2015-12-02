import csv as csv
import numpy as np

def reddit(c,d): #reads csv's from selected file.
	print("Importing data from",c)	
	csv_file_object = csv.reader(open(c),delimiter=d)
	header = next(csv_file_object)
	data = []
	for row in csv_file_object:
		data.append(row)

	return [header,data]