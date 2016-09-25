# -*- coding: utf-8 -*-
import os
import time
os.system('cls')
l=40
h=30
a=[[' ' for i in range(80)] for j in range(80)]
b=[[' ' for i in range(80)] for j in range(80)]
c=[[38,39],[38,40],[39,38],[39,39],[39,40],[39,41],
   [40,38],[40,39],[40,40],[40,41],[41,39],[41,40]]
for i in range(12):
    a[c[i][0]][c[i][1]]='*'
#初始化a中包含的图形
def move(x_1,x_2):
    for t in range(x_1,x_2):
        for i in range(38-(h/2-2),38+h-(h/2-2)):
            for j in range(38-t,38+l-t):
                print a[i][j],
            print ''
        time.sleep(0.1)
        os.system('cls')
#move函数用以移动
def spin():
    for i in range(80):
        for j in range(80):
            b[79-j][i]=a[i][j]
    for i in range(80):
        for j in range(80):
            a[i][j]=b[i][j]
    for i in range(38-(h/2-2),38+h-(h/2-2)):
            for j in range(l/2,l/2+l):
                print a[i][j],
            print ''
    time.sleep(0.1)
    os.system('cls')
#spin函数用以转动
def los(m,t_1,t_2,x_1,x_2,y,char):
    for k in range(4):
        n=m
        for t in range(t_1,t_2):
            a[y+t][x_1]=char
            a[y+t+n][x_2]=char
            n=n+1
            a[y+t+n][x_2]=char
            for i in range(38-(h/2-2),38+h-(h/2-2)):
                for j in range(l/2,l/2+l):
                    print a[i][j],
                print ''
            time.sleep(0.1)
            os.system('cls')
        spin()
#los函数用以伸长或缩短
move(0,l/2-1)
los(0,0,5,39,40,42,'*')
los(-5,-4,1,40,39,37,' ')
move(l/2-1,l-3)