import numpy
import pandas

h1 = numpy.array([0, 0.1, 0.2, 0.2, 0.3, 0.5, 0.8])
h2 = numpy.array([0, 0.4, 0.8, 1.2, 1.8, 2.4, 3.1])



A = (1.015*0.65*10*288*8.31)/(160)
B = (1.015*0.65*20*288*8.31)/(160)

p1 = A/(65 - 10*numpy.pi*0.5625*0.001*h1) # calculating the pressure in first solution
#print(p1*1000)

p2 = B/(65 + 10*numpy.pi*0.5625*0.001*h2) # calculating the pressure in second solution
#print(p2*1000)

C = -6.5

f = C*numpy.abs(((10)/(65 - 10*numpy.pi*0.5625*h1*0.001)) - ((20)/(65 + 10*numpy.pi*0.5625*h2*0.001))) # calculating the osmotic flow
#print(f*1000)

data = pandas.read_csv("./flow.csv")
x = data['t'].to_numpy()
x = x.reshape((7,1))
x = numpy.concatenate([numpy.ones(shape=(7,1)),x], axis=1)

y = data['f'].to_numpy()

w = numpy.linalg.inv(x.T.dot(x)).dot(x.T).dot(y)
print(w)