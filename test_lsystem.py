# -*- coding: utf-8 -*-

import pytest

from lsystem import *


def test__lsystem_step__works_as_expected__on_normal_input():
    # arrange
    ls = LSystem(axiom='A', production_rules={'A': 'AB', 'B': 'A'})

    # act
    recursions = [ls.system]
    for _ in range(7):
        ls.step()
        recursions.append(ls.system)

    # TODO: remove this bit
    #recursions = [recursion for recursion in itertools.islice(ls, 8)]

    # assert
    assert recursions == ['A', 'AB', 'ABA', 'ABAAB', 'ABAABABA', 'ABAABABAABAAB', 'ABAABABAABAABABAABABA', 'ABAABABAABAABABAABABAABAABABAABAAB']


def test__lsystem_step__raises_error__on_unknown_symbol():
    # arrange
    ls = LSystem(axiom='x', production_rules={'A': 'AB', 'B': 'A'})

    # act & assert
    with pytest.raises(KeyError):   # TODO: use another exception?
        ls.step()
