# -*- coding: utf-8 -*-

import pytest

from lsystem import LSystem


# TODO: load tests from json?
@pytest.mark.parametrize('axiom, production_rules, expected_recursions', [
    # https://en.wikipedia.org/wiki/L-system#Example_1:_Algae
    ('A', {'A': 'AB', 'B': 'A'},
     ['A', 'AB', 'ABA', 'ABAAB', 'ABAABABA', 'ABAABABAABAAB',
      'ABAABABAABAABABAABABA', 'ABAABABAABAABABAABABAABAABABAABAAB']),
    # https://en.wikipedia.org/wiki/L-system#Example_2:_Fractal_(binary)_tree
    ('0', {'1': '11', '0': '1[0]0'},
     ['0', '1[0]0', '11[1[0]0]1[0]0', '1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0']),
    # https://en.wikipedia.org/wiki/L-system#Example_4:_Koch_curve
    ('F', {'F': 'F+F−F−F+F'},
     ['F', 'F+F−F−F+F', 'F+F−F−F+F+F+F−F−F+F−F+F−F−F+F−F+F−F−F+F+F+F−F−F+F']),
])
def test__lsystem_step__works_as_expected__on_normal_input(
        axiom, production_rules, expected_recursions):

    # arrange
    ls = LSystem(axiom, production_rules)

    # act
    recursions = []
    for _ in range(len(expected_recursions)):
        recursions.append(ls.system)
        ls.step()

    # assert
    assert recursions == expected_recursions
