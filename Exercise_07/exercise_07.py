# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
class simple_pendulum_euler_method(object):
    def __init__(self):
        self.omega = [[0]]
        self.theta = [[0.2]]
        self.dt = 0.04
        self.time = [[0]]
    def calculate(self):
        l=1
        g=9.8
        while (self.time[-1][-1] < 10):
            temp_omega = self.omega[-1][-1] - (g / l) * self.theta[-1][-1] * self.dt
            temp_theta = self.theta[-1][-1] + self.omega[-1][-1] * self.dt
            self.omega[-1].append(temp_omega)
            self.theta[-1].append(temp_theta)
            self.time[-1].append(self.time[-1][-1] + self.dt)
    def show_results(self):
        plt.plot(self.time[-1],self.theta[-1])
        plt.title('Simple Pendulum - Euler method')
        plt.text(2.5,1.5,'Length = 1 m   time step = 0.04 s') 
        plt.xlabel('time (s)')
        plt.ylabel(r'$\theta$ (radians)')
        plt.xlim(0,10)
        plt.ylim(-2,2)
        plt.show()
class simple_pendulum_euler_cromer_method(simple_pendulum_euler_method):
    def calculate(self):
        l=1
        g=9.8
        while (self.time[-1][-1] < 10):
            temp_omega = self.omega[-1][-1] - (g / l) * self.theta[-1][-1] * self.dt
            temp_theta = self.theta[-1][-1] + temp_omega * self.dt
            self.omega[-1].append(temp_omega)
            self.theta[-1].append(temp_theta)
            self.time[-1].append(self.time[-1][-1] + self.dt)
    def show_results(self):
        plt.plot(self.time[-1],self.theta[-1])
        plt.title('Simple Pendulum - Euler-Cromer method')
        plt.text(2.5,0.25,'Length = 1 m   time step = 0.04 s')
        plt.xlabel('time (s)')
        plt.ylabel(r'$\theta$ (radians)')
        plt.xlim(0,10)
        plt.ylim(-0.3,0.3)
        plt.show()
class damped_pendulum(simple_pendulum_euler_method):
    def calculate(self):
        l = 1
        g = 9.8
        q = [1.0,5,10]
        self.omega.extend([[0],[0]])
        self.theta.extend([[0.2],[0.2]])
        self.time.extend([[0],[0]])
        for i in range(3):
            while (self.time[i][-1] < 10):
                temp_omega = self.omega[i][-1] - ((g / l) * self.theta[i][-1] + q[i] * self.omega[i][-1])* self.dt
                temp_theta = self.theta[i][-1] + temp_omega * self.dt
                self.omega[i].append(temp_omega)
                self.theta[i].append(temp_theta)
                self.time[i].append(self.time[i][-1] + self.dt)
    def show_results(self):
        p1,=plt.plot(self.time[0],self.theta[0],'-')
        p2,=plt.plot(self.time[1],self.theta[1],'-')
        p2.set_dashes([1,2])
        p3,=plt.plot(self.time[2],self.theta[2],'-')
        p3.set_dashes([5,2,1,2])
        plt.title('Damped Pendulum')
        plt.annotate('q = 1.0', xy=(1.5,-0.05),xytext=(2,-0.1),arrowprops=dict(arrowstyle="->"))
        plt.annotate('q = 5', xy=(0.75,0.05),xytext=(2,0.1),arrowprops=dict(arrowstyle="->"))
        plt.annotate('q = 10', xy=(0.75,0.1),xytext=(1.5,0.15),arrowprops=dict(arrowstyle="->"))
        plt.xlabel('time (s)')
        plt.ylabel(r'$\theta$ (radians)')
        plt.xlim(0,10)
        plt.ylim(-0.2,0.2)
        plt.show()
class driven_pendulum(simple_pendulum_euler_method):
    def calculate(self):
        l = 1
        g = 9.8
        q = 1.0
        Omega_D = 2.0
        F_D = 0.2
        while (self.time[-1][-1] < 20):
            temp_omega = self.omega[-1][-1] - ((g / l) * self.theta[-1][-1] + q * self.omega[-1][-1] - F_D * np.sin(Omega_D * self.time[-1][-1]))* self.dt
            temp_theta = self.theta[-1][-1] + temp_omega * self.dt
            self.omega[-1].append(temp_omega)
            self.theta[-1].append(temp_theta)
            self.time[-1].append(self.time[-1][-1] + self.dt)
    def show_results(self):
        plt.plot(self.time[-1],self.theta[-1])
        plt.title('Driven Pendulum')
        plt.text(7,0.1,r'$\Omega_D$ = 2.0   $F_D$ = 0.2' + '\nq = 1.0')
        plt.xlabel('time (s)')
        plt.ylabel(r'$\theta$ (radians)')
        plt.xlim(0,20)
        plt.ylim(-0.2,0.2)
        plt.show()
