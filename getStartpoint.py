from header import *

def getStartpoint(option):
#	src="C:\\Users\\lenovo-pc\\Google Drive\\Python\\Python36-32"
	orifile=os.path.join(UPCOriginalFileFolder,'UPC.xlsx');
#	destaddress='C:\\Users\\lenovo-pc\\Desktop'
	destfile=os.path.join(copyUPCFileToFolder,'UPC.xlsx');
	copyfile(orifile,destfile)	
	input_file=openpyxl.load_workbook(destfile);#input_file is a WorkBook object
	sheet_name=input_file.sheetnames;
	sheet=input_file[sheet_name[0]];
	if option=='885':
		startpoint=sheet.cell(4,2).value
	elif option =='858':
		startpoint=sheet.cell(4,3).value
	return(startpoint)
		