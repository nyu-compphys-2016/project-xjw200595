import numpy as np


L = len(time)

phi = np.zeros(L)
p = 0
phi[0] = p

x_position = np.zeros(L)
xx = 0
x_position[0] = xx

y_position = np.zeros(L)
yy = 0
y_position[0] = yy

angle = np.zeros(L)
a = 0
angle[0] = a

for i in range(L-1):
    p = p + (time[i+1] - time[i]) * y[i+1,3]
    phi[i+1] = p

    xx = xx + (time[i+1] - time[i]) * y[i+1,4]
    x_position[i+1] = xx

    yy = yy + (time[i+1] - time[i]) * y[i+1,5]
    y_position[i+1] = yy

    a = a + (time[i+1] - time[i]) * y[i+1,2]
    angle[i+1] = a


np.save("theta", y[:,0])
np.save("phi", phi)    
np.save("x_position", x_position)     
np.save("y_position", y_position)
np.save("angle",angle)