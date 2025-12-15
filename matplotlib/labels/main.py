import matplotlib.pyplot as plt
import numpy as np

x = np.array([2020, 2021, 2022, 2023, 2024, 2025])
y1 = np.array([10, 15, 13, 17, 20, 22])
y2 = np.array([12, 14, 11, 18, 19, 21])
y3 = np.array([11, 16, 14, 15, 22, 23])

line_style = {
    'marker': 'o',
    'markersize': 10,
    'markerfacecolor': '#0722AB',
    'markeredgecolor': '#000000',
    'linestyle': 'solid',
    'linewidth': 3,
}

plt.title("Class Size", fontsize=25,
                        family='Arial',
                        fontweight='bold',
                        color='#FA0BC2')

plt.xlabel("Years", fontsize=20,
                    family='Arial',
                    fontweight='bold',
                    color='#0BE7FA')

plt.ylabel("Students", fontsize=20,
                    family='Arial',
                    fontweight='bold',
                    color='#0BE7FA')

plt.tick_params(axis='both', colors='#0B83FA')

plt.plot(x, y1, color="#FAFE04", **line_style)
plt.plot(x, y2, color="#FE0404", **line_style)
plt.plot(x, y3, color="#3BFE04", **line_style)

plt.xticks(x)

plt.subplots_adjust(left=0.15, bottom=0.15, top=0.9)

plt.show()