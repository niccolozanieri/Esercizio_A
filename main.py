import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x = np.linspace(1, 90, 10)
y = np.ones(10) * 2
ax.plot(x, y, label="Hostia")
plt.show()