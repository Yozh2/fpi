"""
grapher - draws plots for solutions.
"""
import matplotlib.pyplot as plt
import numpy as np

# r'$\varepsilon^{k}$'

def makeplot_residuals(residuals=[], x_name='x', y_name='y', mth_name='custom'):
    # Data for plotting

    # Note that using plt.subplots below is equivalent to using
    # fig = plt.figure and then ax = fig.add_subplot(111)
    fig, ax = plt.subplots()
    ax.plot(residuals[:-1], residuals[1:])
    ax.set_xscale('log')
    ax.set_yscale('log')

    ax.set(xlabel=x_name, ylabel=y_name,
           title='Residuals regression: ' + mth_name + ' method')
    ax.grid()
    plt.show()
