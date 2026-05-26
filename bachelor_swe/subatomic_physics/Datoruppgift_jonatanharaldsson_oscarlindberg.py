# Jonatan Haraldsson jonhara
# Oscar Lindberg oscarlin

import numpy as np
import scipy.constants as K
from pyteomics import mass
import matplotlib.pyplot as plt
from scipy import integrate

# LaTeX font to plots
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'

# --- Some constants ---
hbar = K.Planck / (2 * np.pi)
c = K.speed_of_light
e = K.elementary_charge
me = K.electron_mass
mp = K.proton_mass
mn = K.neutron_mass
fm = K.femto

# --- Theoretical values ---
Ed_exp = -2.224e6 * e
rd_ex = 1.97 * fm

# Malfliet-Tjon potential
def pot_MT(r):
    a1 = -586.04
    a2 = 1458.19
    a3 = -872.15
    mu1 = 1.55
    mu2 = 3.11
    mu3 = 6
    V1 = a1 * np.exp(-mu1 * r)
    V2 = a2 * np.exp(-mu2 * r)
    V3 = a3 * np.exp(-mu3 * r)
    return (V1 + V2 + V3) / r   

# Conversion functions
def MeV_to_kg(m):
    M = 10**6 * m * e/c**2
    return M


def kg_to_MeV(m):
    M = m * c**2 / (10**6*e)
    return M


rmax = 20
N = 10000
h = rmax / N
mu = kg_to_MeV(mp * mn / (mp + mn)) # µ in MeV
hc = hbar /(e * 1e6) * c /fm # conversion factor hc ≈ 197.327 MeV fm
K = 2 * mu / hc**2  

r = np.linspace(1e-16, rmax, N+1)
u = np.zeros(N+1)
F = np.zeros(N+1)
Vr = np.zeros(N+1)

for i in range(0, N):
    Vr[i] = pot_MT(r[i])

# Parameters 
Emin = np.min(Vr)
Emax = 0
E = 0.5 * (Emin + Emax)  
max_iter = 1000  
tol_kont = 1e-20  

# Loop for iterating over energies E
for i in range(0, max_iter):
    for j in range(0, N):
        F[j] = K * (Vr[j] - E)


    # Choosing matching point where r ≈ 1 fm
    rmp_i = list(r).index(1)

    # Initialise out-integrated wave funciton
    u[0] = 0
    u[1] = h

    # Numerov out
    for j in range(2, rmp_i+1):
        u[j] = (u[j-1]*(2+5/6*h**2*F[j-1])-u[j-2]*(1-1/12*h**2*F[j-2]))/(1-1/12*h**2*F[j])
    u_out = u[rmp_i]

    #Initialise in-integrated wave funciton
    u[N] = 0  
    u[N - 1] = h

    # Numerov inåt
    for j in range(N-2, rmp_i-1, -1):
        u[j] = (u[j+1]*(2+5/6*h**2*F[j+1])-u[j+2]*(1-1/12*h**2*F[j+2]))/(1-1/12*h**2*F[j])
    u_in = u[rmp_i]

    # Scale factors between wave funcitons 
    scale = u_out / u_in

    # Matching the height of the inner and outer wave function
    u[rmp_i:N] = scale * u[rmp_i:N]

    # Calulating discontiuity at the matching point
    matchning = 1/h*(u[rmp_i-1]+u[rmp_i+1]-u[rmp_i]*(2+h**2*F[rmp_i])) 

    # Update E in every loop
    if np.abs(matchning) < tol_kont:
        break
    if u[rmp_i] * matchning > 0:
        Emax = E
    else:
        Emin = E
    E = (Emin + Emax) / 2

u_int = integrate.trapezoid(u**2,r,h) 
u = u/np.sqrt(u_int) # Normalized wave function

R = np.sqrt(integrate.trapezoid((u*r)**2,r,h))
rd = R / 2

rd = np.round(rd,4)
print(f'rd = {rd} fm')
E = np.round(E,4)
print(f'Ed = {E} MeV')


# Plotting resulting wave function and potential
font_size = 16
tick_size = 13
plt.figure(1)
plt.plot(r, u,linewidth = 2.5)
plt.xlabel('$r\,$[fm]',fontsize=font_size)
plt.ylabel('$u(r)\,$[fm$^{-0,\!5}]$',fontsize=font_size)
plt.xticks(fontsize = tick_size)
plt.yticks(fontsize = tick_size)

plt.figure(2)
plt.plot(r, Vr,linewidth = 2.5,color='black')
plt.xlim([0,4])
plt.ylim([-80,150])
plt.xlabel('$r\,$[fm]',fontsize=font_size)
plt.ylabel('$V(r)\,$[MeV]',fontsize=font_size)
plt.xticks(fontsize = tick_size)
plt.yticks(fontsize = tick_size)
plt.show()