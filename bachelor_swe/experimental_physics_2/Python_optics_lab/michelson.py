import matplotlib.pyplot as plt
import numpy as np


# LaTeX font
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'



N               = 2**10                 # NxN är antalet samplade punkter (rekommenderad storlek N=1024)
sidlaengd_Plan1 = 4e-3                  # Det samplade områdets storlek (i x- eller y-led) i Plan 1 (rekommenderad storlek 4 mm)
a               = sidlaengd_Plan1/N  

nl = 1.00029
nk = np.linspace(nl,1,10000)
dn = nl - nk
lamb = 633e-9
l = 0.5e-2
L = 0.1 

x = np.arange(-(N/2)*a, (N/2)*a, a)     # Vektor med sampelpositioner i x-led
y = x                                   # och y-led

X, Y = np.meshgrid(x, y)                # Koordinatmatriser med x- och y-värdet i varje sampelposition
R    = np.sqrt(X**2 + Y**2)   
E1_in_konst= np.ones(X.shape)   
k = 2*np.math.pi/(lamb/nl)
f_lins = L                     # Fokallängd på linsen före Plan 1
T_lins = np.exp(-1j*k*R**2/(2*f_lins))  # Transmissionsfunktion för en lins

D_aperture = 2e-3                       # Diameter för apertur
T_aperture = R < (D_aperture/2) 



E1_cirkular = E1_in_konst*T_lins*T_aperture  # Fältet i Plan 1 (precis efter linsen) för konstant fält som passerat genom cirkulär apertur *** Ej klar 
E1          = E1_cirkular               # Välj fall!

I = 1 + np.cos(4*np.pi*dn*l/lamb)

I1      = np.abs(E1)**2     # Intensiteten är prop mot kvadraten på fältets amplitud (normalt struntar man i proportionalitetskonstanten)
I1_norm = I1/np.max(I1) 


x_mm = x*1e3
y_mm = y*1e3

image = plt.imshow(I1_norm,cmap='hot',extent=[x_mm.min(),x_mm.max(),y_mm.min(),y_mm.max()])
plt.clim(0, 0.5)            # Mättnadsfaktor för apertur
plt.colorbar(image)

#plt.title(r'Intensitet i plan 1. Verkar OK, eller?')
plt.xlabel(r'x $[$mm$]$')
plt.ylabel(r'y $[$mm$]$')
plt.show()