import os
from pathlib import Path
'''
    Author : Aman Adhav
    Date : 2017-12-29
    Project Name : Rename Code

    This code is a simply converts the extension of file to the one you desired.
    Example:
    >>> Directory Name : C:\\Pictures\\Hello
    >>> File Extension : jpg

    *** PLEASE NOTE : SOME FILE FORMATS WILL GET CORRUPTED IF THE FILE EXTENSION GETS CHANGED.
        SUCH AS : PDF -> JPG. PLEASE USE THIS CODE WITH CAUTION
    ***
'''

path = input("Directory Name : ")
exten = input("File Extension: ")

filenames = os.listdir(path)
extension = "."+ exten

for filename in filenames:
    if '.' in filename:
        print(path+"\\"+filename+"\n"+path+"\\"+filename[:filename.index('.')]+ extension)
        os.rename(path+"\\"+filename, path+"\\"+filename[:filename.index('.')]+ extension)
    
