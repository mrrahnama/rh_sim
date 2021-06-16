import csv
from agents import  Product
import numpy as np
from numpy.polynomial.polynomial import polyval2d
x=0
while x>-1:
    x=float(input("enter x"))
    y=float(input("enter y"))
    c="[[1,2,3],[1,2,3],[1,2,3]]"
    c=np.array(eval(c))
    yy=polyval2d(x,y,c)
    print()
    print("y is :"+str(yy))
d={}
inventory= {}
def strategy(step=0):
    print("strategy function")
# with open('filr.csv',newline='', encoding='utf-8') as f:
#     infile=csv.DictReader(f,fieldnames=["name","minvalue","count"])
#     for row in infile:
#         inventory[row["name"]]=Product(name=row["name"], minvalue=float(row["minvalue"]), available=row["count"])
# print((inventory["4"].name))
# print(d)
if hasattr(strategy, "__call__"):
    strategy()