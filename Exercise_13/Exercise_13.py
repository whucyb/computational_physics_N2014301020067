# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

'''
c = 300
Delta_x = 0.01
Delta_t = Delta_x / c
r = 1
y = [[0]]
t = [0]
k = 1000
x_0 = 0.3
for x in np.arange(Delta_x,1,Delta_x):
    y[-1].append(np.exp(- k * (x - x_0) ** 2))
y[-1].append(0)
y.append(y[-1])
while t[-1] < 0.04:
    y.append([0])
    for i in range(1,100):
        temp = 2 * (1 - r ** 2) * y[-2][i] - y[-3][i] + r ** 2 * (y[-2][i + 1] + y[-2][i - 1])
        y[-1].append(temp)
    y[-1].append(0)
    t.append(t[-1] + Delta_t)
f, ax = plt.subplots()
ax = plt.axes(title = 'Waves on a string\n(fixed ends)',xlim = (0,1), ylim = (-5,5),xlabel = 'x (m)',ylabel = 'y (m)') 
p, = ax.plot([],[])
x = np.arange(0,1 + Delta_x,Delta_x)
def animate(i):
    X = x
    Y = y[i]
    p.set_data(X,Y)  
    return p,  
gif = animation.FuncAnimation(f,animate,interval=50)
plt.show()
'''

'''
c = 300
Delta_x = 0.01
Delta_t = Delta_x / c
r = 1
y = [[0]]
t = [0]
k = 1000
x_0 = 0.55
for x in np.arange(Delta_x,1,Delta_x):
    y[-1].append(np.exp(- k * (x - x_0) ** 2))
y[-1].append(0)
y.append(y[-1])
while t[-1] < 0.04:
    y.append([0])
    for i in range(1,100):
        temp = 2 * (1 - r ** 2) * y[-2][i] - y[-3][i] + r ** 2 * (y[-2][i + 1] + y[-2][i - 1])
        y[-1].append(temp)
    y[-1].append(0)
    t.append(t[-1] + Delta_t)
signal = []
for i in range(1,len(y)):
    signal.append(y[i][5])
plt.plot(t,signal)
plt.title('String signal versus time')
plt.xlabel('Time (s)')
plt.ylabel('Signal (arbitrary units)')
plt.show()
'''

'''
c = 300
Delta_x = 0.01
Delta_t = Delta_x / c
r = 1
y = [[0]]
t = [0]
k = 1000
x_0 = 0.55
for x in np.arange(Delta_x,1,Delta_x):
    y[-1].append(np.exp(- k * (x - x_0) ** 2))
y[-1].append(0)
y.append(y[-1])
for n in range(1,1024):
    y.append([0])
    for i in range(1,100):
        temp = 2 * (1 - r ** 2) * y[-2][i] - y[-3][i] + r ** 2 * (y[-2][i + 1] + y[-2][i - 1])
        y[-1].append(temp)
    y[-1].append(0)
    t.append(Delta_t * n)
signal = []
for i in range(1,len(y)):
    signal.append(y[i][5])
power = np.fft.fft(signal)
fs = 1 / Delta_t
frequency = []
for i in range(1024):
    power[i] = abs(power[i])
    frequency.append(i * fs / 1024)
plt.plot(frequency,power)
plt.title('Power spectrum')
plt.xlabel('Frequency (Hz)')
plt.xlim(0,3000)
plt.ylabel('Power (arbitrary units)')
plt.show()
'''

'''
c = 300
Delta_x = 0.01
Delta_t = Delta_x / c
r = 1
y = [[0]]
t = [0]
k = 1000
x_0 = 0.3
for x in np.arange(Delta_x,1,Delta_x):
    if x <= x_0:
        y[-1].append(x / x_0)
    else:
        y[-1].append((1 - x) / (1 - x_0))
y[-1].append(0)
y.append(y[-1])
while t[-1] < 0.04:
    y.append([0])
    for i in range(1,100):
        temp = 2 * (1 - r ** 2) * y[-2][i] - y[-3][i] + r ** 2 * (y[-2][i + 1] + y[-2][i - 1])
        y[-1].append(temp)
    y[-1].append(0)
    t.append(t[-1] + Delta_t)
f, ax = plt.subplots()
ax = plt.axes(title = 'Waves on a string\n(fixed ends)',xlim = (0,1), ylim = (-5,5),xlabel = 'x (m)',ylabel = 'y (m)') 
p, = ax.plot([],[])
x = np.arange(0,1 + Delta_x,Delta_x)
def animate(i):
    X = x
    Y = y[i]
    p.set_data(X,Y)  
    return p,  
gif = animation.FuncAnimation(f,animate,interval=50)
plt.show()
'''

