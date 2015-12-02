

def ext(data,column,string): #extracts selected elements from list.
	new_data=[]
	for x in range(0,len(data)):
		if data[x][column]==string:
			new_data.append(data[x])
	return new_data