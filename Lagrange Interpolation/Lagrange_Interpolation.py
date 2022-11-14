## Lagrange Interpolation
## Created by AAdika45 (aslamic.adika45@gmail.com)

def LI(k,l,m):   ## k = x_i (interpolation point) ; l = y_i ; m = x ; LI(k,l,m) = p(x)
    N = 10       ## input total data (total interpolation points, \sum x_i): N = n+1 = len(x_i)
    f = list()
    p=0
    for i in range(0,N):
        L =1 
        for j in range(0,N):
            if i!=j:
                L *=((m-k[j])/(k[i]-k[j]))
            else:
                pass
        p += L*l[i]
    f.append(p)
    z=np.array(f)
    z = z.T
    return z
