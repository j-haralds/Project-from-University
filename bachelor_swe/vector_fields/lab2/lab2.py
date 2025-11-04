## Uppg.1

from numpy import *
import matplotlib.pyplot as plt

rho = 1500
lambda_ = 1  
c = 1000
k = lambda_/(c*rho)
K = 0.25

x = linspace(0,1,30)
dx = x[1]
dt = K * dx**2/k


T_0 = -10
T_n = 0
s=0
T_new = zeros(x.size)
T_old = zeros(x.size)
S = s*ones(x.size)
u = S/(rho*c) 
t=0
eps = 10**-10
j = 0
T_p = zeros(x.size)

while True:
      for i in range(x.size):     
            
            if i ==0:      
                  T_new[i] = T_0
            elif i == 29:
                  T_new[i] = T_n
            
            else:
                  T_new[i] = T_old[i] + k*dt*(T_old[i+1]-2*T_old[i]+T_old[i-1])/(dx**2)

            T_p=(T_new-T_old) / dt
      t += dt
      
      

      #if (int(t/dt))//10:
      #      T_new_new.append(T_new)

      if linalg.norm(T_p)<eps:
      #if t/dt > 100:
            break 
      
      
      T_old = copy(T_new)
      



      
print(T_new,'tiden blir',t/3600, 'iterationer:',int(t/(dt)))

X = linspace(0,30,30)
plt.plot(X,T_new);plt.show()

      

      