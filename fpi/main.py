#!/usr/local/bin/python3
"""
fpi - Fixed Point Iteration methods comparison.
"""

# basic imports
from sys import argv
import argparse
import logging

# import local modules
import jacobi
import seidel
import sor
import matreader

if __name__ == '__main__':

    def parse_args():
        """ Parses arguments and returns args object to the main program"""
        parser = argparse.ArgumentParser()
        parser.add_argument("PATH", type=str,
                            help="The PATH to the matrix we want work to.")
        return parser.parse_args()


    # Enable logging
    LOG = u'{}.log'.format(argv[0])
    logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] \
    %(message)s', level=logging.DEBUG, filename=LOG)


    ARGS = parse_args()
    PATH = ARGS.PATH


# Ax = b
A = matreader.read(PATH)
