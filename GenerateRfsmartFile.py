from header import *

case={}
pack={}
result=[]
def	GenerateRfsmartFile(upcList,name_list):
	for x in upcList:
		if x[0] !='item name':
			pack[x[0]]=[x[0],x[2]]
			case[x[0]]=[x[0],x[3]]
	name="list.csv"
	refeFile=os.path.join(referenceFolder,name);
	with open(refeFile,encoding="utf8", errors='ignore') as inputfile:
		readfile=csv.reader(inputfile);
		for row in readfile:
			if row[1] in pack.keys():
				pack[row[1]]=[row[0],pack[row[1]][1],row[22]]
				case[row[1]]=[row[0],pack[row[1]][1],row[22]]
	for key,value in pack.items():
		if value[2]=="Universal Unit Type 1":
			value[2]="Pk(6)"
			case[key][2]="120"
		result.append(value)
		result.append(case[key])
	inputfile.close()
#	print("Success: open file",refeFile)
#	print(case)
	
	outputFileName=today+"_upc_rfsmart.csv"
#	address="C:\\Users\\lenovo-pc\\Google Drive\\Python\\Python36-32\\mytools\\output"
	outputfile=os.path.join(outputFolder,outputFileName);
	with open(outputfile,'w') as output:
		wri=csv.writer(output,lineterminator='\n');
		wri.writerows(result);
	output.close()
	print("RF-Smart output file: ",outputfile)
		