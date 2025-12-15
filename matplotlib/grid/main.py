import matplotlib.pyplot as plt
import numpy as np

x = np.array([2020, 2021, 2022, 2023, 2024, 2025])
y = np.array([10, 15, 13, 17, 20, 22])

plt.grid(axis='both',
         color='#969698',
         linestyle='dashed',
         linewidth=2)

plt.plot(x, y)
plt.show()