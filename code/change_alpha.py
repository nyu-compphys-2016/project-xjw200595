import numpy as np
import matplotlib.pyplot as plt
from myfun import RK4, RK4_AD


from scipy.integrate import odeint


def ddtheta(theta, dot_theta, dot_phi, omega, vx, vy, gn):
    solution = np.sin(theta)/I1*(I1*dot_phi**2*np.cos(theta) - I3*omega*dot_phi - R*alpha*gn) + R*mu*gn*vx/I1*(1-alpha*np.cos(theta))
    return solution

def ddphi(theta, dot_theta, dot_phi, omega, vx, vy, gn):
    solution = (I3*dot_theta*omega - 2*I1*dot_theta*dot_phi*np.cos(theta) - mu*gn*vy*R*(alpha-np.cos(theta)))/(I1*np.sin(theta))
    return solution
        
def domega(theta, dot_theta, dot_phi, omega, vx, vy, gn):
    solution = -mu*gn*vy*R*np.sin(theta)/I3
    return solution
    
def dvx(theta, dot_theta, dot_phi, omega, vx, vy, gn):
    part1 = R*np.sin(theta)/I1*(dot_phi*omega*(I3*(1-alpha*np.cos(theta))-I1) + gn*R*alpha*(1-alpha*np.cos(theta)) - I1*alpha*(dot_theta**2+dot_phi**2*np.sin(theta)**2))
    part2 = -mu*gn*vx/m/I1*(I1 + m*R**2*(1-alpha*np.cos(theta))**2) + dot_phi*vy
    solution = part1 + part2
    return solution
    
def dvy(theta, dot_theta, dot_phi, omega, vx, vy, gn):
    part1 = -mu*gn*vy/(m*I1*I3)*(I1*I3 + m*R**2*I3*(alpha-np.cos(theta))**2 + m*R**2*I1*np.sin(theta)**2)
    part2 = omega*dot_theta*R/I1*(I3*(alpha-np.cos(theta)) + I1*np.cos(theta)) - dot_phi*vx
    solution = part1 + part2
    return solution

def f_gn(theta, dot_theta, dot_phi, omega, vx, vy):
    upper = m*g*I1 + m*R*alpha*(np.cos(theta)*(I1*dot_phi**2*np.sin(theta)**2 + I1*dot_theta**2) - I3*dot_phi*omega*np.sin(theta)**2)
    bottom = I1 + m*R**2*alpha**2*np.sin(theta)**2 - m*R**2*alpha*np.sin(theta)*(1-alpha*np.cos(theta))*mu*vx
    solution = float(upper)/bottom
    return solution

def Energy(theta, dot_theta, dot_phi, omega):
    part1 = 0.5*(I1*dot_phi**2*np.sin(theta)**2 + I1*dot_theta**2 + I3*omega**2)
    part2 = m*g*R*(1-np.cos(theta))
    part3 = 0.5*m*R**2*((alpha-np.cos(theta))**2*(dot_theta**2+dot_phi**2*np.sin(theta)**2) + np.sin(theta)**2*(dot_theta**2 + omega**2 + 2*omega*dot_phi*(alpha-np.cos(theta))))
    solution = part1 + part2 + part3
    return solution

def ODE(x ,t):
    gn = f_gn(x[0], x[1], x[2], x[3], x[4], x[5])
    dx0 = x[1]
    dx1 = ddtheta(x[0], x[1], x[2], x[3], x[4], x[5], gn)
    dx2 = ddphi(x[0], x[1], x[2], x[3], x[4], x[5], gn)
    dx3 = domega(x[0], x[1], x[2], x[3], x[4], x[5], gn)
    dx4 = dvx(x[0], x[1], x[2], x[3], x[4], x[5], gn)
    dx5 = dvy(x[0], x[1], x[2], x[3], x[4], x[5], gn)
    return np.array([dx0, dx1, dx2, dx3, dx4, dx5])

    

for i in np.arange(-1.0, 0.0, 0.05):
    alpha = float(i)
    
    g = 9.82
    mu = 0.3
    m = 0.02
    R = 0.02
    #alpha = 0.3
    I1 = 131/350*m*R**2
    I3 = 0.4*m*R**2   
        
    t_end = 8.0
    time = np.linspace(0.0, t_end, 20000)
    
    theta = 0.1
    dot_theta = 0.0
    dot_phi = 0.0
    omega = 155.0
    vx = 0.0
    vy = 0.0
    x_0 = np.array([theta, dot_theta, dot_phi, omega, vx, vy])  
    
    
    sigma = 0.01
    h = 0.00001
    
    time, y = RK4_AD(ODE, 0.0, t_end, x_0, sigma, h)
    


    fig, ((ax1)) = plt.subplots(nrows=1, ncols=1)
    LB = r"$\alpha=$" + str(i)
    ax1.plot(time,y[:,0],label=LB)
    #ax1.plot([0,8],[0.5*np.pi,0.5*np.pi])
    #ax1.plot([0,8],[np.pi,np.pi])
    ax1.plot([0,8],[0,0])
    ax1.set_ylim(0,0.1)
    ax1.legend(loc=2)
    ax1.set_ylabel(r"$\theta$/rad")
    ax1.set_xlabel("time/s")
    j = int(1000*i)
    string = "figure_nagative/image_{0:06d}.png".format(j)#第一个0是第一个format的变量
    #冒号之后的东西是format的形式。d是整数，04是至少4位，0开头。
    fig.savefig(string)
    #plt.show()
    plt.close(fig)