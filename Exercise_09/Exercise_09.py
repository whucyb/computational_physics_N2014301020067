# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
class square_table(object):
    def __init__(self,x_0,y_0,v_0,theta_0):
        self.x = [x_0]
        self.y = [y_0]
        self.v_x = [v_0 * np.cos(theta_0)]
        self.v_y = [v_0 * np.sin(theta_0)]
        self.x_phase_space = []
        self.v_x_phase_space = []
        self.dt = 0.01
    def calculate(self):
        for i in range(10 ** 6):
            temp_x = self.x[-1] + self.v_x[-1] * self.dt
            temp_y = self.y[-1] + self.v_y[-1] * self.dt
            if (temp_x >= 1 or temp_y >= 1 or temp_x <= -1 or temp_y <= -1):
                s = 0
                while (1):
                    temp_x = self.x[-1] + self.v_x[-1] * self.dt * 0.01
                    temp_y = self.y[-1] + self.v_y[-1] * self.dt * 0.01
                    if (temp_x >= 1 and - temp_x < temp_y < temp_x):
                        s = 1
                        break
                    elif (temp_y >= 1 and temp_y > - temp_x and temp_y > temp_x):
                        s = 2
                        break
                    elif (temp_x <= -1 and temp_x < temp_y < - temp_x):
                        s = 3
                        break
                    elif (temp_y <= -1 and temp_y < - temp_x and temp_y < temp_x):
                        s = 4
                        break
                    elif (temp_x >= 1 or temp_y >= 1) and (temp_y == temp_x or temp_y == - temp_x):
                        s = 5
                        break
                    self.x.append(temp_x)
                    self.y.append(temp_y)
                    self.v_x.append(self.v_x[-1])
                    self.v_y.append(self.v_y[-1])
                if s == 1:
                    k = float(self.y[-1] - temp_y) / float(self.x[-1] - temp_x)
                    self.x.append(1)
                    self.y.append(k * (1.0 - self.x[-1]) + self.y[-1])
                    self.v_x.append(- self.v_x[-1])
                    self.v_y.append(self.v_y[-1])
                elif s == 2:
                    k = float(self.y[-1] - temp_y) / float(self.x[-1] - temp_x)
                    self.y.append(1)
                    self.x.append((1.0 - self.y[-1]) / k + self.x[-1])
                    self.v_x.append(self.v_x[-1])
                    self.v_y.append(- self.v_y[-1])
                elif s == 3:
                    k = float(self.y[-1] - temp_y) / float(self.x[-1] - temp_x)
                    self.x.append(-1)
                    self.y.append(k * (-1.0 - self.x[-1]) + self.y[-1])
                    self.v_x.append(- self.v_x[-1])
                    self.v_y.append(self.v_y[-1])
                elif s == 4:
                    k = float(self.y[-1] - temp_y) / float(self.x[-1] - temp_x)
                    self.y.append(-1)
                    self.x.append((-1.0 - self.y[-1]) / k + self.x[-1])
                    self.v_x.append(self.v_x[-1])
                    self.v_y.append(- self.v_y[-1])
                elif s == 5:
                    if (temp_x >= 0 and temp_y >= 0):
                        self.x.append(1)
                        self.y.append(1)
                    elif (temp_x <= 0 and temp_y >= 0):
                        self.x.append(-1)
                        self.y.append(1)
                    elif (temp_x <= 0 and temp_y <= 0):
                        self.x.append(-1)
                        self.y.append(-1)
                    elif (temp_x >= 0 and temp_y <= 0):
                        self.x.append(1)
                        self.y.append(-1)
                    self.v_x.append(- self.v_x[-1])
                    self.v_y.append(- self.v_y[-1])
            else:
                self.x.append(temp_x)
                self.y.append(temp_y)
                self.v_x.append(self.v_x[-1])
                self.v_y.append(self.v_y[-1])
        for i in range(len(self.y)):
            if np.abs(self.y[i]) < 0.0001:
                self.x_phase_space.append(self.x[i])
                self.v_x_phase_space.append(self.v_x[i])
    def show_results(self):
        plt.subplot(121)
        l = np.arange(-1,1.01,0.01)
        L_1 = []
        for i in range(len(l)):
            L_1.append(1)
        L_2 = []
        for i in range(len(l)):
            L_2.append(-1)
        plt.plot(L_1,l,'b')
        plt.plot(l,L_1,'b')
        plt.plot(L_2,l,'b')
        plt.plot(l,L_2,'b')
        plt.plot(self.x[:10 ** 4],self.y[:10 ** 4],'g')
        plt.title('Square table - trajectory')
        plt.xlim(-1.1,1.1)
        plt.ylim(-1.1,1.1)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.subplot(122)
        plt.plot(self.x_phase_space,self.v_x_phase_space,'.')
        plt.title('Square table - phase space plot')
        plt.xlabel('x')
        plt.ylabel(r'$v_x$')
        plt.show()
