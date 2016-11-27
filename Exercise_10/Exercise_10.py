# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
class elliptical_orbit(object):
    def __init__(self,a,e,beta,tlim):
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.dt = 0.001
        self.t = []
        self.T = []
        self.a = a
        self.e = e
        self.beta = beta
        self.tlim = tlim
        self.c = []
    def calculate(self):
        self.x.append((1 + self.e) * self.a)
        self.y.append(0)
        self.vx.append(0)
        self.vy.append(np.sqrt((4 * (np.pi ** 2) * (1 - self.e)) / (self.a * (1 + self.e))))
        self.t.append(0)
        while (self.t[-1] < self.tlim):
            temp_r = np.sqrt(self.x[-1] ** 2 + self.y[-1] ** 2)
            self.vx.append(self.vx[-1] - 4 * (np.pi ** 2) * self.x[-1] / (temp_r ** (self.beta + 1)) * self.dt)
            self.vy.append(self.vy[-1] - 4 * (np.pi ** 2) * self.y[-1] / (temp_r ** (self.beta + 1)) * self.dt)
            self.x.append(self.x[-1] + self.vx[-1] * self.dt)
            self.y.append(self.y[-1] + self.vy[-1] * self.dt)
            self.t.append(self.t[-1] + self.dt)
            if (self.beta == 2.00 and self.x[-1] > 0 and self.y[-1] >= 0 and self.y[-2] <= 0 and self.t[-2] > 0):
                self.T.append((self.t[-1] + self.t[-2]) * 0.5)
        if (self.beta == 2.00):
            T_average = 0
            for i in range(len(self.T)):
                T_average = T_average + self.T[i] / (float(i) + 1)
            T_average = T_average / float(len(self.T))
            self.c.append(T_average ** 2 / self.a ** 3)
    def show_results_1(self):
        plt.scatter(0,0,c = 'r',s = 500)
        p, = plt.plot(self.x,self.y)
        plt.title('Simulation of elliptical orbit')
        plt.xlabel('x (AU)')
        plt.ylabel('y (AU)')
        plt.xlim(-5,20)
        plt.ylim(-10,10)
        plt.legend([p],['a = %.1f  e = %.1f'%(self.a,self.e) + r'  $T^2/a^3$' + ' = %.10f'%self.c[0]],loc = 'best')
        plt.show()
    def show_results_2(self):
        plt.scatter(0,0,c = 'r',s = 100)
        p, = plt.plot(self.x,self.y,'.')
        plt.title('Simulation of elliptical orbit')
        plt.xlabel('x (AU)')
        plt.ylabel('y (AU)')
        plt.xlim(-1,1)
        plt.ylim(-1,1)
        plt.legend([p],[r'$\beta$' + ' = %.2f'%self.beta],loc = 'best')
        plt.show()