class driven_nonlinear_pendulum(simple_pendulum_euler_method):
    def calculate(self):
        l = 9.8
        g = 9.8
        q = 0.5
        Omega_D = 2.0/3
        F_D = [0,0.5,1.2]
        self.omega.extend([[0],[0]])
        self.theta.extend([[0.2],[0.2]])
        self.time.extend([[0],[0]])
        for i in range(3):
            while (self.time[i][-1] < 60):
                temp_omega = self.omega[i][-1] - ((g / l) * np.sin(self.theta[i][-1]) + q * self.omega[i][-1] - F_D[i] * np.sin(Omega_D * self.time[i][-1]))* self.dt
                temp_theta = self.theta[i][-1] + temp_omega * self.dt
                self.omega[i].append(temp_omega)
                self.theta[i].append(temp_theta)
                self.time[i].append(self.time[i][-1] + self.dt)
        self.theta.append([])
        for i in self.theta[2]:
            while i < -np.pi:
                i = i + 2 * np.pi
            self.theta[3].append(i)
    def show_results_1(self):
        plt.subplot(131)
        plt.plot(self.time[0],self.theta[0])
        plt.title(r'$\theta$ versus time' + '\n' + r'$F_D$ = 0')
        plt.xlabel('time (s)')
        plt.ylabel(r'$\theta$ (radians)')
        plt.xlim(0,60)
        plt.ylim(-1.4,0.3)
        plt.subplot(132)
        plt.plot(self.time[1],self.theta[1])
        plt.title(r'$\theta$ versus time' + '\n' + r'$F_D$ = 0.5')
        plt.xlabel('time (s)')
        plt.ylabel(r'$\theta$ (radians)')
        plt.xlim(0,60)
        plt.ylim(-10,7)
        plt.subplot(133)
        plt.plot(self.time[2],self.theta[3])
        plt.title(r'$\theta$ versus time' + '\n' + r'$F_D$ = 1.2')
        plt.xlabel('time (s)')
        plt.ylabel(r'$\theta$ (radians)')
        plt.xlim(0,60)
        plt.ylim(-4,13)
        plt.show()
    def show_results_2(self):    
        plt.subplot(131)
        plt.plot(self.time[2],self.theta[3])
        plt.title(r'$\theta$ versus time' + '\n' + r'$F_D$ = 1.2')
        plt.xlabel('time (s)')
        plt.ylabel(r'$\theta$ (radians)')
        plt.xlim(0,60)
        plt.ylim(-10,4)
        plt.subplot(132)
        plt.plot(self.time[2],self.theta[2])
        plt.title(r'$\theta$ versus time' + '\n' + r'$F_D$ = 1.2')
        plt.xlabel('time (s)')
        plt.ylabel(r'$\theta$ (radians)')
        plt.xlim(0,60)
        plt.ylim(-10,4)
        plt.subplot(133)
        plt.plot(self.time[2],self.theta[3])
        plt.plot(self.time[2],self.theta[2])
        plt.title(r'$\theta$ versus time' + '\n' + r'$F_D$ = 1.2')
        plt.xlabel('time (s)')
        plt.ylabel(r'$\theta$ (radians)')
        plt.xlim(0,60)
        plt.ylim(-10,4)
        plt.show()
    def show_results_3(self):
        plt.subplot(131)
        plt.plot(self.time[0],self.omega[0])
        plt.title(r'$\omega$ versus time' + '\n' + r'$F_D$ = 0')
        plt.xlabel('time (s)')
        plt.ylabel(r'$\omega$ (radians/s)')
        plt.xlim(0,60)
        plt.ylim(-8,1)
        plt.subplot(132)
        plt.plot(self.time[1],self.omega[1])
        plt.title(r'$\omega$ versus time' + '\n' + r'$F_D$ = 0.5')
        plt.xlabel('time (s)')
        plt.ylabel(r'$\omega$ (radians/s)')
        plt.xlim(0,60)
        plt.ylim(-6,2)
        plt.subplot(133)
        plt.plot(self.time[2],self.omega[2])
        plt.title(r'$\omega$ versus time' + '\n' + r'$F_D$ = 1.2')
        plt.xlabel('time (s)')
        plt.ylabel(r'$\omega$ (radians/s)')
        plt.xlim(0,60)
        plt.ylim(-3,5)
        plt.show()
