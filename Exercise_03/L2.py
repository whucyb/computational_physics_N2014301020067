# -*- coding: utf-8 -*-
import os
import time
os.system('cls')
l=40
h=30
a=[[' ' for i in range(80)] for j in range(80)]
b=[[' ' for i in range(80)] for j in range(80)]
a[38][39]='*'
a[38][40]='*'
a[39][38]='*'
a[39][39]='*'
a[39][40]='*'
a[39][41]='*'
a[40][38]='*'
a[40][39]='*'
a[40][40]='*'
a[40][41]='*'
a[41][39]='*'
a[41][40]='*'
for t in range(l/2-2):
    for i in range(38-(h/2-2),38+h-(h/2-2)):
        for j in range(38-t,38+l-t):
            print a[i][j],
        print ''
    time.sleep(0.05)
    os.system('cls')
for i in range(38-(h/2-2),38+h-(h/2-2)):
        for j in range(l/2,l/2+l):
            print a[i][j],
        print ''
time.sleep(0.1)
os.system('cls')
for k in range(4):
    n=0
    for t in range(5):
        a[42+t][39]='*'
        a[42+t+n][40]='*'
        n=n+1
        a[42+t+n][40]='*'
        for i in range(38-(h/2-2),38+h-(h/2-2)):
            for j in range(l/2,l/2+l):
                print a[i][j],
            print ''
        time.sleep(0.1)
        os.system('cls')
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
    time.sleep(0.5)
    os.system('cls')
for k in range(4):
    n=5
    for t in range(5)[::-1]:
        a[37-t][40]=' '
        a[37-t-n][39]=' '
        n=n-1
        a[37-t-n][39]=' '
        for i in range(38-(h/2-2),38+h-(h/2-2)):
            for j in range(l/2,l/2+l):
                print a[i][j],
            print ''
        time.sleep(0.1)
        os.system('cls')
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
    time.sleep(0.5)
    os.system('cls')        
for t in range(l/2-1,l-3):
    for i in range(38-(h/2-2),38+h-(h/2-2)):
        for j in range(38-t,38+l-t):
            print a[i][j],
        print ''
    time.sleep(0.05)
    os.system('cls')   