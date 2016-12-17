import numpy as np
import matplotlib.pyplot as plt

theta = np.load("theta.npy")
phi = np.load("angle.npy")
x_position = np.load("x_position.npy")
y_position = np.load("y_position.npy")
z_position = 0.02-0.02*0.3*np.cos(theta)

def trans(x,y,z):
    X = y- np.sqrt(2)/4.0*x
    Y = z- np.sqrt(2)/4.0*x
    return X, Y

N = 20000
for i in np.arange(0,N,10):
    XX = x_position[i]
    YY = y_position[i]
    ZZ = z_position[i]
    fig_x, fig_y = trans(XX, YY, ZZ)
    
    fig, ((ax1)) = plt.subplots(nrows=1, ncols=1)
    LB = "time = {:04.3f}".format(i/2500)
    ax1.set_xlim(-2.5, 2.5)
    ax1.set_ylim(-2.5, 2.5)
    ax1.set_aspect('equal')
    ax1.axes.get_xaxis().set_visible(False)
    ax1.axes.get_yaxis().set_visible(False)
    angle = np.linspace(0, 2*np.pi, 1000)
    angle1 = np.linspace(-0.5*np.pi, 0.5*np.pi, 1000)
    angle2 = np.linspace(0.5*np.pi, 1.5*np.pi, 1000)
    l1 = np.linspace(0, 0, 1000)
    l2 = np.linspace(-2.0, 2.0, 1000)
    ax1.plot(l1, l2, 'b', lw=1)#z
    ax1.plot(l2, l1-1, 'b', lw=1)#y
    l3 = np.linspace(-1.0/np.sqrt(2), 1.0/np.sqrt(2), 1000)
    ax1.plot(l3, l3-1, 'b', lw=1)#x
    #for j in np.linspace(0.1, 1, 9):
        #ax1.plot(l3, l3, 'b--', lw=1)#x
        #ax1.plot(l2, l1-1-j/np.sqrt(2)*0.5, 'b--', lw=1)#y
    point_X, point_Y = trans(np.sin(theta[i])*np.cos(phi[i]), np.sin(theta[i])*np.sin(phi[i]), np.cos(theta[i]))
    X = np.linspace(-point_X, point_X*1.5, 1000)
    Y = np.linspace(-point_Y, point_Y*1.5, 1000)
    ax1.plot(fig_x+X, fig_y+Y, 'r', lw=2, label=LB)#point
    #print(i)
    ax1.plot(fig_x+np.cos(angle), fig_y+np.sin(angle), 'k', lw=1)#x circle
    ax1.plot(fig_x+trans(np.cos(angle1), np.sin(angle1), 0)[0], fig_y+trans(np.cos(angle1), np.sin(angle1), 0)[1], 'k', lw=1)#z circle
    ax1.plot(fig_x+trans(np.cos(angle2), np.sin(angle2), 0)[0], fig_y+trans(np.cos(angle2), np.sin(angle2), 0)[1], 'k--', lw=1)
    ax1.plot(fig_x+trans(np.cos(angle1), 0, np.sin(angle1))[0], fig_y+trans(np.cos(angle1), 0, np.sin(angle1))[1], 'k', lw=1)#y circle
    ax1.plot(fig_x+trans(np.cos(angle2), 0, np.sin(angle2))[0], fig_y+trans(np.cos(angle2), 0, np.sin(angle2))[1], 'k--', lw=1)
    ax1.plot(fig_x+trans(np.sin(theta[i])*np.cos(angle1), np.sin(theta[i])*np.sin(angle1), np.cos(theta[i]))[0], fig_y+trans(np.sin(theta[i])*np.cos(angle1), np.sin(theta[i])*np.sin(angle1), np.cos(theta[i]))[1], 'g', lw=1)#small circle
    ax1.plot(fig_x+trans(np.sin(theta[i])*np.cos(angle2), np.sin(theta[i])*np.sin(angle2), np.cos(theta[i]))[0], fig_y+trans(np.sin(theta[i])*np.cos(angle2), np.sin(theta[i])*np.sin(angle2), np.cos(theta[i]))[1], 'g--', lw=1)
    plt.legend(loc = 2)
    string = "figure_test/image_{0:06d}.png".format(i)#第一个0是第一个format的变量
    #冒号之后的东西是format的形式。d是整数，04是至少4位，0开头。
    fig.savefig(string,dpi=200)
    #plt.show()
    plt.close(fig)