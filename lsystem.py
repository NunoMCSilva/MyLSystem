# -*- coding: utf-8 -*-

"""lsystem module

This module implements an L-System. See https://en.wikipedia.org/wiki/L-system
for more information.
"""

from typing import Dict


class LSystem():
    # TODO: add docstring

    def __init__(self, axiom: str, production_rules: Dict[str, str]):
        # TODO: add docstring
        # TODO: verify correctness of axiom and production_rules?

        self.system = axiom
        self.production_rules = production_rules

    def step(self) -> None:
        # TODO: add docstring
        # TODO: raises error...

        def apply_rule(symbol):
            return self.production_rules[symbol]

        self.system = ''.join(list(map(apply_rule, self.system)))

    # TODO: remove this
    """
    def __iter__(self):
        return self

    def __next__(self):
        system = self.system
        self._step()
        return system
    """
