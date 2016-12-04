# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
class hyperion_circular_orbit(object):
    def __init__(self,x_0 = 1,vy_0 = 2 * np.pi,tlim = 7.25):
        self.x = [x_0]
        self.y = [0]
        self.vx = [0]
        self.vy = [vy_0]
        self.theta = [0]
        self.omega = [0]
        self.dt = 0.0001
        self.t = [0]
        self.GM = 4 * (np.pi ** 2)
        self.e = 1 - x_0 * (vy_0 ** 2) / self.GM
        self.a = x_0 / (1 + self.e)
        self.tlim = tlim
    def calculate(self):
        while (self.t[-1] < self.tlim):
            temp_r = np.sqrt(self.x[-1] ** 2 + self.y[-1] ** 2)
            self.vx.append(self.vx[-1] - self.GM * self.x[-1] / (temp_r ** 3) * self.dt)
            self.vy.append(self.vy[-1] - self.GM * self.y[-1] / (temp_r ** 3) * self.dt)
            self.omega.append(self.omega[-1] - 3 * self.GM / (temp_r ** 5) * (self.x[-1] * np.sin(self.theta[-1]) - self.y[-1] * np.cos(self.theta[-1])) * (self.x[-1] * np.cos(self.theta[-1]) + self.y[-1] * np.sin(self.theta[-1])) * self.dt)
            self.x.append(self.x[-1] + self.vx[-1] * self.dt)
            self.y.append(self.y[-1] + self.vy[-1] * self.dt)
            self.theta.append(self.theta[-1] + self.omega[-1] * self.dt)
            self.t.append(self.t[-1] + self.dt)
            while self.theta[-1] >=  np.pi:
                self.theta[-1] -= 2 * np.pi
            while self.theta[-1] <= - np.pi:
                self.theta[-1] += 2 * np.pi
    def show_result_1(self):
        plt.subplot(121)
        plt.plot(self.t,self.theta)
        plt.title(r'Hyperion  $\theta$ versus time' + '\n' + 'Circular orbit')
        plt.xlim(0,8)
        plt.ylim(-4,4)
        plt.xlabel('time (yr)')
        plt.ylabel(r'$\theta$ (radians)')
        plt.subplot(122)
        plt.plot(self.t,self.omega)
        plt.title(r'Hyperion  $\omega$ versus time' + '\n' + 'Circular orbit')
        plt.xlim(0,8)
        plt.ylim(0,15)
        plt.xlabel('time (yr)')
        plt.ylabel(r'$\omega$ (radians/yr)')
        plt.show()
    def show_result_2(self):
        plt.scatter(self.theta,self.omega,s = 0.01)
        plt.title(r'Hyperion  phase space plot' + '\n' + 'Circular orbit')
        plt.xlabel(r'$\theta$ (radians)')
        plt.ylabel(r'$\omega$ (radians/yr)')