class circular_stadium(object):
    def __init__(self,x_0,y_0,v_0,theta_0):
        self.x = [x_0]
        self.y = [y_0]
        self.v_x = [v_0 * np.cos(theta_0)]
        self.v_y = [v_0 * np.sin(theta_0)]
        self.x_phase_space = []
        self.v_x_phase_space = []
        self.dt = 0.01
    def calculate(self):
        for i in range(10 ** 6):
            temp_x = self.x[-1] + self.v_x[-1] * self.dt
            temp_y = self.y[-1] + self.v_y[-1] * self.dt
            if (temp_x ** 2 + temp_y **2) >= 1:
                while (1):
                    temp_x = self.x[-1] + self.v_x[-1] * self.dt * 0.01
                    temp_y = self.y[-1] + self.v_y[-1] * self.dt * 0.01
                    if (temp_x ** 2 + temp_y **2) >= 1:
                        break
                    self.x.append(temp_x)
                    self.y.append(temp_y)
                    self.v_x.append(self.v_x[-1])
                    self.v_y.append(self.v_y[-1])
                self.x.append(temp_x / np.sqrt(temp_x ** 2 + temp_y ** 2))
                self.y.append(temp_y / np.sqrt(temp_x ** 2 + temp_y ** 2))
                temp_v_n = self.x[-1] * self.v_x[-1] + self.y[-1] * self.v_y[-1]
                temp_v_x = self.v_x[-1] - 2 * temp_v_n * self.x[-1]
                temp_v_y = self.v_y[-1] - 2 * temp_v_n * self.y[-1]
                self.v_x.append(temp_v_x)
                self.v_y.append(temp_v_y)
            else:
                self.x.append(temp_x)
                self.y.append(temp_y)
                self.v_x.append(self.v_x[-1])
                self.v_y.append(self.v_y[-1])
        for i in range(len(self.y)):
            if np.abs(self.y[i]) < 0.0001:
                self.x_phase_space.append(self.x[i])
                self.v_x_phase_space.append(self.v_x[i])
    def show_results(self):
        plt.subplot(121)
        Theta = np.arange(0,2 * np.pi,0.01)
        plt.plot(np.cos(Theta),np.sin(Theta))
        plt.plot(self.x[:10 ** 4],self.y[:10 ** 4])
        plt.title('Circular stadium - trajectory')
        plt.xlim(-1,1)
        plt.ylim(-1,1)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.subplot(122)
        plt.plot(self.x_phase_space,self.v_x_phase_space,'.')
        plt.title('Circular stadium - phase space plot')
        plt.xlabel('x')
        plt.ylabel(r'$v_x$')
        plt.show()
