
def reader_data(filename):  
	#  read and load the txt file to a list 
	with open(filename) as fp:  
	   line = fp.readline()
	   list_ = []
	   while line:
	       list_.append(line.strip())
	       line = fp.readline()
	   return list_

