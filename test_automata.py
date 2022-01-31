"""Test automata module functions."""

import os

import numpy as np

import automata

BASE_PATH = os.path.dirname(__file__)


def test_lorenz96():
    """Test Lorenz 96 implementation"""
    initial64 = np.load(os.sep.join((BASE_PATH,
                                     'lorenz96_64_init.npy')))

    onestep64 = np.load(os.sep.join((BASE_PATH,
                                     'lorenz96_64_onestep.npy')))

    
    print(initial64, "inital64")
    print(onestep64, "onestep64")
    
    assert np.isclose(automata.lorenz96(initial64, 1), onestep64).all()

    thirtystep64 = np.load(os.sep.join((BASE_PATH,
                                         'lorenz96_64_thirtystep.npy')))
    assert np.isclose(automata.lorenz96(initial64, 30), thirtystep64).all()

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