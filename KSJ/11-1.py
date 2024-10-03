print('\n11-1.  20203035 김석준 \n')
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
x = [x for x in range(1000)]
y = np.random.randn(1000)
plt.title("Numbers (20203035, Kim seok jun)")
plt.plot(x, y, 'r-', marker='o')

plt.show()
