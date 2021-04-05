import numpy as np
import matplotlib.pyplot as plt

SAMPLES = 3

mu = 3.5
sigma2 = (6^2 - 1) / 12
clt = []
for i in range(1000):  # number of points we want to plot in normal
    three_d6 = np.array([np.random.randint(1, 7) for _ in range(SAMPLES)])
    clt.append((np.sum(three_d6) - mu * SAMPLES) / np.sqrt(sigma2 * SAMPLES))

plt.hist(clt)
plt.show()
