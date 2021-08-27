import csv
from agents import  Product
import numpy as np
import sympy
from numpy.polynomial.polynomial import polyval2d


def fix_power_sign( equation):
    return equation.replace("^", "**")




def eval_polynomial( equation, x_value, y_value=None):
    fixed_equation = fix_power_sign(equation.strip())
    parts = fixed_equation.split("+")
    x_str_value = str(x_value)
    parts_with_values = (part.replace("x", x_str_value) for part in parts)
    if y_value is not None :
        y_str_value =str(y_value)
        parts_with_values = (part.replace("y", y_str_value) for part in parts_with_values)
    partial_values = (eval(part) for part in parts_with_values)
    return sum(partial_values)
# x=0
# lista=["(2*x)^4+3*x+1*x^2"]
# res=eval_polynomial(str(lista[0]),2)
# print("res : "+str(res))
# while x > -1 :
#     # x=float(input("enter x"))
#
#     my_poly = input("enter poly")
#     x = float(input("enter x"))
#     res=eval_polynomial(my_poly,x)
#     # x = sympy.Symbol('x')
#     # my_poly = sympy.polys.polytools.poly_from_expr(my_poly)[0]
#     # a, b, c = my_poly.coeffs()
#     # y=float(input("enter y"))
#     # c="[[1,2,3],[1,2,3],[1,2,3]]"
#     # c=np.array(eval(c))
#     # yy=polyval2d(x,y,c)
#     print("y is :"+str(res))
# d={}
# inventory= {}
# def strategy(step=0):
#     print("strategy function")
# # with open('filr.csv',newline='', encoding='utf-8') as f:
# #     infile=csv.DictReader(f,fieldnames=["name","minvalue","count"])
# #     for row in infile:
# #         inventory[row["name"]]=Product(name=row["name"], minvalue=float(row["minvalue"]), available=row["count"])
# # print((inventory["4"].name))
# # print(d)
# if hasattr(strategy, "__call__"):
#     strategy()
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def newImg():
    img = Image.new('RGB', (100, 100))
    for i in range(40):
        img.putpixel((30,60-i), (155,155,55))
        img.putpixel((31,60-i), (155,155,55))
        img.putpixel((32,60-i), (155,155,55))
    img.save('sqr.png')

    return img
import numpy as np
import h5py
import scipy.io
import matplotlib.pyplot as plt

#-- Generate Data -----------------------------------------
# Using linspace so that the endpoint of 360 is included...
data=scipy.io.loadmat('FLS_DATA_MATRIX.mat')['FLS_DATA_MATRIX']
data=np.transpose(data)
azimuths = np.radians(np.arange(0, 180))
zeniths = np.arange(0, 119)

r, theta = np.meshgrid(zeniths, azimuths)
values = np.random.random((azimuths.size, zeniths.size))
# values = np.zeros((azimuths.size, zeniths.size))
# values=np.random.random((2,2))
#-- Plot... ------------------------------------------------
fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
ax.pcolormesh(theta, r, data)
ax.set_theta_zero_location("W")
rmin=20
ax.set_rorigin(-rmin)
ax.set_thetamin(45)
ax.set_thetamax(135)
ax.set_theta_direction( -1 )
# ax.set_rgrids(np.arange(10,80,20))
# ax2.set_theta_offset(np.pi/2)

# ax.set_rticks(np.arange(15, 90, 8))
# ax.set_rticks(np.arange(15, 90, 8))
# ax.set_thetagrids(np.arange(45, 135, 22.5),['a','b','c','d'])
# ax.set_rlim(10,60)
ax.set_rmin(rmin)
ax.set_rmax(100)
# ax.set_thetagrids([theta * 30 for theta in range(360//30)])
plt.grid(color = 'yellow', linestyle = '--', linewidth = 0.5)
plt.show()