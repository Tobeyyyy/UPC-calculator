import sys
import math
import csv
import openpyxl
from openpyxl import Workbook
import os
import re
import datetime

x = datetime.datetime.now()
today=str(x.year)+str(x.month)+str(x.day)

referenceFolder='C:\\Users\\melody\\AppData\\Local\\Programs\\Python\\Python36-32\\mytools\\UPCGenerator\\reference'
outputFolder='C:\\Users\\melody\\AppData\\Local\\Programs\\Python\\Python36-32\\mytools\\output'

UPCOriginalFileFolder="Z:\\Wayne"
copyUPCFileToFolder="C:\\Users\\melody\\Desktop"
'''
#my computer
referenceFolder='C:\\Users\\lenovo-pc\\Google Drive\\Python\\Python36-32\\mytools\\UPCGenerator\\reference'
outputFolder='C:\\Users\\lenovo-pc\\Google Drive\\Python\\Python36-32\\mytools\\output'

UPCOriginalFileFolder="C:\\Users\\Desktop"
copyUPCFileToFolder="C:\\Users\\Desktop"
'''

from shutil import copyfile

from singleUPCgenerator import *
from getStartpoint import *
from getinputFile import *
from generateUpcFiles import *
from GenerateRfsmartFile import *

from commandGeneratefile import *


