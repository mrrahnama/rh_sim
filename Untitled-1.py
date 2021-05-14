import csv
from agents import  Product
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