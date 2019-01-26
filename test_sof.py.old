# -*- coding: utf-8 -*-

import pytest

import sof

# from https://en.wikipedia.org/wiki/L-system#Example_2:_Fractal_(binary)_tree
WIKIP_RECURSION0 = '0'
WIKIP_RECURSION1 = '1[0]0'
WIKIP_RECURSION2 = '11[1[0]0]1[0]0'
WIKIP_RECURSION3 = '1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0'

MINE_RECURSION0 = '0'
MINE_RECURSION1 = '1[0]0'
MINE_RECURSION2 = '1[1[0]0]1[0]0'
MINE_RECURSION3 = '1[1[1[0]0]1[0]0]1[1[0]0]1[0]0'


# TODO: improve this (check pytest docs)
@pytest.mark.parametrize('input_system, output_system, rules', [
    (WIKIP_RECURSION0, WIKIP_RECURSION1, 'wikip'),
    (WIKIP_RECURSION1, WIKIP_RECURSION2, 'wikip'),
    (WIKIP_RECURSION2, WIKIP_RECURSION3, 'wikip'),
    (MINE_RECURSION0, MINE_RECURSION1, 'mine'),
    (MINE_RECURSION1, MINE_RECURSION2, 'mine'),
    (MINE_RECURSION2, MINE_RECURSION3, 'mine'),    
])
def test__apply_rules__returns_correctly(input_system, output_system, rules):
    assert sof._apply_rules(input_system, rules) == output_system
