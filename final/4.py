# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x_0 = 0.4
sigma2 = 0.001
c = 1.0 / (np.sqrt(np.pi * sigma2))
delta_t = 5 * (10 ** (-7))
delta_x = np.sqrt(delta_t / 2.0)

show_psi = []
show_psi2 = []

x = np.arange(0,1,delta_x)
print x
def V(x_v):
    return 0

print len(x)

psi_0 = []
psi_02 = []
for i in x:
    psi_0.append(c * np.exp(-((i - x_0) ** 2) / sigma2))
    psi_02.append((c * np.exp(-((i - x_0) ** 2) / sigma2)) ** 2)


show_psi.append(psi_0)
show_psi2.append(psi_02)
show_t = [0]

while show_t[-1] < 500.0 * (10 ** (-7)):
    show_psi.append([0])
    show_psi2.append([0])
    for i in range(1,1999):
        temp = show_psi[-2][i] + complex(0,1) * delta_t / 2.0 * (show_psi[-2][i + 1] + show_psi[-2][i - 1] - 2 * show_psi[-2][i]) / (delta_x ** 2) - complex(0,1) * delta_t * V(x[i]) * show_psi[-2][i]
        show_psi[-1].append(temp)
        temp2 = temp.real ** 2 + temp.imag ** 2
        show_psi2[-1].append(temp2)
    show_psi[-1].append(0)
    show_psi2[-1].append(0)
    show_t.append(show_t[-1] + delta_t)

f, ax = plt.subplots()
ax = plt.axes(title = 'Wave packet spreading',xlim = (0,1), ylim = (0,30),xlabel = 'x',ylabel = r'$\Psi ^ * \Psi$') 
p, = ax.plot([],[])



def animate(i):
    

    
    X = x
    Y = show_psi2[i]
    p.set_data(X,Y)  
    
    plt.legend([p],['t = %.2f * 10 ^ 3'%(show_t[i] * 1000)],loc='best')
    
    return p,  




gif = animation.FuncAnimation(f,animate,frames=len(show_t),interval=1)
plt.show()

