import matplotlib.pyplot as plt
import numpy as np

members = ("Lourdes", "Paula", "Rocio", "Eva")
penguin_means = {
    'Enero': (18, 18, 14, 12),
    'Febrero': (38, 48, 47, 14),
    'Marzo': (189, 195, 217, 35),
    
}

x = np.arange(len(members))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, members)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 250)

plt.show()
