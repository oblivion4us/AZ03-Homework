import numpy as np
import matplotlib.pyplot as plt

random_array1 = np.random.rand(5)
print(random_array1)
random_array2 = np.random.rand(5)
print(random_array2)

plt.scatter(random_array1, random_array2)

plt.xlabel("Ось Х")
plt.ylabel("Ось Y")
plt.title("Тестовая диаграмма рассеяния")

plt.show()