import numpy as np
import matplotlib.pyplot as plt
from myfun import RK4, RK4_AD, Energy, ODE


from scipy.integrate import odeint



    

g = 9.82
mu = 0.3
m = 0.02
R = 0.02
alpha = 0.3
I1 = 131/350*m*R**2
I3 = 0.4*m*R**2   
    
t_end = 8.0
time = np.linspace(0.0, t_end, 20000)



for i in np.linspace(0.0,0.5,51):
    theta = float(i)
    
    #theta = 0.1
    dot_theta = 0.0
    dot_phi = 0.0
    omega = 160.0
    vx = 0.0
    vy = 0.0
    x_0 = np.array([theta, dot_theta, dot_phi, omega, vx, vy])  
    
    
    sigma = 0.01
    h = 0.00001
    
    time, y = RK4_AD(ODE, 0.0, t_end, x_0, sigma, h)
    
    
    
    fig, ((ax1)) = plt.subplots(nrows=1, ncols=1)
    LB = r"$\theta_0=$" + str(i)
    ax1.plot(time,y[:,0],label=LB)#r"$\omega=$")
    ax1.plot([0,8],[0.5*np.pi,0.5*np.pi])
    ax1.plot([0,8],[np.pi,np.pi])
    ax1.set_ylim(0,np.pi+0.1)
    ax1.legend(loc=2)
    ax1.set_ylabel(r"$\theta$/rad")
    ax1.set_xlabel("time/s")
    j = int(1000*i)
    string = "figure_theta/image_{0:06d}.png".format(j)#第一个0是第一个format的变量
    #冒号之后的东西是format的形式。d是整数，04是至少4位，0开头。
    fig.savefig(string)
    plt.close(fig)

