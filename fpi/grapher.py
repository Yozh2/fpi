"""
grapher - draws plots for solutions.
"""
import matplotlib.pyplot as plt
import numpy as np
import random
import os

def get_color():
        """ Returns string like '#xxxxxx' containing randomly generated colour"""
        return "#" + "".join(random.sample("0123456789abcdef", 6))

def makeplot_residuals(residuals=[], x_name='x', y_name='y', mth_name='custom', path='.'):
    # Data for plotting

    # Note that using plt.subplots below is equivalent to using
    # fig = plt.figure and then ax = fig.add_subplot(111)
    fig, ax = plt.subplots()

    # Set axes, figure names
    fig.suptitle('Residuals regression: ' + mth_name + ' method',
                 fontsize=14, fontweight='bold')
    ax.set(xlabel=x_name, ylabel=y_name)
    ax.set_title(os.path.basename(path).split('_')[0])

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.grid()

    ax.plot(residuals[:-1], residuals[1:],
            color=get_color(),
            label='sorelx: {}'.format(len(residuals)))

    plt.legend()
    plt.savefig(os.path.join(path, mth_name + '.png'))
    plt.show()


def makeplots_residuals(r_jacobi=[], r_seidel=[], r_sor=[], x_name='x', y_name='y', path='.'):
    # Data for plotting

    # Note that using plt.subplots below is equivalent to using
    # fig = plt.figure and then ax = fig.add_subplot(111)
    fig, ax = plt.subplots()

    # Set axes, figure names
    fig.suptitle('Residuals regression: all methods',
                 fontsize=14, fontweight='bold')
    ax.set(xlabel=x_name, ylabel=y_name)
    ax.set_title(os.path.basename(path).split('_')[0])

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.grid()

    ax.plot(r_jacobi[:-1], r_jacobi[1:],
            color='blue',
            label='jacobi: {}'.format(len(r_jacobi)))
    ax.plot(r_seidel[:-1], r_seidel[1:],
            color='green',
            label='seidel: {}'.format(len(r_seidel)))
    ax.plot(r_sor[:-1], r_sor[1:],
            color='red',
            label='sorelx: {}'.format(len(r_sor)))

    # Setup plot legend
    plt.legend()
    plt.savefig(os.path.join(path, 'all.png'))
    plt.show()
