import numpy as np

#mylist = [13,22,45,52,63,25]

mylist = [10,11,12,13,14,15]
ele = 12
flag = 0
for i in mylist:
    if (i== ele):
        print("Element found")
        flag=1
        break
if(flag==0):
        print("Element not found")
        
