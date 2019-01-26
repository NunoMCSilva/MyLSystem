#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Sort of Fractal

Actually a L-system I've been obssessing with since my middle school days.
"""

# quick and dirty implementation

import turtle


def draw(system, length=20):
    # TODO: add docstring -- may raise ValueError or IndexError -- .pop()

    #turtle.clear()
    #turtle.penup()
    #turtle.home()
    #turtle.pendown()
    turtle.reset()
    turtle.hideturtle()
    turtle.left(90)

    stack = []
    for symbol in system:
        #print('symbol', symbol)
        #print('before pos angle', turtle.pos(), turtle.heading())
        if symbol == '0':
            # option 1
            #turtle.forward(length)
            #turtle.dot(3)

            # option 2
            turtle.pencolor('red')
            turtle.forward(length)
            turtle.pencolor('black')
        elif symbol == 'x':
            # my rule: blocked 0 (no longer a 0) -- later info
            turtle.forward(length)
        elif symbol == '1':
            turtle.forward(length)
        elif symbol == '[':
            stack.append((*turtle.pos(), turtle.heading()))
            turtle.left(45)
        elif symbol == ']':
            x, y, angle = stack.pop()  # can raise IndexError
            turtle.penup()
            turtle.setposition(x, y)
            turtle.pendown()
            turtle.setheading(angle)
            turtle.right(45)
        else:
            raise ValueError("symbol {} isn't valid".format(symbol))
        #print('after pos angle', turtle.pos(), turtle.heading())
        #print('stack', stack)
        #input()

    turtle.hideturtle()
    print()


def _step(system):
    # TODO: add docstring

    print('System: {}'.format(system))
    draw(system)
    system = _apply_rules(system, rules='mine')
    #input('Press ENTER to continue')    # TODO: not necessary for last loop

    return system


def _apply_wikip_rule(symbol):
    # TODO: add docstring

    if symbol == '0':
        return '1[0]0'
    elif symbol == '1':
        return '11'
    elif symbol == '[':
        return '['
    elif symbol == ']':
        return ']'
    else:
        raise ValueError("symbol {} isn't valid".format(symbol))


def _apply_my_rule(symbol):
    # TODO: add docstring

    if symbol == '0':
        return '1[0]0'
    elif symbol == '1':
        return '1'
    elif symbol == '[':
        return '['
    elif symbol == ']':
        return ']'
    else:
        raise ValueError("symbol {} isn't valid".format(symbol))


def _apply_my_rule2(symbol):
    # TODO: add docstring

    return symbol if symbol == 'x' else _apply_my_rule(symbol)


def _apply_rules(system, rules='wikip'):
    # TODO: add docstring

    if rules == 'wikip':
        return ''.join(list(map(_apply_wikip_rule, system)))
    elif rules == 'mine':
        return ''.join(list(map(_apply_my_rule, system)))
    elif rules == 'mine2':
        return ''.join(list(map(_apply_my_rule2, system)))
    else:
        raise ValueError('unknown rules')


def run(axiom='0', n=None):
    # TODO: add docstring

    # TODO: improve this bit of code
    system = axiom
    if n is None:
        while True:
            system = _step(system)
    else:
        for _ in range(n):
            system = _step(system)


if __name__ == '__main__':
    turtle.setup(width=400, height=400, startx=0, starty=0)
    turtle.speed(0) # fastest, no animation
    turtle.delay(0)
    turtle.tracer(0)

    #run(n=5)

    # example of collision detection (by hand) -- hmmm, collision detection during...

    system = '1[1[1[0]0]1[0]x]1[1[x]0]1[0]0'
    #draw(system, length=20)
    system = _apply_rules(system, rules='mine2')
    draw(system, length=20)

    # TODO: add save to image, re-implement turtle so it doesn't need to go to screen
    screen = turtle.getscreen()
    screen.getcanvas().postscript(file='test.eps')
    # thanks https://github.com/kvoss/lsystem/blob/master/example-plant.py for this instruction
    # https://pypi.org/project/lsystems/

    # TODO: can use Tkinter Canvas to get exists of a point for collision test?