class stadium_billiard(object):
    def __init__(self,x_0,y_0,v_0,theta_0,alpha):
        self.alpha = alpha * 2
        self.x = [x_0]
        self.y = [y_0 + alpha / 2.0]
        self.v_x = [v_0 * np.cos(theta_0)]
        self.v_y = [v_0 * np.sin(theta_0)]
        self.x_phase_space = []
        self.v_x_phase_space = []
        self.dt = 0.01
    def calculate(self):
        for i in range(10 ** 6):
            temp_x = self.x[-1] + self.v_x[-1] * self.dt
            temp_y = self.y[-1] + self.v_y[-1] * self.dt
            if ((temp_x ** 2 + (temp_y - self.alpha / 2.0) **2) >= 1 and temp_y > (self.alpha / 2.0))\
               or ((temp_x ** 2 + (temp_y + self.alpha / 2.0) **2) >= 1 and temp_y < - (self.alpha / 2.0))\
               or (- (self.alpha / 2.0) < temp_y < (self.alpha / 2.0) and temp_x < -1)\
               or (- (self.alpha / 2.0) < temp_y < (self.alpha / 2.0) and temp_x > 1):
                s = 0
                while (1):
                    temp_x = self.x[-1] + self.v_x[-1] * self.dt * 0.01
                    temp_y = self.y[-1] + self.v_y[-1] * self.dt * 0.01
                    if (temp_x ** 2 + (temp_y - self.alpha / 2.0) **2) >= 1 and temp_y > (self.alpha / 2.0):
                        s = 1
                        break
                    elif (temp_x ** 2 + (temp_y + self.alpha / 2.0) **2) >= 1 and temp_y < - (self.alpha / 2.0):
                        s = 2
                        break
                    elif - (self.alpha / 2.0) < temp_y < (self.alpha / 2.0) and temp_x < -1:
                        s = 3
                        break
                    elif - (self.alpha / 2.0) < temp_y < (self.alpha / 2.0) and temp_x > 1:
                        s = 4
                        break
                    self.x.append(temp_x)
                    self.y.append(temp_y)
                    self.v_x.append(self.v_x[-1])
                    self.v_y.append(self.v_y[-1])
                if s == 1:
                    self.x.append(temp_x / np.sqrt(temp_x ** 2 + (temp_y - self.alpha / 2.0) ** 2))
                    self.y.append((temp_y - self.alpha / 2.0) / np.sqrt(temp_x ** 2 + (temp_y - self.alpha / 2.0) ** 2) + self.alpha / 2.0)
                    temp_v_n = self.x[-1] * self.v_x[-1] + (self.y[-1] - self.alpha / 2.0) * self.v_y[-1]
                    temp_v_x = self.v_x[-1] - 2 * temp_v_n * self.x[-1]
                    temp_v_y = self.v_y[-1] - 2 * temp_v_n * (self.y[-1] - self.alpha / 2.0)
                    self.v_x.append(temp_v_x)
                    self.v_y.append(temp_v_y)
                elif s == 2:
                    self.x.append(temp_x / np.sqrt(temp_x ** 2 + (temp_y + self.alpha / 2.0) ** 2))
                    self.y.append((temp_y + self.alpha / 2.0) / np.sqrt(temp_x ** 2 + (temp_y + self.alpha / 2.0) ** 2) - self.alpha / 2.0)
                    temp_v_n = self.x[-1] * self.v_x[-1] + (self.y[-1] + self.alpha / 2.0) * self.v_y[-1]
                    temp_v_x = self.v_x[-1] - 2 * temp_v_n * self.x[-1]
                    temp_v_y = self.v_y[-1] - 2 * temp_v_n * (self.y[-1] + self.alpha / 2.0)
                    self.v_x.append(temp_v_x)
                    self.v_y.append(temp_v_y)
                elif s == 3:
                    k = float(self.y[-1] - temp_y) / float(self.x[-1] - temp_x)
                    self.x.append(-1)
                    self.y.append(k * (-1.0 - self.x[-1]) + self.y[-1])
                    self.v_x.append(- self.v_x[-1])
                    self.v_y.append(self.v_y[-1])
                elif s == 4:
                    k = float(self.y[-1] - temp_y) / float(self.x[-1] - temp_x)
                    self.x.append(1)
                    self.y.append(k * (1.0 - self.x[-1]) + self.y[-1])
                    self.v_x.append(- self.v_x[-1])
                    self.v_y.append(self.v_y[-1])
            else:
                self.x.append(temp_x)
                self.y.append(temp_y)
                self.v_x.append(self.v_x[-1])
                self.v_y.append(self.v_y[-1])
        for i in range(len(self.y)):
            if np.abs(self.y[i]) < 0.0001:
                self.x_phase_space.append(self.x[i])
                self.v_x_phase_space.append(self.v_x[i])
    def show_results(self):
        plt.subplot(121)
        Theta_1 = np.arange(0,np.pi,0.01)
        Theta_2 = np.arange(np.pi,2 * np.pi,0.01)
        plt.plot(np.cos(Theta_1),np.sin(Theta_1) + self.alpha / 2.0,'b')
        plt.plot(np.cos(Theta_2),np.sin(Theta_2) - self.alpha / 2.0,'b')
        plt.plot(self.x[:10 ** 4],self.y[:10 ** 4],'g')
        plt.title(r'Stadium billiard: $\alpha$' + '= %.3f'%(self.alpha / 2.0))
        plt.xlim(-1.11,1.11)
        plt.ylim(-1.11,1.11)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.subplot(122)
        plt.plot(self.x_phase_space,self.v_x_phase_space,'.')
        plt.title(r'Stadium billiard: $\alpha$' + '= %.3f'%(self.alpha / 2.0))
        plt.xlabel('x')
        plt.ylabel(r'$v_x$')
        plt.show()
