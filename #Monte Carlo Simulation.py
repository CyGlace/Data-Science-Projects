import numpy as np
import matplotlib.pyplot as plt


sim = 100000

A = np.random.uniform(1,5, sim)
B = np.random.uniform(2,6, sim)

duration = A + B

plt.figure(figsize= (3, 3.15))
plt.hist(duration, density = True)
plt.axvline(9, color = 'r')
plt.show()
print((duration > 9).sum()/sim)