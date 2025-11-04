import numpy as np
import matplotlib.pyplot as plt

# LaTeX font
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'

# Definitions
rho = 1500  # Density
c = 1000  # Specific heat capacity
l = 1  # Thermal conductivity
k = l/(c*rho)
K = 0.25
m = 30  # Number of points
d = 1  # Total depth
x = np.linspace(0, d, m)
dx = d/(m-1)
dt = K*(dx**2/k)

T_old = np.zeros(m)  # Temperature, old values
T_new = np.zeros(m)  # Temperature, new values
T_old[0] = -10
T_old[m-1] = 0

s = np.zeros(m)
u = s/(c*rho)

t = 0
eps = 10**-10

T_plots = []

cont = True




while cont:

      for i in range(x.size):
            if i == 0 or i == 29:
                  T_new[i] = T_old[i]
            else:
                  T_new[i] = T_old[i] + dt*k*(T_old[i+1]-2*T_old[i]+T_old[i-1])/dx**2 + dt*u[i]

      if int(t/dt) % 50 == 0:
            T_plots.append(T_new.copy())

      t += dt
      T_prime = (T_new - T_old)/dt
      if np.linalg.norm(T_prime) < eps:
            cont = False
      T_old = np.copy(T_new)
    







print('Time (s):', t)
print('Time (h):', t/3600)
print('Time (d):', t/(3600*24))
print('Number of iterations:', int(t/dt))

colormap = plt.cm.winter
plt.gca().set_prop_cycle(plt.cycler('color', colormap(np.linspace(0, 1, len(T_plots)))))

# Plots
for i in range(len(T_plots)):
    plt.plot(T_plots[i], x)

# Analytic plot
plt.plot(10*x-10, x, 'k:')

plt.xlabel('Temperatur ($^{\circ}$C)', fontsize=11)
plt.ylabel('Djup (m)', fontsize=11)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])
plt.show()
