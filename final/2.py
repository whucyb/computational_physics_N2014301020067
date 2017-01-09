# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

E = 0
delta_E_1 = 0.01
delta_E_2 = 0.001
delta_E_3 = 0.0001
delta_E_4 = 1
delta_x = 0.01
psi_x_1 = 0.0
psi_x_2 = -0.0001 * delta_x
show_psi_l = []
show_psi_r = []
show_E = []

def V(x):
    v = 4 * 1.0 * (((1.0 / x) ** 12) - ((1.0 / x) ** 6))
    return v

for t in range(2001):
    psi_l = []
    x_l = 0.5
    psi_l.append(psi_x_1)
    temp = 2 * psi_x_1 - psi_x_2 - 2 * (E - V(x_l)) * (delta_x ** 2) * psi_x_1
    psi_l.append(temp)
    while x_l < 5:
        x_l = x_l + delta_x
        temp = 2 * psi_l[-1] - psi_l[-2] - 2 * (E - V(x_l)) * (delta_x ** 2) * psi_l[-1]
        psi_l.append(temp)
    
    psi_r = []
    x_r = 5.0
    psi_r.append(psi_x_1)
    temp = 2 * psi_x_1 - psi_x_2 - 2 * (E - V(x_r)) * (delta_x ** 2) * psi_x_1
    psi_r.append(temp)
    while x_r > 1:
        x_r = x_r - delta_x
        temp = 2 * psi_r[-1] - psi_r[-2] - 2 * (E - V(x_r)) * (delta_x ** 2) * psi_r[-1]
        psi_r.append(temp)
    
    show_psi_l.append(psi_l)
    show_psi_r.append(psi_r)
    show_E.append(E)
    
    E = E - delta_E_1
'''
    if 0.5 <= E < 1.0 or E >= 1.2:
        E = E + delta_E_1
    elif 1.0 <= E < 1.15 or 1.16 <= E < 1.2:
        E = E + delta_E_2
    elif 1.15<= E < 1.16:
        E = E + delta_E_3
    print E,t
'''    


f, ax = plt.subplots()
ax = plt.axes(title = 'Lennard - Jones potential',xlim = (0,5), ylim = (-1,2),xlabel = 'x',ylabel = r'$\Psi$') 
p1, = ax.plot([],[])
p2, = ax.plot([],[])

v_x = np.linspace(0.95,5,100)
v_y = []
for x_v in v_x:
    v_y.append(4 * 1.0 * (((1.0 / x_v) ** 12) - ((1.0 / x_v) ** 6)))
plt.plot(v_x,v_y,'r-.')

def animate(i):

    X_l = []
    for j in range(len(show_psi_l[i])):
        X_l.append(0.5 + j * delta_x)
    Y_l = show_psi_l[i]
    p1.set_data(X_l,Y_l)  
    
    X_r = []
    for j in range(len(show_psi_r[i])):
        X_r.append(5.0 - j * delta_x)
    Y_r = show_psi_r[i]
    p2.set_data(X_r,Y_r) 
    
    plt.legend([p1,p2],['E = ','%.4f'%show_E[i]],loc='best')
    
    return p1,




gif = animation.FuncAnimation(f,animate,frames=2001,interval=1)
plt.show()
