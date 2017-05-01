import numpy as np
import matplotlib.pyplot as plt
#input data
data=np.random.randn(10)
#histogram
v,b=np.histogram(data,bins=50)
#cumulative sum
cum=np.cumsum(v)
print(data)
print(cum)
print(b)
plt.hist(data,bins=50)
plt.plot(b[:-1],cum,c='r')
plt.show()
