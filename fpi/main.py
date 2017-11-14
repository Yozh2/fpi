#!/usr/local/bin/python3
"""
fpi - Fixed Point Iteration methods comparison.
"""

# basic imports
import os
from sys import argv
import argparse
import logging
import numpy as np

# import local modules
from jacobi import jacobi
from seidel import seidel
from sor import sor
import matreader
def save_solution(func, eps, x, error, residuals, path):
    name = ''.join(os.path.basename(path).split('.')[:-1])

    testdir_path = os.path.join(os.getcwd(), name + '_solutions')
    if not os.path.exists(testdir_path):
        os.makedirs(name=testdir_path, exist_ok=True)

    x_path = os.path.join(testdir_path, func.__name__+'.x.smtx')
    err_path = os.path.join(testdir_path, func.__name__+'.err.smtx')
    res_path = os.path.join(testdir_path, func.__name__+'.res.smtx')

    np.savetxt(x_path, x, fmt='%.10e', delimiter=' ', newline='\n')
    np.savetxt(err_path, error, fmt='%.10e', delimiter=' ', newline='\n')
    np.savetxt(res_path, residuals, fmt='%.10e', delimiter=' ', newline='\n')

def print_solution(func, A, b, eps, to_files=False, path=None):
    print(func.__name__,'computing started...')
    x, iterations, residuals = func(A, b, eps)
    print(func.__name__, 'completed:', iterations, 'iterations')
    # print(x)

    # print(func.__name__, 'error:')
    error = np.dot(A, x) - b
    # print(error)

    # print(func.__name__, 'residuals:')
    # print(residuals, sep='\n')

    if to_files:
        save_solution(func, eps, x, error, residuals, path)

    return x, residuals

def compare(mth1, mth2, x1, x2):
    print(mth1, '-', mth2, ':')
    print(x1-x2)

def build_graph_from(path=None):
    import grapher
    r_v = matreader.read_vector(path)
    r_v_name = os.path.basename(path).split('.')[0]
    grapher.makeplot_residuals(r_v, r'$\varepsilon^k$', r'$\varepsilon^{k+1}$', r_v_name)


if __name__ == '__main__':

    def parse_args():
        """ Parses arguments and returns args object to the main program"""
        parser = argparse.ArgumentParser()
        parser.add_argument("OPT", type=str, nargs='?', default='all',
                            help="'jacobi', 'seidel' or 'sor' computation only")
        parser.add_argument("PATH", type=str,
                            help="The PATH to the matrix we want work to.")
        parser.add_argument("EPS", type=float, nargs='?', default=10e-10,
                            help="epsilon, the discrepancy from the precise solution.")
        parser.add_argument('-s', "--savefiles", action='store_true',
                            help="Save computation results to .smtx files.")
        parser.add_argument('-g', "--grapher", action='store_true',
                            help="Read .smtx vector from PATH and make plot.")
        return parser.parse_args()


    # Enable logging
    LOG = u'{}.log'.format(argv[0])
    logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] \
    %(message)s', level=logging.DEBUG, filename=LOG)

    # parse arguments
    ARGS = parse_args()
    PATH = ARGS.PATH
    OPT = ARGS.OPT
    EPS = ARGS.EPS
    SF = ARGS.savefiles
    GR = ARGS.grapher

    if GR:
        build_graph_from(PATH)

    else:
        # Ax = b
        # Read A, b
        A, b = matreader.read(PATH)
        if OPT == 'all':
            x_jacobi, r_jacobi = print_solution(jacobi, A, b, EPS, SF, PATH)
            x_seidel, r_seidel = print_solution(seidel, A, b, EPS, SF, PATH)
            x_sor, r_sor = print_solution(sor, A, b, EPS, SF, PATH)

            compare('jacobi', 'seidel', x_jacobi, x_seidel)
            compare('jacobi', 'sor', x_jacobi, x_sor)
            compare('sor', 'seidel', x_sor, x_seidel)

        elif OPT == 'jacobi':
            x = print_solution(jacobi, A, b, EPS, SF, PATH)
        elif OPT == 'sor':
            x = print_solution(sor, A, b, EPS, SF, PATH)
        elif OPT == 'seidel':
            x = print_solution(seidel, A, b, EPS, SF, PATH)
