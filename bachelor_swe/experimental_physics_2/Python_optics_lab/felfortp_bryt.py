from numpy import * 
#Parameters; errors:
lambda_ = 632.8e-9      ; dlambda = 0.1e-9
p0 = 9.95e+04           ; dp0 = 500
#p0 = 9.95e+04           ; dp0 = 250
l = 4.50e-2            ; dl = 0.5e-2
#l = 4.50e-2            ; dl = 0.1e-3
k = 2426.88            ; dk = 19.196/sqrt(10)   

E = ['lambda','p0','l','k']
#Expression for n_l:
nl = 1 + lambda_*p0/(2*l*k) 
err = [dlambda,dp0,dl,dk]

#Partial derivatives:
part_der = [(p0)/(2*k*l),lambda_/(2*l*k),
            -(lambda_*p0)/(2*k*l**2), -(lambda_*p0)/(2*l*k**2)]

delta_nl = 0; errlist=[]
for i in range(len(err)):
      delta_nl += abs(part_der[i])*err[i]
      errlist.append(abs(part_der[i])*err[i])
marg = delta_nl/nl
print('n =',nl,'±',(delta_nl)) #Printing error margin 
print('Felmarginal',marg*100,'%')

max_index = errlist.index(max(errlist)) #Find the index of the max error. 
print(f'{E[max_index]}, andel av totalt fel:',(100*errlist[max_index])/delta_nl,'%') 
print('Det näst största',100*errlist[1]/delta_nl)



ntabell = 1.000276
#print(E[max_index])
#print('Minimalt n:',nl-delta_nl)

if abs(nl-ntabell) < delta_nl:
      print('JAAA!!')


#print('r, andel av totalt fel:',(100*errlist[3])/delta_nl,'%')