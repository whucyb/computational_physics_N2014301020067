# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
x_1=np.linspace(1,5)
x_2=np.linspace(1,5,10)
y_1=25/x_1
y_2=x_2**2
p1,=plt.plot(x_1, y_1,'r-')
p1.set_dashes([10,5,2,5])
p2,=plt.plot(x_2, y_2,'cD')
plt.grid()
plt.title('Figure')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.xlim(0.8, 5.2)
plt.ylim(0.0, 26.0)
plt.legend((p1,p2),(r'$y=\frac{25}{x}$',r'$y=x^2$'), loc='best')
plt.show()