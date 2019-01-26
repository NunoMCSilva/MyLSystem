# -*- coding: utf-8 -*-

"""lsystem module

This module implements an L-System. See https://en.wikipedia.org/wiki/L-system
for more information.

Classes:
    LSystem -- L-system implementation
"""

from typing import Dict


class LSystem():
    # TODO: add docstring

    def __init__(self, axiom: str, production_rules: Dict[str, str]):
        # TODO: add docstring
        # TODO: verify correctness of production_rules?

        self.system = axiom
        self.production_rules = production_rules

    def step(self) -> None:
        # TODO: add docstring

        def apply_rule(symbol):
            return self.production_rules.get(symbol, symbol)

        self.system = ''.join(list(map(apply_rule, self.system)))
