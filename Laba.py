import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 5, 51)
y = 10 * np.cos(x ** 2) / x ** 2

plt.plot(x, y, label='10 * cos(x^2)/x^2', color='red', linewidth=5)

plt.title('My schedule', fontsize=15)
plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('y', fontsize=12, color='blue')
plt.grid(True)

plt.show()
