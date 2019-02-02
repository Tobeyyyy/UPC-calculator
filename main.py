#!/usr/bin/python
from header import *

#user interface for UPC generator

singleUpcRequest=input("Do you want to generate one upc or upc file? 1.one upc/2.upc file\n")
if singleUpcRequest=='1':
	stop='1'
	while(stop=="1"):
		singleUpc=input("input upc:\n")
		p1=singleUPCgenerator(singleUpc)#p1 is an object
		if p1.resultUPC:
			print("Result: "+p1.resultUPC)
		stop=input("[Enter 0.quit 1.continue]\n")
		if (stop!="1"):
			print("Program is quitted")

elif singleUpcRequest=='2':
	commandGeneratefile()

