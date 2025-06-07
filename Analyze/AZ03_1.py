import numpy as np
import matplotlib.pyplot as plt

mean = 0 # Среднее значение
std_dev = 1 # Стандартное отклонение
num_samples = 1000 # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

plt.hist(data, bins=16)
plt.xlabel("Ось х")
plt.ylabel("Ось у")
plt.title("Гистограма №1")

plt.show()



