import numpy as np

def write2file(header,data,column,filename,string): #writes selected elements of list into file.
	document=open(filename,string)
	if string=="a":
		document.write("\n")
	document.write(header[0]+" "+header[column]+"\n")
	for x in range(0,len(data)):
		document.write(data[x][0]+" "+data[x][column]+"\n")
	document.close()
	print("Data printed to file:",filename)

def write2array(data,column): #turns selected elements from list into [ix2] matrix.
	array=[[0]*2]*len(data)
	for x in range(0,len(data)):
		array[x]=[data[x][0],data[x][column]]
	array=np.array(array).astype(int)
	return array

def array2list(matrix): #turns [ix2] array into list.
	data=[]
	for x in range(0,len(matrix)):
		data.append([matrix[x][0],matrix[x][1]])
	return data

