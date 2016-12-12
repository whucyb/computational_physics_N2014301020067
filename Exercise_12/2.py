# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def update_Jacobi(grid,L):

    delta_V = 0
    a=grid

    for i in range(L):    
        for j in range(L):
            if i==0 or j==0 or i==L-1 or j==L-1:
                pass
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(70/201)):
                pass
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(130/201)):
                pass
            else:
                voltage_new = (a[i+1][j]+a[i-1][j]+a[i][j+1]+a[i][j-1])/4
                voltage_old = a[i][j]
                delta_V += abs(voltage_new - voltage_old)
                grid[i][j] = voltage_new


    return grid, delta_V

def Jacobi(L):

    grid = []
    for i in range(L):
        row_i = []
        for j in range(L):
            if i==0 or j==0 or i==L-1 or j==L-1:
                voltage = 0
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(70/201)):
                voltage = 1
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(130/201)):
                voltage = -1
            else:
                voltage = 0
            row_i.append(voltage)
        grid.append(row_i)

    epsilon = 10**(-5)*(L-1)**2
    grid_init = grid
    delta_V = 0
    N_iter = 0

    while delta_V >= epsilon or N_iter <=5:
        grid_init, delta_V = update_Jacobi(grid_init,L)
        N_iter += 1

    return N_iter



def update_GS(grid,L):

    delta_V = 0

    for i in range(L):    
        for j in range(L):
            if i==0 or j==0 or i==L-1 or j==L-1:
                pass
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(70/201)):
                pass
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(130/201)):
                pass
            else:
                voltage_new = (grid[i+1][j]+grid[i-1][j]+grid[i][j+1]+grid[i][j-1])/4
                voltage_old = grid[i][j]
                delta_V += abs(voltage_new - voltage_old)
                grid[i][j] = voltage_new

    return grid, delta_V

def Gauss_Seidel(L):
    
    grid = []
    for i in range(L):
        row_i = []
        for j in range(L):
            if i==0 or j==0 or i==L-1 or j==L-1:
                voltage = 0
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(70/201)):
                voltage = 1
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(130/201)):
                voltage = -1
            else:
                voltage = 0
            row_i.append(voltage)
        grid.append(row_i)

    epsilon = 10**(-5)*(L-1)**2
    grid_init = grid
    delta_V = 0
    N_iter = 0

    while delta_V >= epsilon or N_iter <= 5:
        grid_init, delta_V = update_GS(grid_init,L)
        N_iter += 1

    return N_iter



def update_SOR(grid,L):

    delta_V = 0

    for i in range(L):    
        for j in range(L):
            if i==0 or j==0 or i==L-1 or j==L-1:
                pass
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(70/201)):
                pass
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(130/201)):
                pass
            else:
                voltage_new = (grid[i+1][j]+grid[i-1][j]+grid[i][j+1]+grid[i][j-1])/4
                voltage_old = grid[i][j]
                dV = voltage_new - voltage_old
                alpha = 2/(1+(np.pi/L))
                voltage_new = alpha*dV + voltage_old
                delta_V += abs(voltage_new - voltage_old)
                grid[i][j] = voltage_new

    return grid, delta_V

def SOR(L):
    
    grid = []
    for i in range(L):
        row_i = []
        for j in range(L):
            if i==0 or j==0 or i==L-1 or j==L-1:
                voltage = 0
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(70/201)):
                voltage = 1
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(130/201)):
                voltage = -1
            else:
                voltage = 0
            row_i.append(voltage)
        grid.append(row_i)

    epsilon = 10**(-5)*(L-1)**2
    grid_init = grid
    delta_V = 0
    N_iter = 0

    while delta_V >= epsilon or N_iter <= 5:
        grid_init, delta_V = update_SOR(grid_init,L)
        N_iter += 1

    return N_iter
        
l = []
N = []
ll = []
NN = []
lll=[]
NNN=[]
for i in range(10,61):
    l.append(i*i)
    ll.append(i*i)
    lll.append(i)
    N.append(Jacobi(i))
    NN.append(Gauss_Seidel(i))
    NNN.append(SOR(i))

plt.subplot(131)
plt.plot(l,N,'.-',label='Jacobi')
plt.legend(loc='best')
plt.xlabel(r'$L^2$')
plt.ylabel(r'$N_iter$')
plt.xlim(0,3700)
plt.title(r'$N_iter$ versus $L^2$')
plt.subplot(132)
plt.plot(ll,NN,'.-',label='Gauss-Seidel')
plt.legend(loc='best')
plt.xlabel(r'$L^2$')
plt.ylabel(r'$N_iter$')
plt.xlim(0,3700)
plt.title(r'$N_iter$ versus $L^2$')
plt.subplot(133)
plt.plot(lll,NNN,'.-',label='SOR')
plt.legend(loc='best')
plt.xlabel('L')
plt.ylabel(r'$N_iter$')
plt.xlim(0,70)
plt.title(r'$N_iter$ versus L')
plt.show()