'''
c = 300
Delta_x = 0.01
Delta_t = Delta_x / c
r = 1
y = [[0]]
t = [0]
k = 1000
x_0 = 0.55
for x in np.arange(Delta_x,1,Delta_x):
    if x <= x_0:
        y[-1].append(x / x_0)
    else:
        y[-1].append((1 - x) / (1 - x_0))
y[-1].append(0)
y.append(y[-1])
while t[-1] < 0.04:
    y.append([0])
    for i in range(1,100):
        temp = 2 * (1 - r ** 2) * y[-2][i] - y[-3][i] + r ** 2 * (y[-2][i + 1] + y[-2][i - 1])
        y[-1].append(temp)
    y[-1].append(0)
    t.append(t[-1] + Delta_t)
signal = []
for i in range(1,len(y)):
    signal.append(y[i][5])
plt.plot(t,signal)
plt.title('String signal versus time')
plt.xlabel('Time (s)')
plt.ylabel('Signal (arbitrary units)')
plt.show()
'''

'''
c = 300
Delta_x = 0.01
Delta_t = Delta_x / c
r = 1
y = [[0]]
t = [0]
k = 1000
x_0 = 0.55
for x in np.arange(Delta_x,1,Delta_x):
    if x <= x_0:
        y[-1].append(x / x_0)
    else:
        y[-1].append((1 - x) / (1 - x_0))
y[-1].append(0)
y.append(y[-1])
for n in range(1,1024):
    y.append([0])
    for i in range(1,100):
        temp = 2 * (1 - r ** 2) * y[-2][i] - y[-3][i] + r ** 2 * (y[-2][i + 1] + y[-2][i - 1])
        y[-1].append(temp)
    y[-1].append(0)
    t.append(Delta_t * n)
signal = []
for i in range(1,len(y)):
    signal.append(y[i][5])
power = np.fft.fft(signal)
fs = 1 / Delta_t
frequency = []
for i in range(1024):
    power[i] = abs(power[i])
    frequency.append(i * fs / 1024)
plt.plot(frequency,power)
plt.title('Power spectrum')
plt.xlabel('Frequency (Hz)')
plt.xlim(0,3000)
plt.ylabel('Power (arbitrary units)')
plt.show()
'''

'''
c = 300
Delta_x = 0.01
Delta_t = Delta_x / c
r = 1
y = [[0]]
t = [0]
k = 1000
x_0 = 0.5
i_0 = 50
for x in np.arange(Delta_x,1,Delta_x):
    y[-1].append(np.exp(- k * (x - x_0) ** 2))
y[-1].append(0)
y.append(y[-1])
for n in range(1,1024):
    y.append([0])
    for i in range(1,100):
        temp = 2 * (1 - r ** 2) * y[-2][i] - y[-3][i] + r ** 2 * (y[-2][i + 1] + y[-2][i - 1])
        y[-1].append(temp)
    y[-1].append(0)
    t.append(Delta_t * n)
signal = []
for i in range(1,len(y)):
    signal.append(y[i][i_0])
power = np.fft.fft(signal)
fs = 1 / Delta_t
frequency = []
for i in range(1024):
    power[i] = abs(power[i])
    frequency.append(i * fs / 1024)
p, = plt.plot(frequency,power)
plt.title('Power spectrum')
plt.legend([p],[r'$x_0$' + ' = %.2f'%(i_0 * Delta_x)],loc = 'best')
plt.xlabel('Frequency (Hz)')
plt.xlim(0,3000)
plt.ylabel('Power (arbitrary units)')
plt.ylim(0,70)
plt.show()
'''

'''
c_1 = 300
Delta_x = 0.01
Delta_t = Delta_x / c_1
r_1 = 1
r_2 = 0.5
y = [[0]]
t = [0]
k = 1000
x_0 = 0.3
for x in np.arange(Delta_x,1,Delta_x):
    y[-1].append(np.exp(- k * (x - x_0) ** 2))
y[-1].append(0)
y.append(y[-1])
while t[-1] < 0.04:
    y.append([0])
    for i in range(1,100):
        if i <= 50:
            r = r_1
        else:
            r = r_2
        temp = 2 * (1 - r ** 2) * y[-2][i] - y[-3][i] + r ** 2 * (y[-2][i + 1] + y[-2][i - 1])
        y[-1].append(temp)
    y[-1].append(0)
    t.append(t[-1] + Delta_t)
f, ax = plt.subplots()
ax = plt.axes(title = 'Waves on a string\n(fixed ends)',xlim = (0,1), ylim = (-5,5),xlabel = 'x (m)',ylabel = 'y (m)') 
p, = ax.plot([],[])
x = np.arange(0,1 + Delta_x,Delta_x)
def animate(i):
    X = x
    Y = y[i]
    p.set_data(X,Y)  
    return p,  
gif = animation.FuncAnimation(f,animate,interval=50)
plt.show()
'''
