# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
class resonance(object):
    def __init__(self, initial_number_of_nuclei_A, initial_number_of_nuclei_B,
                 time_constant, time_of_duration, time_step):
        self.N_A = [initial_number_of_nuclei_A]
        self.N_B = [initial_number_of_nuclei_B]
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.T = time_of_duration
        self.nsteps = int(time_of_duration / time_step)
    def __repr__(self):
        return 'Initial number of nuclei A : %d\n'%self.N_A[0]\
              +'Initial number of nuclei B : %d\n'%self.N_B[0]\
              +'Time constant : %.2f s\n'%self.tau\
              +'Time step : %.2f s\n'%self.dt\
              +'Total time : %.2f s'%self.T
    def calculate(self):
        self.dN_A_dt = [self.N_B[0] / self.tau - self.N_A[0] / self.tau]
        self.dN_B_dt = [self.N_A[0] / self.tau - self.N_B[0] / self.tau]
        for i in range(self.nsteps):
            temp_A = self.N_A[i] + (self.dN_A_dt[i]) * self.dt
            temp_B = self.N_B[i] + (self.dN_B_dt[i]) * self.dt
            self.N_A.append(temp_A)
            self.N_B.append(temp_B)
            self.dN_A_dt.append(self.N_B[i+1] / self.tau - self.N_A[i+1] / self.tau)
            self.dN_B_dt.append(self.N_A[i+1] / self.tau - self.N_B[i+1] / self.tau)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        plt.subplot(211)
        p1,=plt.plot(self.t, self.N_A)
        p2,=plt.plot(self.t, self.N_B)
        plt.title(r'$N_{A0}$ = %d  $N_{B0}$ = %d  $\tau$ = %.2f s  $\Delta  t$ = %.2f s '\
                  %(self.N_A[0],self.N_B[0],self.tau,self.dt))
        plt.xlabel('Time (s)')
        plt.ylabel('Number of Nuclei')
        plt.xlim(0, self.T)
        plt.legend((p1,p2),
                   (r'$N_{A}(t)$',r'$N_{B}(t)$',),
                   loc='best')
        plt.subplot(212)
        p3,=plt.plot(self.t, self.dN_A_dt, '-')
        p3.set_dashes([10,5])
        p4,=plt.plot(self.t, self.dN_B_dt, '-')
        p4.set_dashes([10,5])
        plt.xlabel('Time (s)')
        plt.ylabel(r'$\frac{\mathrm{d} }{\mathrm{d} t}[N_{A}(t)]}$ or '\
                  +r'$\frac{\mathrm{d} }{\mathrm{d} t}[N_{B}(t)]$ ($s^{-1}$)')
        plt.xlim(0, self.T)
        plt.legend((p3,p4),
                   (r'$\mathrm{d} N_{A}(t)/\mathrm{d} t$',
                    r'$\mathrm{d} N_{B}(t)/\mathrm{d} t$'),
                   loc='best')
        plt.show()
    def store_results(self):
        f = open('data.txt', 'w')
        f.write('Initial number of nuclei A : %d\n'%self.N_A[0]\
               +'Initial number of nuclei B : %d\n'%self.N_B[0]\
               +'Time constant : %.2f s\n'%self.tau\
               +'Time step : %.2f s\n'%self.dt\
               +'Total time : %.2f s\n'%self.T\
               +'Time\t\tNumber of nuclei A\t\tNumber of nuclei B\n')
        for i in range(len(self.t)):
            f.write('%.2f\t\t%13.6f\t\t\t%13.6f\n'\
                    %(self.t[i],self.N_A[i],self.N_B[i]))
        f.close()
class exact_results_check(resonance):
    def show_results(self):
        self.et_A = []
        self.et_B = []
        self.et_t = np.arange(0,self.T+0.001,0.001)
        C_1=float(self.N_A[0] + self.N_B[0]) / 2
        C_2=float(self.N_A[0] - self.N_B[0]) / 2
        for i in range(len(self.et_t)):
            temp_et_A = C_1 + C_2 * np.exp(float((-2) * self.et_t[i]) / self.tau)
            temp_et_B = C_1 - C_2 * np.exp(float((-2) * self.et_t[i]) / self.tau)
            self.et_A.append(temp_et_A)
            self.et_B.append(temp_et_B)
        p11,=plt.plot(self.et_t, self.et_A)
        p12,=plt.plot(self.t, self.N_A, 'x')
        p21,=plt.plot(self.et_t, self.et_B)
        p22,=plt.plot(self.t, self.N_B, '+')
        plt.title(r'$N_{A0}$ = %d  $N_{B0}$ = %d  $\tau$ = %.2f s  $\Delta  t$ = %.2f s '\
                  %(self.N_A[0],self.N_B[0],self.tau,self.dt))
        plt.xlabel('Time (s)')
        plt.ylabel('Number of Nuclei')
        plt.xlim(0, self.T)
        plt.legend((p11,p12,p21,p22),
                   (r'$N_{A}(t)$ (Analytical Solution)',
                    r'$N_{A}(t)$ (Euler Method)',
                    r'$N_{B}(t)$ (Analytical Solution)',
                    r'$N_{B}(t)$ (Euler Method)'),
                   loc='best')
        plt.show()
