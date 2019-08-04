import numpy as np
import pandas as pd

a=[]
n=int(input("Enter the number of elements:"))

for i in range(0,n):
  element=int(input("Enter element"+str(i+1)+":"))
  a.append(element)
  
x=pd.Series(a)

mean=x.mean()
median=x.median()
mode=x.mode()
std=x.std()

print("Mean",mean)
print("Median",median)
print("Mode",mode)
print("Standard Deviation",std)


------------------------------------------------------------------------------------------------------


OUTPUT:
Enter the number of elements:5
Enter element1:1
Enter element2:5
Enter element3:4
Enter element4:4
Enter element5:6
Mean 4.0
Median 4.0
Mode 0    4
dtype: int64
Standard Deviation 1.8708286933869707  