class elliptical_table(object):
    def __init__(self,x_0,y_0,v_0,theta_0,a,b):
        self.a = a
        self.b = b
        self.x = [x_0]
        self.y = [y_0]
        self.v_x = [v_0 * np.cos(theta_0)]
        self.v_y = [v_0 * np.sin(theta_0)]
        self.x_phase_space = []
        self.v_x_phase_space = []
        self.dt = 0.01
    def calculate(self):
        for i in range(10 ** 6):
            temp_x = self.x[-1] + self.v_x[-1] * self.dt
            temp_y = self.y[-1] + self.v_y[-1] * self.dt
            if ((temp_x / self.a) ** 2 + (temp_y / self.b) **2) >= 1:
                while (1):
                    temp_x = self.x[-1] + self.v_x[-1] * self.dt * 0.01
                    temp_y = self.y[-1] + self.v_y[-1] * self.dt * 0.01
                    if ((temp_x / self.a) ** 2 + (temp_y / self.b) **2) >= 1:
                        break
                    self.x.append(temp_x)
                    self.y.append(temp_y)
                    self.v_x.append(self.v_x[-1])
                    self.v_y.append(self.v_y[-1])
                self.x.append(temp_x / np.sqrt((temp_x / self.a) ** 2 + (temp_y / self.b) **2))
                self.y.append(temp_y / np.sqrt((temp_x / self.a) ** 2 + (temp_y / self.b) **2))
                temp_v_n = (self.x[-1] * self.b ** 2 * self.v_x[-1] + self.y[-1] * self.a ** 2  * self.v_y[-1]) / np.sqrt(self.x[-1] ** 2 * self.b ** 4 + self.y[-1] ** 2 * self.a ** 4 )
                temp_v_x = self.v_x[-1] - 2 * temp_v_n * self.x[-1] * self.b ** 2 / np.sqrt(self.x[-1] ** 2 * self.b ** 4 + self.y[-1] ** 2 * self.a ** 4 )
                temp_v_y = self.v_y[-1] - 2 * temp_v_n * self.y[-1] * self.a ** 2 / np.sqrt(self.x[-1] ** 2 * self.b ** 4 + self.y[-1] ** 2 * self.a ** 4 )
                self.v_x.append(temp_v_x)
                self.v_y.append(temp_v_y)
            else:
                self.x.append(temp_x)
                self.y.append(temp_y)
                self.v_x.append(self.v_x[-1])
                self.v_y.append(self.v_y[-1])
        for i in range(len(self.y)):
            if np.abs(self.y[i]) < 0.0001:
                self.x_phase_space.append(self.x[i])
                self.v_x_phase_space.append(self.v_x[i])
    def show_results(self):
        plt.subplot(121)
        Theta = np.arange(0,2 * np.pi,0.01)
        p, = plt.plot(np.cos(Theta) * self.a,np.sin(Theta) * self.b)
        plt.legend([p],[r'$\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$   ' + r'$a^2$ = ' + '%.0f   '%(self.a ** 2) + r'$b^2$ = ' + '%.0f'%(self.b ** 2)],loc = 'best')
        plt.plot(self.x[:10 ** 5],self.y[:10 ** 5])
        plt.title('elliptical table - trajectory')
        plt.xlim(-self.a,self.a)
        plt.ylim(-self.a,self.a)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.subplot(122)
        plt.plot(self.x_phase_space,self.v_x_phase_space,'.')
        plt.title('elliptical table - phase space plot')
        plt.xlabel('x')
        plt.ylabel(r'$v_x$')
        plt.xlim(-self.a,self.a)
        plt.ylim(-1,1)
        plt.show()