class two_identical_pendulums(object):
    def __init__(self,theta_1,q,t_1,t_2):
        self.omega_1 = [[0],[0]]
        self.omega_2 = [[0],[0]]
        self.theta_1 = [[theta_1],[theta_1]]
        self.theta_2 = [[theta_1 + 0.001],[theta_1 + 0.001]]
        self.delta_theta = [[0.001],[0.001]]
        self.dt = 0.04
        self.time = [[0],[0]]
        self.LE = []
        self.lyapunov = [[],[]]
        self.q = q
        self.t_lim = [t_1,t_2]
    def calculate(self):
        l = 9.8
        g = 9.8
        Omega_D = 2.0/3
        F_D = [0.5,1.2]
        for i in range(2):
            sum = 0.0
            while self.time[i][-1] < float(self.t_lim[i] - 0.001):
                temp_omega_1 = self.omega_1[i][-1] - ((g / l) * np.sin(self.theta_1[i][-1]) + self.q * self.omega_1[i][-1] - F_D[i] * np.sin(Omega_D * self.time[i][-1])) * self.dt
                temp_theta_1 = self.theta_1[i][-1] + temp_omega_1 * self.dt
                self.omega_1[i].append(temp_omega_1)
                self.theta_1[i].append(temp_theta_1)
                temp_omega_2 = self.omega_2[i][-1] - ((g / l) * np.sin(self.theta_2[i][-1]) + self.q * self.omega_2[i][-1] - F_D[i] * np.sin(Omega_D * self.time[i][-1])) * self.dt
                temp_theta_2 = self.theta_2[i][-1] + temp_omega_2 * self.dt
                self.omega_2[i].append(temp_omega_2)
                self.theta_2[i].append(temp_theta_2)
                self.delta_theta[i].append(np.abs(self.theta_1[i][-1]-self.theta_2[i][-1]))
                self.time[i].append(self.time[i][-1] + self.dt)
                sum += np.log(self.delta_theta[i][-1] / self.delta_theta[i][-2])
            self.LE.append(sum / float(self.t_lim[i]))
            print self.time[i][-1]
        for j in range(2):
            for i in self.time[j]:
                self.lyapunov[j].append(np.exp(self.LE[j] * i) * 0.001)
    def show_results(self):
        plt.subplot(121)
        plt.semilogy(self.time[0],self.delta_theta[0])
        p1,=plt.semilogy(self.time[0],self.lyapunov[0])
        plt.title(r'$\Delta\theta$ versus time   $F_D$ = 0.5   q = %.2f'%self.q + '\n' + r'$\theta_{10}$ = %.3f   $\theta_{20}$ = %.3f'%(self.theta_1[0][0],self.theta_2[0][0]))
        plt.legend([p1],[r'$\lambda\ \approx$ %.3f'%self.LE[0]],loc='best')
        plt.xlabel('time (s)')
        plt.ylabel(r'$\Delta\theta$ (radians)')
        plt.xlim(0,50)
        plt.subplot(122)
        plt.semilogy(self.time[1],self.delta_theta[1])
        p2,=plt.semilogy(self.time[1],self.lyapunov[1])
        plt.title(r'$\Delta\theta$ versus time   $F_D$ = 1.2   q = %.2f'%self.q + '\n' + r'$\theta_{10}$ = %.3f   $\theta_{20}$ = %.3f'%(self.theta_1[0][0],self.theta_2[0][0]))
        plt.legend([p2],[r'$\lambda\ \approx$ %.3f'%self.LE[1]],loc='best')
        plt.xlabel('time (s)')
        plt.ylabel(r'$\Delta\theta$ (radians)')
        plt.xlim(0,150)
        plt.show()
