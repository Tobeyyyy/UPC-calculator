from header import *

class singleUPCgenerator:
	def __init__(self,upc_11):
		self.upc_11=upc_11
		self.resultUPC=self.get_UPC_12(self.upc_11)

	#-------UPC CALCULATED FUNCTION------------------------
	def roundup(self,a, digits=0):#round up function to round at ten digit.
		n = 10**-digits
		return round(math.ceil(a / n) * n, digits)

	def get_UPC_12(self,UPC_11):#get 12 digit UPC
		UPC_11=str(UPC_11)
		start_UPC_length=len(UPC_11)
		if re.match('0+',UPC_11):
			print('Error: Zero are not accepted.\nPlease enter 11 digits UPC')
		elif UPC_11 == '':#check input UPC to avoid 0 and empty
			print('Error: You must enter something.\nPlease enter 11 digits UPC')
			#print("Error: Zero and empty string are not accepted.\nPlease enter 11 digits UPC")
		elif len(UPC_11) != 11:
			error_message='You enter '+str(len(UPC_11))+' digits UPC.\nPlease enter 11 digits UPC.'
			print('Error: '+error_message);
		else:
			sum_old=0
			sum_even=0
			for i in range(0,start_UPC_length,2):
				sum_old=sum_old+int(UPC_11[i]);
				if ((i+1) < start_UPC_length):
					sum_even=sum_even+int(UPC_11[i+1]);
			sum_old_time_three=sum_old*3+sum_even
			round_up=self.roundup(sum_old_time_three,-1)
			diff_round_sum=round_up-sum_old_time_three
			result=UPC_11+str(diff_round_sum)
			#print(self.result)
			return(result)
	#-------END UPC CALCULATED FUNCTION------------------------
	