class circle_in_square(object):
    def __init__(self,x_0,y_0,v_0,theta_0):
        self.x = [x_0]
        self.y = [y_0]
        self.v_x = [v_0 * np.cos(theta_0)]
        self.v_y = [v_0 * np.sin(theta_0)]
        self.x_phase_space = []
        self.v_x_phase_space = []
        self.dt = 0.01
    def calculate(self):
        for i in range(10 ** 6):
            temp_x = self.x[-1] + self.v_x[-1] * self.dt
            temp_y = self.y[-1] + self.v_y[-1] * self.dt
            if (temp_x >= 1 or temp_y >= 1 or temp_x <= -1 or temp_y <= -1 or (temp_x ** 2 + temp_y ** 2) <= 0.25):
                s = 0
                while (1):
                    temp_x = self.x[-1] + self.v_x[-1] * self.dt * 0.01
                    temp_y = self.y[-1] + self.v_y[-1] * self.dt * 0.01
                    if (temp_x >= 1 and - temp_x < temp_y < temp_x):
                        s = 1
                        break
                    elif (temp_y >= 1 and temp_y > - temp_x and temp_y > temp_x):
                        s = 2
                        break
                    elif (temp_x <= -1 and temp_x < temp_y < - temp_x):
                        s = 3
                        break
                    elif (temp_y <= -1 and temp_y < - temp_x and temp_y < temp_x):
                        s = 4
                        break
                    elif (temp_x >= 1 or temp_y >= 1) and (temp_y == temp_x or temp_y == - temp_x):
                        s = 5
                        break
                    elif (temp_x ** 2 + temp_y ** 2) <= 0.25:
                        s = 6
                        break
                    self.x.append(temp_x)
                    self.y.append(temp_y)
                    self.v_x.append(self.v_x[-1])
                    self.v_y.append(self.v_y[-1])
                if s == 1:
                    k = float(self.y[-1] - temp_y) / float(self.x[-1] - temp_x)
                    self.x.append(1)
                    self.y.append(k * (1.0 - self.x[-1]) + self.y[-1])
                    self.v_x.append(- self.v_x[-1])
                    self.v_y.append(self.v_y[-1])
                elif s == 2:
                    k = float(self.y[-1] - temp_y) / float(self.x[-1] - temp_x)
                    self.y.append(1)
                    self.x.append((1.0 - self.y[-1]) / k + self.x[-1])
                    self.v_x.append(self.v_x[-1])
                    self.v_y.append(- self.v_y[-1])
                elif s == 3:
                    k = float(self.y[-1] - temp_y) / float(self.x[-1] - temp_x)
                    self.x.append(-1)
                    self.y.append(k * (-1.0 - self.x[-1]) + self.y[-1])
                    self.v_x.append(- self.v_x[-1])
                    self.v_y.append(self.v_y[-1])
                elif s == 4:
                    k = float(self.y[-1] - temp_y) / float(self.x[-1] - temp_x)
                    self.y.append(-1)
                    self.x.append((-1.0 - self.y[-1]) / k + self.x[-1])
                    self.v_x.append(self.v_x[-1])
                    self.v_y.append(- self.v_y[-1])
                elif s == 5:
                    if (temp_x >= 0 and temp_y >= 0):
                        self.x.append(1)
                        self.y.append(1)
                    elif (temp_x <= 0 and temp_y >= 0):
                        self.x.append(-1)
                        self.y.append(1)
                    elif (temp_x <= 0 and temp_y <= 0):
                        self.x.append(-1)
                        self.y.append(-1)
                    elif (temp_x >= 0 and temp_y <= 0):
                        self.x.append(1)
                        self.y.append(-1)
                    self.v_x.append(- self.v_x[-1])
                    self.v_y.append(- self.v_y[-1])
                elif s == 6:
                    self.x.append(temp_x / np.sqrt((temp_x / 0.5) ** 2 + (temp_y / 0.5) **2))
                    self.y.append(temp_y / np.sqrt((temp_x / 0.5) ** 2 + (temp_y / 0.5) **2))
                    temp_v_n = (self.x[-1] * 0.5 ** 2 * self.v_x[-1] + self.y[-1] * 0.5 ** 2  * self.v_y[-1]) / np.sqrt(self.x[-1] ** 2 * 0.5 ** 4 + self.y[-1] ** 2 * 0.5 ** 4 )
                    temp_v_x = self.v_x[-1] - 2 * temp_v_n * self.x[-1] * 0.5 ** 2 / np.sqrt(self.x[-1] ** 2 * 0.5 ** 4 + self.y[-1] ** 2 * 0.5 ** 4 )
                    temp_v_y = self.v_y[-1] - 2 * temp_v_n * self.y[-1] * 0.5 ** 2 / np.sqrt(self.x[-1] ** 2 * 0.5 ** 4 + self.y[-1] ** 2 * 0.5 ** 4 )
                    self.v_x.append(temp_v_x)
                    self.v_y.append(temp_v_y)
            else:
                self.x.append(temp_x)
                self.y.append(temp_y)
                self.v_x.append(self.v_x[-1])
                self.v_y.append(self.v_y[-1])
        for i in range(len(self.y)):
            if np.abs(self.y[i]) < 0.0001:
                self.x_phase_space.append(self.x[i])
                self.v_x_phase_space.append(self.v_x[i])
    def show_results(self):
        plt.subplot(121)
        Theta = np.arange(0,2 * np.pi,0.01)
        p, = plt.plot(np.cos(Theta) * 0.5,np.sin(Theta) * 0.5,'r')
        plt.legend([p],[r'$x^2$ + $y^2$ = 0.25'],loc='best')
        l = np.arange(-1,1.01,0.01)
        L_1 = []
        for i in range(len(l)):
            L_1.append(1)
        L_2 = []
        for i in range(len(l)):
            L_2.append(-1)
        plt.plot(L_1,l,'b')
        plt.plot(l,L_1,'b')
        plt.plot(L_2,l,'b')
        plt.plot(l,L_2,'b')
        plt.plot(self.x[:10 ** 4],self.y[:10 ** 4],'g')
        plt.title('A square table with a circular interior wall located in the center' + '\n' + 'trajectory')
        plt.xlim(-1.1,1.1)
        plt.ylim(-1.1,1.1)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.subplot(122)
        plt.plot(self.x_phase_space,self.v_x_phase_space,'.')
        plt.title('A square table with a circular interior wall located in the center' + '\n' + 'phase space plot')
        plt.xlabel('x')
        plt.ylabel(r'$v_x$')
        plt.show()