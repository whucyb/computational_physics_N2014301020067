# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

L = 10
J = 1.0
k_B = 1.0

M = []
show_T = np.arange(1.5,4.1,0.1)
for T in show_T:
    s = []
    for i in range(L):
        s.append([])
        for j in range(L):
            s[i].append(1)
    t = 0
    M.append([1])
    

    
    m = random.randint(0,L - 1)
    n = random.randint(0,L - 1)
       
    while t < 30000:
        
        
        f = random.uniform(0,4)
        if 0 <= f < 1:
            if m + 1 <= L - 1:
                m = m + 1
            else:
                m = 0
        elif 1 <= f < 2:
            if m - 1 >= 0:
                m = m - 1
            else:
                m = L - 1
        elif 2 <= f < 3:
            if n + 1 <= L - 1:
                n = n + 1
            else:
                n = 0
        else:
            if n - 1 >= 0:
                n = n - 1
            else:
                n = L - 1
        
        a = 0
        b = 0
        c = 0
        d = 0
        if m - 1 < 0:
            a = s[L - 1][n]
        else:
            a = s[m - 1][n]
        if m + 1 > L - 1:
            b = s[0][n]
        else:
            b = s[m + 1][n]
        if n - 1 < 0:
            c = s[m][L - 1]
        else:
            c = s[m][n - 1]
        if n + 1 > L - 1:
            d = s[m][0]
        else:
            d = s[m][n + 1]
        E_flip = - 2 * J * s[m][n] * (a + b + c + d)
        if E_flip <= 0:
            s[m][n] = - s[m][n]
        else:
            r = random.uniform(0,1)
            if r <= np.exp(- E_flip / (k_B * T)):
                s[m][n] = - s[m][n]
        
        
        
        
        '''
        s_temp = []
        for i in range(L):
            s_temp.append([])
            for j in range(L):
                s_temp[i].append(s[i][j])
                
                
        for m in range(L):
            for n in range(L):
                f = random.randint(0,1)
                if f == 1:
                    a = 0
                    b = 0
                    c = 0
                    d = 0
                    if m - 1 < 0:
                        a = s_temp[L - 1][n]
                    else:
                        a = s_temp[m - 1][n]
                    if m + 1 > L - 1:
                        b = s_temp[0][n]
                    else:
                        b = s_temp[m + 1][n]
                    if n - 1 < 0:
                        c = s_temp[m][L - 1]
                    else:
                        c = s_temp[m][n - 1]
                    if n + 1 > L - 1:
                        d = s_temp[m][0]
                    else:
                        d = s_temp[m][n + 1]
                    E_flip = - 2.0 * J * s_temp[m][n] * (a + b + c + d)
                    if E_flip <= 0:
                        s[m][n] = - s[m][n]
                    else:
                        r = random.uniform(0,1)
                        if r <= np.exp(- E_flip / (k_B * T)):
                            s[m][n] = - s[m][n]
        '''
        
        M_total = 0
        for m in range(L):
            for n in range(L):
                M_total = M_total + s[m][n]
        
        M[-1].append(M_total / float(L ** 2))
        '''
        M[-1].append(M[-1][-1] + e * 2 * s[m][n] / float(L ** 2))
        '''
        t = t + 1
        
'''
X = range(30001)
Y = M[3]
plt.plot(X,Y)
'''
f, ax = plt.subplots()
ax = plt.axes(title = 'Ising model Magnetization versus time',xlim = (0,10000), ylim = (-2,2),xlabel = 'time',ylabel = 'Magnetization') 
p, = ax.plot([],[])



def animate(i):
    
   
    
    X = range(10001)
    Y = M[i][20000:]
    p.set_data(X,Y)  
    
    plt.legend([p],['T = %.2f'%show_T[i]],loc=1)
    
    return p,  




gif = animation.FuncAnimation(f,animate,frames=len(show_T),interval=1)
plt.show()
    
