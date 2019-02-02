from header import *

def commandGeneratefile():
	name_list,header=getinputFile()
	if name_list[0][0:3]=="M2R":
		startupc=getStartpoint('858')#m2r item and 8pin upc startwith 858;
	else:
		startupc=getStartpoint('885')#m2r item and 8pin upc startwith 858;
#	print("UPC Start from: "+str(startupc))
	upcList=generateUpcFiles(startupc,header,name_list)
	GenerateRfsmartFile(upcList,name_list)
