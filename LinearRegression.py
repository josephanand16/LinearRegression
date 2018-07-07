import os
import numpy
import math
import statistics
import matplotlib.pyplot as plt

land_price = [50,69,80,30,15,150,250]
sqft100 = [19,22,28,12,6,30,50]
Xmean = numpy.mean(land_price)
Ymean = numpy.mean(sqft100)

n = len(X)

varX = statistics.variance(land_price-Xmean)
covXY = numpy.cov(land_price,sqft100)[0][1]

slope = covXY/varX
intercept = Ymean - slope*Xmean

print("The equation of the line is: y = %fx + %f" % (slope,intercept) )

def graph(formula, x_range):  
    x = numpy.array(x_range)  
    y = eval(formula)
    plt.plot(x, y)  
    plt.show()

plt.plot(X, Y, 'ro')
plt.xlabel("100Square_ft")
plt.ylabel("land_price in lakhs")
plt.axis([0, 300, 0, 150])
graph("%f*x + %f" % (slope,intercept), range(0, 300))
plt.show()
