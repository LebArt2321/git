from cmath import cos, sin
import math

def F(x):
    return x*x

    
a, b, h = float(input()), float(input()), float(input())
a, b, h = int(a*10000), int(b*10000), int(h*10000)
for i in range(a, b+h, h):
    print("i = {}, x = {}".format(float(i)/10000, F(float(i)/10000)))