import numpy as np
import matplotlib.pyplot as plt

# LaTeX font
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'


sigma = 3.475e-06
mu = 1.00030167
x = np.linspace(1.0002,1.0004,10000)

y = np.exp(-((x-mu)/sigma)**2/2)/np.sqrt(2*np.pi*sigma**2)

plt.plot(x,y)
plt.show()