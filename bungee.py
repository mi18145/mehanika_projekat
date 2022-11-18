import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig,ax=plt.subplots()
dt=1e-2
def animate(i):     
    #konstante
    gamma=6.67e-11
    M_earth=5.972e24
    R_earth=6371000
    rho0=1.2255 #gustina vazduha
    h0=10000.
    el_coef=2000.662 #za kabl 228667
    drag_coef=0.47 #za loptu
    body_density=985. #prosecna gustina 985.
    body_r=0.75 #duzina poluprecnika lopte
    l=100. #duzina kabla
    h=1000. #pocetna visina
    v_start=1.5 #pocetna vx
    dt=1e-2
    
    #ostalo
    body_mass=body_density*4/3*math.pi*body_r**3
    body_area=body_r**2*math.pi
    pos=np.array([0.,h])
    pos_start=np.array([0.,h])
    vel=np.array([v_start,0.])
    t=0
    
    X=[pos[0]]
    Y=[pos[1]]
    while t<1000:    
        vel_int=np.linalg.norm(vel)
        h=pos[1]+R_earth
        g=-np.array([0.,gamma*M_earth/h**2])
        rho=rho0*math.exp(-pos[1]/h0)
        drag=-0.5*rho*vel_int*vel*body_area*drag_coef/body_mass
        acc=g+drag
        pos_dif=pos_start-pos
        strech=np.linalg.norm(pos_dif)-l
        if strech>0:
            el_acc=pos_dif/(strech+l)*strech*el_coef/body_mass
            acc+=el_acc
        vel+=acc*dt
        pos+=vel*dt
        X.append(pos[0])
        Y.append(pos[1])
        ax.clear()
        ax.plot(X,Y)
        t+=dt

ani=animation.FuncAnimation(fig,animate,interval=(dt*1000))
plt.show()
  
#pravljenje i prikazivanje grafika
#Xosa=np.array(X)
#Yosa=np.array(Y)
#plt.plot(Xosa,Yosa)
#plt.show()