import pptx
import numpy as np
from fourierseries import expand, square_wave

from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import japanize_matplotlib

N = 50
T = 1
dt = 0.0001
margin = 0.1
x = np.arange(-T*(1+margin), T*(1+margin), dt)
func = square_wave

y0 = func(x, T)

n = list(range(1, N+1))
a, b = expand(interp1d(x, y0), T, N)
print(a)
print(b)

fig, axes = plt.subplots(1, 2, figsize=(8, 3), sharex=True, sharey=True)
x = np.arange(N+1)
axes[0].stem(x, a, label="$a_k$", markerfmt=".")
axes[0].set_title("$a_k$")
axes[0].set_xlabel("$k$")
axes[1].stem(x+0.1, b, label="$b_k$", markerfmt=".")
axes[1].set_title("$b_k$")
axes[1].set_xlabel("$k$")
fig.tight_layout()
plt.savefig("coefficients.png")
plt.show()