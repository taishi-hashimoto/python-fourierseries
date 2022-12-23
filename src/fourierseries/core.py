"Fourier series expansion."
from math import cos, sin
from typing import Callable, Tuple, List
import numpy as np
from typing import Callable, Tuple, List
from scipy.integrate import quad


def expand(
    f: Callable[[np.ndarray], np.ndarray],
    T: float,
    n: int
) -> Tuple[List[float], List[float]]:
    """Compute the coefficients of the Fourier series of a periodic function f.

    Parameters
    ----------
    f: Function (t) -> y
        Periodic function.
    T: float
        Period.
    n: int
        The number of terms used.

    Returns
    -------
    a: List of float
        Coefficients of cosine terms with a length of `n + 1`.
        `a[0]` is the 0-th harmonic (DC).
    b: List of float
        Coefficients of sine terms with a length of `n + 1`.
        `b[0]` is always `nan`.
    """
    def fc(x, f, k, omega): return f(x) * cos(k*omega*x)
    def fs(x, f, k, omega): return f(x) * sin(k*omega*x)
    omega = 2*np.pi/T
    a = [1/T * quad(f, -T/2, T/2)[0] * 2 / T]
    b = [np.nan]
    for i in range(n):
        a.append(2/T * quad(fc, -T/2, T/2, args=(f, i+1, omega))[0])
        b.append(2/T * quad(fs, -T/2, T/2, args=(f, i+1, omega))[0])
    return a, b


def evaluate(
    x: np.ndarray,
    T: float,
    a: List[float],
    b: List[float]
) -> np.ndarray:
    """Evaluate the fourier series expansion.
    
    Parameters
    ----------
    x: array of float
        Points at where the Fourier series are evaluated.
    T: float
        Period.
    a: list of float
        Fourier coefficients of cosine term.
    b: list of float
        Fourier coefficients of sine term.

    Returns
    -------
    y: np.ndarray
        Evaluation of the fourier series.
    """
    x = np.array(x)
    omega = 2*np.pi/T
    n = len(a)
    y = np.full_like(x, a[0] / 2, dtype=float)
    for i in range(1, n):
        y += a[i] * np.cos(i*omega*x) + b[i] * np.sin(i*omega*x)
    return y