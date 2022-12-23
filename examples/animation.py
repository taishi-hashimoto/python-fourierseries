import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from scipy.interpolate import interp1d
from fourierseries import (
    expand, evaluate, square_wave
)


n = [1, 3, 5, 10, 20, 50]

T = 1
dt = 0.0001
margin = 0.1
x = np.arange(-T*(1+margin), T*(1+margin), dt)

func = square_wave

y0 = func(x, T)


ab = [expand(interp1d(x, y0), T, i) for i in n]
yy = [evaluate(x, T, a, b) for a, b in ab]


fig, ax = plt.subplots(1, 1, figsize=(8, 3))
ax.set_ylim(-2, 2)
ax.plot(x, y0)
ax.set_title("k=0")
line, = ax.plot(x, y0)
ax.set_xticks([])
ax.set_yticks([])
fig.tight_layout()

def update(i):
    line.set_data([x, yy[i]])
    ax.set_title(f"$n = {n[i]}$")

ani = anim.FuncAnimation(fig, update, len(n), interval=1000, repeat=True)
shape = "square" if func == square_wave else "tri"
ani.save(f"fourier_{shape}.gif", anim.PillowWriter(fps=1))


plt.show()
    