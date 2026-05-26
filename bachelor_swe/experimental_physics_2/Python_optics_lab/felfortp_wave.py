from numpy import * 
#Parameters; errors:

k = 3.16e6      ;dk = 0.0354e6

E = ['k']

#Expression for lambda:
lambda_ = 2/k
err = [dk]

#Partial derivatives:
part_der = [-2/k**2]

delta_lambda = 0; errlist=[]
for i in range(len(err)):
      delta_lambda += abs(part_der[i])*err[i]
      errlist.append(abs(part_der[i])*err[i])
marg = delta_lambda/lambda_
print('Lambda =',lambda_*10**9,'nm','±',delta_lambda*10**9,'nm') #Printing error margin 
print('Felmarginal',100*marg,'%')

max_index = errlist.index(max(errlist)) #Find the index of the max error. 
print(E[max_index])
#print('W, andel av totalt fel:',(100*errlist[max_index])/deltaT,'%') 
#print('r, andel av totalt fel:',(100*errlist[3])/deltaT,'%')