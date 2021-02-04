"""
Human class can create base env where player can game.
It is very simple env ;).
"""
from typing import Type, TypeVar

import time

import numpy as np

from gym_tetris_simple.game import constants
from gym_tetris_simple.game.tetris_base import TetrisBase
from gym_tetris_simple.movement.human_movement import HumanMovement

from gym_tetris_simple.movement.movement import Movement

TypeObject = TypeVar('TypeObject', bound='Human')


class Human:
    """
    Create base human env with random seed
    """

    def __init__(self, game: TetrisBase, movement: Movement):
        self.game: TetrisBase = game
        self.movement: Movement = movement

    @classmethod
    def tetris_base(cls: Type[TypeObject]) -> TypeObject:
        """
        Create Human env with base movement and random seed
        :return: Human
        """
        seed: int = np.random.randint(0, constants.MAX_INT)
        return cls(TetrisBase(seed=seed), HumanMovement.base_movement())

    def play(self) -> None:
        """
        Start base game :)
        :return: None
        """
        self.game.reset()

        end_game = False
        info = {'Score': 0, 'Lines': 0}

        while not end_game:

            time_next = 1.0 / (info['Lines'] // 5 + 1) / constants.FPS

            action, end_game = self.movement.next(time_next)

            _, _, done, info = self.game.step(action)
            self.game.render()

            if done:
                break

            if action == constants.NONE:
                time.sleep(0.035)
            else:
                time.sleep(0.07)

        self.game.close()
