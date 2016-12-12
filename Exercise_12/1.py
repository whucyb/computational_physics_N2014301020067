# -*- coding: utf-8 -*-
import numpy as np 
import matplotlib.cm as cm
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from copy import deepcopy
v = []
for i in range(101):    
    row_i = []
    for j in range(101):
        if i == 0 or i == 100 or j == 0 or j == 100:
            voltage = 0
        elif 35<=i<=65 and 35<=j<=65:
            voltage = 1
        else:
            voltage = 0
        row_i.append(voltage)
    v.append(row_i)
def update_V(v):
    delta_V = 0
    for i in range(101):    
        for j in range(101):
            if i == 0 or i == 100 or j == 0 or j == 100:
                pass
            elif 35<=i<=65 and 35<=j<=65:
                pass
            else:
                voltage_new = (v[i+1][j]+v[i-1][j]+v[i][j+1]+v[i][j-1])/4.0
                voltage_old = v[i][j]
                delta_V += abs(voltage_new - voltage_old)
                v[i][j] = voltage_new
    return v, delta_V
def Laplace_calculate(v):   
    epsilon = 10**(-5)*101**2
    delta_V = 0
    N_iter = 0
    while delta_V >= epsilon or N_iter <= 10:
        v, delta_V = update_V(v)
        N_iter += 1
    return v
x = np.linspace(-1,1,101)
y = np.linspace(-1,1,101)
X, Y = np.meshgrid(x, y)
Z = Laplace_calculate(v)
Ex = deepcopy(Z)
Ey = deepcopy(Z)
E = deepcopy(Z)
for i in range(101):
    for j in range(101):
        if i == 0 or i == 100 or j == 0 or j == 100:
            Ex[i][j] = 0
            Ey[i][j] = 0
        else:
            Ex_value = -(Z[i+1][j] - Z[i][j])/2
            Ey_value = -(Z[i][j+1] - Z[i][j])/2
            Ex[i][j] = Ex_value
            Ey[i][j] = Ey_value
for i in range(101):
    for j in range(101):
        E_value = np.sqrt(Ex[i][j]**2 + Ey[i][j]**2)
        E[i][j] = E_value
plt.figure()
CS = plt.contour(X,Y,Z, 20, alpha=1, cmap=cm.jet_r)
plt.clabel(CS, inline=1, fontsize=12)
plt.title('Electric potential')
plt.xlabel('x')
plt.ylabel('y')
fig = plt.figure()
ax = Axes3D(fig)
surf=ax.plot_surface(X, Y, Z,rstride=1, cstride=1, cmap=cm.hsv,linewidth=0, antialiased=False) 
ax.set_xlabel('x') 
ax.set_ylabel('y')
ax.set_title('Electric potential') 
fig.colorbar(surf,shrink=0.5,aspect=5)
fig0, ax0 = plt.subplots()
strm = ax0.streamplot(X, Y, np.array(Ey), np.array(Ex), color=np.array(E), linewidth=1,cmap=cm.gist_rainbow_r)
ax0.set_xlabel('x')
ax0.set_ylabel('y')
ax0.set_xlim(-1,1)
ax0.set_ylim(-1,1)
ax0.set_title('Electric field')
plt.show()
