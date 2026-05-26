
import matplotlib.pyplot as plt
import numpy as np

# LaTeX font
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'


lambda_ = 633e-9    
pl = 9.95e+04          
l = 4.50e-2            
k = 2426.88            

E = ['lambda','pl','l','k']
#Expression for n_l:

dp = [1656.1,4045.3,6363.7,8799.2,11366.85,13669.8,16035.4,18589.7,21195.6,23431,25951.2,28151.1]
N = [1,2,3,4,5,6,7,8,9,10,11,12]
A = np.vstack([N, np.ones(len(N))]).T
m, c = np.linalg.lstsq(A, dp, rcond=None)[0]
x = np.linspace(1,12)
plt.plot(x,(m*x + c),color='black',linestyle='dashed')
plt.scatter(N,dp,marker='o',facecolor = 'none',edgecolor='tab:blue')
#plt.scatter(N,dp,marker='x',sizes=40*np.ones(len(N)))#,facecolor = 'none',edgecolor='tab:blue')

plt.show()

mu = 4.7015e-2

deltanl =0.5e-4#0.5e-2# 4.414882395485211e-06


l = np.linspace(3.57e-2,5.42e-2,1000)
y = np.linspace(1,1.0005,1000)

ntabell = 1.000276*np.ones(len(l))

mu = 4.7e-2*np.ones(len(l))
mu0 = 4.48e-2*np.ones(len(l))
stdmax =(mu0+deltanl)*np.ones(len(l))
stdmin = (mu0-deltanl)*np.ones(len(l))

nl = 1 + lambda_*pl/(2*l*k) 
y = np.linspace(min(nl),max(nl),1000)

plt.plot(l,nl)
plt.plot(l,ntabell,linestyle='dotted',linewidth=0.9,color='black')
#plt.plot(mu,y,linestyle='dotted',linewidth=0.75,color='black')
plt.plot(mu0,y,linestyle='dotted',linewidth=0.95,color='black')
plt.plot(stdmax,y,linestyle='dotted',linewidth=1.1,color='tab:red')
plt.plot(stdmin,y,linestyle='dotted',linewidth=1.1,color='tab:red')
plt.show()
plt.clf()