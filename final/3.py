# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

delta_psi = 0.01
delta_x = 0.05

show_psi = []
show_E = []

psi_0 = []
x = np.arange(-1.3,1.31,0.05)
for i in range(len(x)):
    if 6 <= i <= 46:
        psi_0.append(np.sqrt(2) / 2.0)
    else:
        psi_0.append(0)

show_psi.append(psi_0)

def V(x):
    if -1 <= x <= 1:
        return 0
    else:
        return 1000

a = 0
b = 0       
for i in range(1,52):
    da = show_psi[-1][i] * (- 0.5 * (show_psi[-1][i + 1] + show_psi[-1][i - 1] -2 * show_psi[-1][i]) / (delta_x ** 2) + V(x[i]) * show_psi[-1][i])
    db = show_psi[-1][i] ** 2
    a = a + da
    b = b + db
E_0 = float(a) / float(b)

show_E.append(E_0)

    
for t in range(10000):
    psi_new = show_psi[-1]

    f_1 = 0    
    while f_1 == 0:
        r_1 = random.uniform(0,1)
        r_2 = random.uniform(0,1)
        random_i = int(r_1 * 51) + 1
        if r_2 <= psi_new[random_i] / max(psi_new):
            f_1 = 1
        else:
            f_1 = 0
    
    
    f_2 = random.randint(0,1)
    if f_2 == 0 or psi_new[random_i] - delta_psi < 0:    
        psi_new[random_i] = psi_new[random_i] + delta_psi
    else:
        psi_new[random_i] = psi_new[random_i] - delta_psi
    a = 0
    b = 0       
    for i in range(1,52):
        da = psi_new[i] * (- 0.5 * (psi_new[i + 1] + psi_new[i - 1] -2 * psi_new[i]) / (delta_x ** 2) + V(x[i]) * psi_new[i])
        db = psi_new[i] ** 2
        a = a + da
        b = b + db
    E_new = float(a) / float(b)
    if E_new < show_E[-1]:
        show_psi.append(psi_new)
        show_E.append(E_new)
    else:
        show_psi.append(show_psi[-1])
        show_E.append(show_E[-1])



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
    
    
    y = show_psi[i]
    X = x
    Y = y
    p.set_data(X,Y)  
    
    plt.legend([p],['E = %.4f'%show_E[i]],loc='best')
    
    return p,  




gif = animation.FuncAnimation(f,animate,frames=10000,interval=1)
plt.show()
