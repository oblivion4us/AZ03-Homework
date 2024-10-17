import numpy as np
import matplotlib.pyplot as plt

mean = 0
std_dev = 1
num_samples = 1000

data = np.random.normal(loc=mean, scale=std_dev, size=num_samples)

plt.hist(data, bins=20)
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.title("Гистограмма 1")
plt.show()