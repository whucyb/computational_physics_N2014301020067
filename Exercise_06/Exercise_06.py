# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.stats as ss
class cannon_shell(object):
    def __init__(self,target):
        self.x = [[]]
        self.y = [[]]
        self.v_0 = [2]
        self.v_x = [[]]
        self.v_y = [[]]
        self.delta_t = 0.05
        self.angle = np.arange(0,90.1,0.1)
        self.shoot_angle = []
        self.target = target
        self.distance_from_the_target=[]
        self.deviation=[]
        self.deviation_2=[]
        self.RMS=[]
        self.g_0 = 0.0098
        self.R = 6371
        self.B_2_divided_by_m = 0.04
        self.a = 6.5
        self.alpha = 2.5
        self.T_0 = 300
        self.v_wind = [10.0 / 3600]
    def calculate(self):
        for i in self.angle:
            self.x[0].append([0])
            self.y[0].append([0])
            self.v_x[0].append([self.v_0[-1] * np.cos((float(i) / 180) * np.pi)])
            self.v_y[0].append([self.v_0[-1] * np.sin((float(i) / 180) * np.pi)])
            while (self.y[0][-1][-1] > 0) or (self.x[0][-1][-1] == 0):
                delta_v = np.sqrt((self.v_x[0][-1][-1] - self.v_wind[-1]) ** 2 + (self.v_y[0][-1][-1]) ** 2)
                self.x[0][-1].append(self.x[0][-1][-1] + self.v_x[0][-1][-1] * self.delta_t)
                self.y[0][-1].append(self.y[0][-1][-1] + self.v_y[0][-1][-1] * self.delta_t)
                self.v_x[0][-1].append(self.v_x[0][-1][-1] - ((1 - self.a * self.y[0][-1][-1] / self.T_0) ** self.alpha) * self.B_2_divided_by_m * delta_v * (self.v_x[0][-1][-1] - self.v_wind[-1]) * self.delta_t)
                self.v_y[0][-1].append(self.v_y[0][-1][-1] - (self.g_0 * ((float(self.R) / (self.R + self.y[0][-1][-1])) ** 2) + ((1 - self.a * self.y[0][-1][-1] / self.T_0) ** self.alpha) * self.B_2_divided_by_m * delta_v * self.v_y[0][-1][-1]) * self.delta_t)
            if self.y[0][-1][-1] < 0:
                r = - (self.y[0][-1][-2] / self.y[0][-1][-1])
                self.x[0][-1][-1] = (self.x[0][-1][-2] + r * self.x[0][-1][-1]) / (r + 1)
            self.distance_from_the_target.append(abs(self.x[0][-1][-1] - self.target))
        for i in self.angle:
            if self.distance_from_the_target[int(i * 10)] == min(self.distance_from_the_target):
                print i
                print self.x[0][int(i * 10)][-1]
                self.shoot_angle.append(i)
    def shoot(self):
        self.x.append([])
        self.y.append([])
        self.v_x.append([])
        self.v_y.append([])
        for i in range(1000):
            self.v_0.append(self.v_0[0] * (1 + random.uniform(-0.05,0.05)))
            self.shoot_angle.append(self.shoot_angle[0] + random.uniform(-2,2))
            self.v_wind.append(self.v_wind[0] * (1 + random.uniform(-0.1,0.1)))
            self.x[1].append([0])
            self.y[1].append([0])
            self.v_x[1].append([self.v_0[-1] * np.cos((self.shoot_angle[-1] / 180) * np.pi)])
            self.v_y[1].append([self.v_0[-1] * np.sin((self.shoot_angle[-1] / 180) * np.pi)])
            while (self.y[1][-1][-1] > 0) or (self.x[1][-1][-1] == 0):
                delta_v = np.sqrt((self.v_x[1][-1][-1] - self.v_wind[-1]) ** 2 + (self.v_y[1][-1][-1]) ** 2)
                self.x[1][-1].append(self.x[1][-1][-1] + self.v_x[1][-1][-1] * self.delta_t)
                self.y[1][-1].append(self.y[1][-1][-1] + self.v_y[1][-1][-1] * self.delta_t)
                self.v_x[1][-1].append(self.v_x[1][-1][-1] - ((1 - self.a * self.y[1][-1][-1] / self.T_0) ** self.alpha) * self.B_2_divided_by_m * delta_v * (self.v_x[1][-1][-1] - self.v_wind[-1]) * self.delta_t)
                self.v_y[1][-1].append(self.v_y[1][-1][-1] - (self.g_0 * ((float(self.R) / (self.R + self.y[1][-1][-1])) ** 2) + ((1 - self.a * self.y[1][-1][-1] / self.T_0) ** self.alpha) * self.B_2_divided_by_m * delta_v * self.v_y[1][-1][-1]) * self.delta_t)
            if self.y[1][-1][-1] < 0:
                r = - (self.y[1][-1][-2] / self.y[1][-1][-1])
                self.x[1][-1][-1] = (self.x[1][-1][-2] + r * self.x[1][-1][-1]) / (r + 1)
            self.deviation.append(self.x[1][-1][-1] - self.target)           
            self.deviation_2.append(self.deviation[-1] ** 2)
        self.RMS.append(sum(self.deviation_2) / 1000.0)
    def show_results_1(self):
        for i in self.angle:
            plt.plot(self.x[0][int(i * 10)], self.y[0][int(i * 10)])
        plt.title('Trajectory of cannon shell')
        plt.xlabel('x (km)')
        plt.ylabel('y (km)')
        plt.ylim(0,)
        plt.show()
    def show_results_2(self):        
        for i in range(1000):
            plt.plot(self.x[1][i], self.y[1][i])
        plt.title(r'Trajectory of cannon shell   $\theta$ = %.1f'%self.shoot_angle[0])
        plt.xlabel('x (km)')
        plt.ylabel('y (km)')
        plt.ylim(0,)
        plt.show()
    def show_results_3(self):   
        plt.plot(sorted(self.deviation), ss.norm.pdf(sorted(self.deviation)))
        plt.title(r'$\overline{(\Delta x)^2}$ = %.2f $km^2$'%self.RMS[-1])
        plt.xlabel(r'$\Delta x(km)$')
        plt.ylabel('P')
        plt.ylim(0,)
        plt.show()
a=cannon_shell(100)
a.calculate()
a.shoot()
