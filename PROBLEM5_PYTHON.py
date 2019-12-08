import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(0,199,200)

def conv(n):
    w = eval(x)
    return w
    
x = input('Input X(n): ')

for z in range(0,200):
    if z == 0:
        y = (-1.5*conv(n)) + (2*conv(n+1)) - (0.5*conv(n+2))

    elif z <= 198:
        y= 0.5*conv(n+1) - 0.5*conv(n-1)
       
    elif z == 199:
        y = 1.5*conv(n) - 2*conv(n-1) + 0.5*conv(n-2)
        
plt.plot(conv(n),color="b",label="Line of x(n)")
plt.plot(y,color="r",label="Line of y(n)")
plt.grid()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show

        