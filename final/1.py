# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

E = 0.5
delta_E_1 = 0.01
delta_E_2 = 0.001
delta_E_3 = 0.0001
delta_x = 0.01
b = 2.0
psi_minus_one = 1.0
psi_zero = 1.0
show_psi = []
show_E = []
def V(x):
    if -1 <= x <= 1:
        return 0
    else:
        return 1000
for t in range(511):
    psi = []
    psi.append(psi_zero)
    temp = 2 * psi_zero - psi_minus_one - 2 * (E - V(0)) * (delta_x ** 2) * psi_zero
    psi.append(temp)
    i = 1
    while psi[-1] <= b and i <= 150:
        temp = 2 * psi[-1] - psi[-2] - 2 * (E - V(i * delta_x)) * (delta_x ** 2) * psi[-1]
        psi.append(temp)
        i = i + 1
    show_psi.append(psi)
    show_E.append(E)

    if 0.5 <= E < 1.0 or E >= 1.2:
        E = E + delta_E_1
    elif 1.0 <= E < 1.15 or 1.16 <= E < 1.2:
        E = E + delta_E_2
    elif 1.15<= E < 1.16:
        E = E + delta_E_3
    print E,t
    


f, ax = plt.subplots()
ax = plt.axes(title = 'Square Well - lowest even parity level',xlim = (-2,2), ylim = (-2,2),xlabel = 'x',ylabel = r'$\Psi$') 
p, = ax.plot([],[])

well_xl = []
well_xr = []
line_y = []
for j in range(100):
    well_xl.append(-1)
    well_xr.append(1)
    line_y.append(0)
well_y = np.linspace(-2,2,100)
line_x = np.linspace(-2,2,100)
plt.plot(well_xl,well_y,'r--')
plt.plot(well_xr,well_y,'r--')
plt.plot(line_x,line_y,'black')

def animate(i):
    
    x = []
    for j in range(-len(show_psi[i]) + 1,len(show_psi[i])):
        x.append(j * delta_x)
    y = []
    show_psi[i].reverse()
    for j in show_psi[i]:
        y.append(j)
    show_psi[i].reverse()
    show_psi[i]=show_psi[i][1:]
    y = y + show_psi[i]
    
    X = x
    Y = y
    p.set_data(X,Y)  
    
    plt.legend([p],['E = %.4f'%show_E[i]],loc='best')
    
    return p,  




gif = animation.FuncAnimation(f,animate,frames=511,interval=1)
plt.show()

