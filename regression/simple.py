import matplotlib.pyplot as plt
import numpy as np

N = 10
x = np.arange(N)
y = 1 + 0.5 * x
y_noised = y + np.random.normal(size=N)

sum_x = np.sum(x)
sum_y = np.sum(y_noised)
sum_xy = np.sum(x * y_noised)
sum_x_squared = np.sum(x**2)

a = (sum_x_squared * sum_y - sum_x * sum_xy) / (N * sum_x_squared - sum_x**2)
b = (N * sum_xy - sum_x * sum_y) / (N * sum_x_squared - sum_x**2)
y_pred = a + b * x

plt.plot(x, y, label='true func')
plt.plot(x, y_pred, label='prediction')
plt.plot(x, y_noised, 'ro', label='data')
plt.legend()
plt.show()
