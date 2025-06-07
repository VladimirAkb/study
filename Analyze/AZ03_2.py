import numpy as np
import matplotlib.pyplot as plt

random_array1 = np.random.rand(50) # массив из 5 случайных чисел
random_array2 = np.random.rand(50) # массив из 5 случайных чисел

plt.scatter(random_array1, random_array2)

plt.xlabel("Ось х")
plt.ylabel("Ось у")
plt.title("Гистограма №2")

plt.show()
