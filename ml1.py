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

 