class phase_space(simple_pendulum_euler_method):
    def calculate(self):
        l = 9.8
        g = 9.8
        q = 0.5
        Omega_D = 2.0/3
        F_D = [0.5,1.2]
        self.omega.append([0])
        self.theta.append([0.2])
        self.time.append([0])
        for i in range(2):
            while (self.time[i][-1] < 300):
                temp_omega = self.omega[i][-1] - ((g / l) * np.sin(self.theta[i][-1]) + q * self.omega[i][-1] - F_D[i] * np.sin(Omega_D * self.time[i][-1]))* self.dt
                temp_theta = self.theta[i][-1] + temp_omega * self.dt
                while temp_theta > np.pi:
                    temp_theta -= 2 * np.pi
                while temp_theta < -np.pi:
                    temp_theta += 2 * np.pi
                self.omega[i].append(temp_omega)
                self.theta[i].append(temp_theta)
                self.time[i].append(self.time[i][-1] + self.dt)
    def show_results(self):
        plt.subplot(121)
        plt.plot(self.theta[0],self.omega[0],'.')
        plt.title(r'$\omega$ versus $\theta$   $F_D$ = 0.5')
        plt.xlabel(r'$\theta$ (radians)')
        plt.ylabel(r'$\omega$ (radians/s)')
        plt.xlim(-1,1)
        plt.ylim(-1,1)
        plt.subplot(122)
        plt.plot(self.theta[1],self.omega[1],'.')
        plt.title(r'$\omega$ versus $\theta$   $F_D$ = 1.2')
        plt.xlabel(r'$\theta$ (radians)')
        plt.ylabel(r'$\omega$ (radians/s)')
        plt.xlim(-4,4)
        plt.ylim(-3,3)
        plt.show()
class poincare_section(simple_pendulum_euler_method):
    def __init__(self,c):
        self.omega = [[0]]
        self.theta = [[0.2]]
        self.dt = 0.04
        self.time = [[0]]
        self.omega_in_poincare_section = []
        self.theta_in_poincare_section = []
        self.c = c
    def calculate(self):
        l = 9.8
        g = 9.8
        q = 0.5
        Omega_D = 2.0/3
        F_D = [0.5,1.2]
        self.omega.append([0])
        self.theta.append([0.2])
        self.time.append([0])
        t_max = self.dt * ((0.5 + (2 * 500 * np.pi + self.c) / (Omega_D * self.dt)) // 1)
        for i in range(2):
            while (self.time[i][-1] <= t_max):
                temp_omega = self.omega[i][-1] - ((g / l) * np.sin(self.theta[i][-1]) + q * self.omega[i][-1] - F_D[i] * np.sin(Omega_D * self.time[i][-1]))* self.dt
                temp_theta = self.theta[i][-1] + temp_omega * self.dt
                while temp_theta > np.pi:
                    temp_theta -= 2 * np.pi
                while temp_theta < -np.pi:
                    temp_theta += 2 * np.pi
                self.omega[i].append(temp_omega)
                self.theta[i].append(temp_theta)
                self.time[i].append(self.time[i][-1] + self.dt)
        for i in range(2):
            self.omega_in_poincare_section.append([])
            self.theta_in_poincare_section.append([])
            for n in range(1,501):
                k = int((0.5 + (2 * n * np.pi + self.c) / (Omega_D * self.dt)) // 1)
                self.omega_in_poincare_section[i].append(self.omega[i][k])
                self.theta_in_poincare_section[i].append(self.theta[i][k])
    def show_results(self):
        plt.subplot(121)
        p1,=plt.plot(self.theta_in_poincare_section[0],self.omega_in_poincare_section[0],'.')
        plt.title(u'Poincaré section\n' + r'$\omega$ versus $\theta$   $F_D$ = 0.5')
        plt.legend([p1],[r'$\Omega_Dt=2n\pi$'],loc='best')
        plt.xlabel(r'$\theta$ (radians)')
        plt.ylabel(r'$\omega$ (radians/s)')
        plt.xlim(-1,1)
        plt.ylim(-1,1)
        plt.subplot(122)
        p2,=plt.plot(self.theta_in_poincare_section[1],self.omega_in_poincare_section[1],'.')
        plt.title(u'Poincaré section\n' + r'$\omega$ versus $\theta$   $F_D$ = 1.2')
        plt.legend([p2],[r'$\Omega_Dt=2n\pi$'],loc='best')
        plt.xlabel(r'$\theta$ (radians)')
        plt.ylabel(r'$\omega$ (radians/s)')
        plt.xlim(-4,4)
        plt.ylim(-3,3)
        plt.show()