class hyperion_elliptical_orbit(object):
    def __init__(self,x_0 = 1,vy_0 = 5,tlim = 10):
        self.x = [x_0]
        self.y = [0]
        self.vx = [0]
        self.vy = [vy_0]
        self.theta = [0]
        self.omega = [0]
        self.dt = 0.0001
        self.t = [0]
        self.GM = 4 * (np.pi ** 2)
        self.e = 1 - x_0 * (vy_0 ** 2) / self.GM
        self.a = x_0 / (1 + self.e)
        self.tlim = tlim
    def calculate(self):
        while (self.t[-1] < self.tlim):
            temp_r = np.sqrt(self.x[-1] ** 2 + self.y[-1] ** 2)
            self.vx.append(self.vx[-1] - self.GM * self.x[-1] / (temp_r ** 3) * self.dt)
            self.vy.append(self.vy[-1] - self.GM * self.y[-1] / (temp_r ** 3) * self.dt)
            self.omega.append(self.omega[-1] - 3 * self.GM / (temp_r ** 5) * (self.x[-1] * np.sin(self.theta[-1]) - self.y[-1] * np.cos(self.theta[-1])) * (self.x[-1] * np.cos(self.theta[-1]) + self.y[-1] * np.sin(self.theta[-1])) * self.dt)
            self.x.append(self.x[-1] + self.vx[-1] * self.dt)
            self.y.append(self.y[-1] + self.vy[-1] * self.dt)
            self.theta.append(self.theta[-1] + self.omega[-1] * self.dt)
            self.t.append(self.t[-1] + self.dt)
            while self.theta[-1] >=  np.pi:
                self.theta[-1] -= 2 * np.pi
            while self.theta[-1] <= - np.pi:
                self.theta[-1] += 2 * np.pi
    def show_result_1(self):
        plt.subplot(121)
        plt.plot(self.t,self.theta)
        plt.title(r'Hyperion  $\theta$ versus time' + '\n' + 'Elliptical orbit')
        plt.xlim(0,10)
        plt.ylim(-4,4)
        plt.xlabel('time (yr)')
        plt.ylabel(r'$\theta$ (radians)')
        plt.subplot(122)
        plt.plot(self.t,self.omega)
        plt.title(r'Hyperion  $\omega$ versus time' + '\n' + 'Elliptical orbit')
        plt.xlim(0,10)
        plt.ylim(-20,60)
        plt.xlabel('time (yr)')
        plt.ylabel(r'$\omega$ (radians/yr)')
        plt.show()
    def show_result_2(self):
        plt.scatter(self.theta,self.omega,s = 0.01)
        plt.title(r'Hyperion  phase space plot' + '\n' + 'Elliptical orbit')
        plt.xlabel(r'$\theta$ (radians)')
        plt.ylabel(r'$\omega$ (radians/yr)')
class LE_1(object):
    def __init__(self,x_0,vy_0,theta_0,omega_0,tlim):
        self.x = [[x_0],[x_0]]
        self.y = [[0],[0]]
        self.vx = [[0],[0]]
        self.vy = [[vy_0],[vy_0]]
        self.theta = [[theta_0],[theta_0 + 0.01]]
        self.Delta_theta = []
        self.omega = [[omega_0],[omega_0]]
        self.dt = 0.0001
        self.t = [[0],[0]]
        self.GM = 4 * (np.pi ** 2)
        self.e = 1 - x_0 * (vy_0 ** 2) / self.GM
        self.a = x_0 / (1 + self.e)
        self.tlim = tlim
    def calculate(self):
        for i in range(2):
            while (self.t[i][-1] < self.tlim):
                temp_r = np.sqrt(self.x[i][-1] ** 2 + self.y[i][-1] ** 2)
                self.vx[i].append(self.vx[i][-1] - self.GM * self.x[i][-1] / (temp_r ** 3) * self.dt)
                self.vy[i].append(self.vy[i][-1] - self.GM * self.y[i][-1] / (temp_r ** 3) * self.dt)
                self.omega[i].append(self.omega[i][-1] - 3 * self.GM / (temp_r ** 5) * (self.x[i][-1] * np.sin(self.theta[i][-1]) - self.y[i][-1] * np.cos(self.theta[i][-1])) * (self.x[i][-1] * np.cos(self.theta[i][-1]) + self.y[i][-1] * np.sin(self.theta[i][-1])) * self.dt)
                self.x[i].append(self.x[i][-1] + self.vx[i][-1] * self.dt)
                self.y[i].append(self.y[i][-1] + self.vy[i][-1] * self.dt)
                self.theta[i].append(self.theta[i][-1] + self.omega[i][-1] * self.dt)
                self.t[i].append(self.t[i][-1] + self.dt)
                while self.theta[i][-1] >=  np.pi:
                    self.theta[i][-1] -= 2 * np.pi
                while self.theta[i][-1] <= - np.pi:
                    self.theta[i][-1] += 2 * np.pi
        for j in range(len(self.t[0])):
            self.Delta_theta.append(np.abs(self.theta[0][j] - self.theta[1][j]))
    def show_result(self):
        plt.semilogy(self.t[0],self.Delta_theta)
        plt.title(r'Hyprion  $\Delta \theta$ versus time' + '\n' + 'e = %.3f  '%self.e)
        plt.xlim(0,10)
        plt.xlabel('time (yr)')
        plt.ylabel(r'$\Delta \theta$ (radians)')
