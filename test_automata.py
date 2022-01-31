"""Test automata module functions."""

import os

import numpy as np

import automata

BASE_PATH = os.path.dirname(__file__)

def test_glider():

    input_test_glider = np.array([[False, False, False, False, False],
                                [False, True, True, True, False],
                                [False, False, False, True, False],
                                [False, False, True, False, False],
                                [False, False, False, False, False]])

    output_test_glider = np.array([[False, False, True, True, True],
                                [False, False, False, False, True],
                                [False, False, False, True, False],
                                [False, False, False, False, False],
                                [False, False, False, False, False]])


    assert (automata.life(input_test_glider, 4) == output_test_glider).all()
    assert (automata.life_periodic(input_test_glider, 4) == output_test_glider).all()

def test_blinker():

    input_test_blinker = np.array([[False, False, False, False, False],
                               [False, False, False, False, False],
                               [False, True, True, True, False],
                               [False, False, False, False, False],
                               [False, False, False, False, False]])

    output_test_blinker = np.array([[False, False, False, False, False],
                                    [False, False, True, False, False],
                                    [False, False, True, False, False],
                                    [False, False, True, False, False],
                                    [False, False, False, False, False]])

    
    assert (automata.life(input_test_blinker, 1) == output_test_blinker).all()
    assert (automata.life_periodic(input_test_blinker, 1) == output_test_blinker).all()