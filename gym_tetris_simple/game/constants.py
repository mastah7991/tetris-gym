"""
Constants for base tetris settings
"""
import numpy as np

WIDTH = 10
HEIGHT = 20

NONE = 0
DOWN = 1
LEFT = 2
RIGHT = 3
ROTATE_L = 4
ROTATE_R = 5
DOWN_FAST = 6

ACTIONS = [
    NONE,
    DOWN,
    LEFT,
    RIGHT,
    ROTATE_R,
    ROTATE_L,
    DOWN_FAST
]

AUTO_MOVE = 5
MARGIN = 4

FPS = 30

MAX_INT = 2147483648

colors = [
    (255, 255, 0),
    (0, 255, 0),
    (0, 0, 255)
]

elements = [
    np.array([
        [1, 1],
        [1, 1]
    ]),
    np.array([
        [1, 0],
        [1, 0],
        [1, 1]
    ]),
    np.array([
        [1],
        [1],
        [1],
        [1]
    ]),
    np.array([
        [1, 0],
        [1, 1],
        [1, 0]
    ]),
    np.array([
        [0, 1],
        [1, 1],
        [1, 0]
    ]),
    np.array([
        [1, 0],
        [1, 1],
        [0, 1]
    ])
]
