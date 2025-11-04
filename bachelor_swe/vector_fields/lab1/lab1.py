# Import modules.
# pylab contains matplotlib
from matplotlib import scale
from numpy import *
import pylab as p
import matplotlib.pyplot as plt
from matplotlib import colors
#from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
#plt.rc('text', usetex=True)
# Read data


P = loadtxt('/Users/Marias/Dropbox/Utbildning/0_Högskola/Pågående kurser/FFM234 Vektorfält/Datorlab/tryckfalt.dat.txt')
u = loadtxt('/Users/Marias/Dropbox/Utbildning/0_Högskola/Pågående kurser/FFM234 Vektorfält/Datorlab/vindfalt_u.dat.txt')
v = loadtxt('/Users/Marias/Dropbox/Utbildning/0_Högskola/Pågående kurser/FFM234 Vektorfält/Datorlab/vindfalt_v.dat.txt')


x = linspace(0, 55*30,31)
y = linspace(0, 55*29,30)

#skapar meshgrid
X,Y = meshgrid(x,y)

#A = (u**2 + v**2)**0.5 
#print('Maximal vind ges av ',A.max())
# LaTeX font
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'

def isobarer(X,Y,P):

      fig,ax = plt.subplots()
      CS = ax.contour(X, Y, P,20,linewidths=0.6,colors = 'black')
      #ax.clabel(CS, inline=True,fmt='%1.f', fontsize=10)
      ax.set_title('Isobarer över tryckfält')
      plt.gca().set_aspect('equal',adjustable='box')
      plt.show()

# ---VINDFÄLT--

def streamline(X,Y,u,v):
      fig,ax = plt.subplots()
      strm = ax.streamplot(X,Y,u,v,density=3, color = (u**2 + v**2)**0.5, linewidth=0.6,cmap=plt.cm.autumn)
      colbar = plt.colorbar(strm.lines)
      colbar.set_label('Vindhastighet [m/s]');ax.set_title('$\Omega$ Vindfältet')
      p.xlabel('$x$'),p.ylabel('$y$')
      plt.show()
      
      
def quiver(X,Y,u,v):
      fig,ax = plt.subplots()
      ax.quiver(X,Y,u,v,30)
      #ax.barbs(X, Y,u,v)
      plt.show()

def Div_curl(u,v):
      dx=1;dy=1
      dudx = gradient(u,dx,axis=1,edge_order=2)
      dudy = gradient(u,dy,axis=0,edge_order=2)
      dvdx = gradient(v,dx,axis=1,edge_order=2)
      dvdy = gradient(v,dy,axis=0,edge_order=2)
      div = (dudx + dvdy)
      curl = dvdx - dudy
      D_C = [div,curl]
      return D_C

def plotdiv(X,Y,u,v,P):
      div = Div_curl(u,v)[0]
      fig,ax = plt.subplots()
      CS = ax.contourf(X, Y, div ,50,cmap=plt.cm.Spectral) #Spectral är snygg cmap
      
      #divnorm=colors.TwoSlopeNorm(vmin=-5., vcenter=0., vmax=10)
      #pcolormesh(your_data, cmap="coolwarm", norm=divnorm)
      cb = p.colorbar(CS)
      #strm = p.streamplot(X,Y,u,v,density=2, color = (u**2 + v**2)**0.5,cmap=plt.cm.gray, linewidth=0.6)
      #colbar=p.colorbar(strm.lines)
      #ax.quiver(X,Y,u,v,60)
      ax.set_title('Divergens och fältlinjer av vindfält')
      CS = ax.contour(X, Y, P,45,linewidths=0.6,colors='k')
      #ax.clabel(CS, inline=True,fmt='%1.f', fontsize=10)
      
      plt.gca().set_aspect('equal',adjustable='box')

      plt.show()

def plotcurl(X,Y,u,v):
      curl = Div_curl(u,v)[1]
      fig,ax = plt.subplots()
      CS = ax.contourf(X, Y, curl ,100,cmap=p.cm.Spectral) #Spectral är snygg cmap
      cb = p.colorbar(CS)
      #strm = p.streamplot(X,Y,u,v,density=3, color = (u**2 + v**2)**0.5,cmap=plt.cm.gray, linewidth=1)
      #colbar=p.colorbar(strm.lines)
      ax.quiver(X,Y,u,v,40,color='k')
      #ax.set_title('Rotation och fältlinjer av vindfält')
      plt.show()

#plotdiv(X,Y,u,v,P)
#streamline(X,Y,u,v)
isobarer(X,Y,P)
#plotcurl(X,Y,u,v)
#plt.show()