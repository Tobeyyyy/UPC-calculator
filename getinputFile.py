from header import *

def getinputFile():
#	name = "C:\\Users\\lenovo-pc\\Google Drive\\Python\\Python36-32\\mytools\\UPCGenerator\\reference\\image2.csv"
	fileName="image2.csv"
	name=os.path.join(referenceFolder,fileName);
	name_list=[]
	header=''
	
	with open(name,newline='') as inputfile:
		readfile=csv.reader(inputfile);
		for row in readfile:
			if row[0] != 'item name':
				name_list.append([row[0]]);
			else:
				header=row;#save header of the file
	print("Success: open file",name)
	return(name_list,header)
	