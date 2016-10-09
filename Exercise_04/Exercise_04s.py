# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
class resonance(object):
    def __init__(self, initial_number_of_nuclei_A, initial_number_of_nuclei_B,
                 time_constant_A, time_constant_B, time_of_duration, time_step):
        self.N_A = [initial_number_of_nuclei_A]
        self.N_B = [initial_number_of_nuclei_B]
        self.t = [0]
        self.tau_A = time_constant_A
        self.tau_B = time_constant_B
        self.dt = time_step
        self.T = time_of_duration
        self.nsteps = int(time_of_duration / time_step)
    def calculate(self):
        self.dN_A_dt = [self.N_B[0] / self.tau_B - self.N_A[0] / self.tau_A]
        self.dN_B_dt = [self.N_A[0] / self.tau_A - self.N_B[0] / self.tau_B]
        for i in range(self.nsteps):
            temp_A = self.N_A[i] + (self.dN_A_dt[i]) * self.dt
            temp_B = self.N_B[i] + (self.dN_B_dt[i]) * self.dt
            self.N_A.append(temp_A)
            self.N_B.append(temp_B)
            self.dN_A_dt.append(self.N_B[i+1] / self.tau_B - self.N_A[i+1] / self.tau_A)
            self.dN_B_dt.append(self.N_A[i+1] / self.tau_A - self.N_B[i+1] / self.tau_B)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        plt.subplot(211)
        p1,=plt.plot(self.t, self.N_A)
        p2,=plt.plot(self.t, self.N_B)
        plt.title(r'$N_{A0}$ = %d  $N_{B0}$ = %d  $\tau_{A}$ = %.2f s  $\tau_{B}$ = %.2f s  $\Delta  t$ = %.2f s '\
                  %(self.N_A[0],self.N_B[0],self.tau_A,self.tau_B,self.dt))
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
