#N = 12
xm = [
    0.981560634246719,-0.981560634246719,0.904117256370475,-0.904117256370475,
    0.769902674194305,-0.769902674194305,0.587317954286617,-0.587317954286617,
    0.367831498998180,-0.367831498998180,0.125233408511169,-0.125233408511169
]
wm = [
    0.047175336386512, 0.047175336386512,0.106939325995318, 0.106939325995318,
    0.160078328543346, 0.160078328543346,0.203167426723066, 0.203167426723066,
    0.233492536538355, 0.233492536538355,0.249147045813403, 0.249147045813403
]
g = lambda x: mth.sin(x**2) #fungsi
a = 0 #masukkan batas bawah integral
b = 3 #masukkan batas atas integral
k = (b-a)/2
l = (b+a)/2
hasil = 0
for i in range(0,len(xm)):
    integral = wm[i]*(k*g(k*xm[i]+l))
    hasil +=integral
hasil
