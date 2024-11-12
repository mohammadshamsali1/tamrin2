import sys
EPSILON =ie-15
c= float(sys.argv[1])
t = c
while abs (t-c/t)>(EPSILON*t):
    t= (c/t + t) / 2.0
    print(t)