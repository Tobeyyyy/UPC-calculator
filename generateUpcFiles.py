from header import *


def get_UPC_12_list(name_list,num_of_UPC,start_UPC):
	name_list_length=len(name_list)*num_of_UPC;
	start_UPC=int(start_UPC)
	UPC_list=[];
	m=0
	for i in range(0,name_list_length):
		upcObject=singleUPCgenerator(start_UPC)
		UPC_12=upcObject.resultUPC;
		#UPC_list.append(int(UPC_12))
		start_UPC=start_UPC+1;
		m=math.floor(i/num_of_UPC);
		name_list[m].append(str(UPC_12))
	#print(name_list)
	display_result=[]
	for x in name_list:
		for i in range(1,len(x)):
			temp_11=x[i][0:11]
			temp=str(temp_11)+' -> '+str(x[i])+'\n'
			display_result.append(temp)

	#----show result to User interface----
	return(name_list)
		

def generateUpcFiles(startupc,header,name_list):
	startpoint_UPC_11=str(startupc)
	num_of_UPC=len(header)-1;
	print("You have "+str(num_of_UPC)+" UPCs for each items")
	list=get_UPC_12_list(name_list,num_of_UPC,startpoint_UPC_11)
	list.insert(0, header)#insert header at the head of list
	outputFileName=today+"_upc_output.csv"
#	address="C:\\Users\\lenovo-pc\\Google Drive\\Python\\Python36-32\\mytools\\output"
	outputfile=os.path.join(outputFolder,outputFileName);
	with open(outputfile,'w') as output:
		wri=csv.writer(output,lineterminator='\n');
		wri.writerows(list);
	output.close()
	print('You have generated new UPC in total:',(len(list)-1)*num_of_UPC)
	print('Last From:',startpoint_UPC_11)
	print('Last End :',int(startpoint_UPC_11)+(len(name_list)-1)*num_of_UPC-1)
	print('Last End :',int(startpoint_UPC_11)+(len(name_list)-1)*num_of_UPC)
	print("UPC output file: ",outputfile)
	return (list)