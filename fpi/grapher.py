"""
grapher - draws plots for solutions.
"""
import matplotlib.pyplot as plt
import numpy as np

def makeplot(x, disp, plot):
    # Data for plotting
    t = np.arange(0, len(x), 1)

    # Note that using plt.subplots below is equivalent to using
    # fig = plt.figure and then ax = fig.add_subplot(111)
    fig, ax = plt.subplots()
    ax.plot(t, x)

    ax.set(xlabel='x coordinate', ylabel='x values',
           title='Solution somparison: Jacobi, Seidel, SOR methods')
    ax.grid()
    plt.show()
