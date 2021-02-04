"""
Create all gym environments
"""
from typing import Tuple, Dict

import gym
import numpy as np

from gym_tetris_simple.game import constants
from gym_tetris_simple.game.tetris_base import TetrisBase


class TetrisGymOneSeed(gym.Env):
    """
    Create gym env with seed '0'
    """
    metadata = {'render.modes': ['human']}

    def __init__(self) -> None:
        self.game: TetrisBase = TetrisBase()

    def step(self, action: int) -> Tuple[np.ndarray, int, bool, Dict[str, int]]:
        return self.game.step(action)

    def reset(self) -> np.ndarray:
        return self.game.reset()

    def render(self, mode: str = 'human') -> None:
        self.game.render()

    def close(self) -> None:
        self.game.close()


class TetrisGymRandomSeed(gym.Env):
    """
    Create gym env with random seed
    """
    metadata = {'render.modes': ['human']}

    def __init__(self) -> None:
        seed = np.random.randint(0, constants.MAX_INT)
        self.game: TetrisBase = TetrisBase(seed=seed)

    def step(self, action: int) -> Tuple[np.ndarray, int, bool, Dict[str, int]]:
        return self.game.step(action)

    def reset(self) -> np.ndarray:
        return self.game.reset()

    def render(self, mode: str = 'human') -> None:
        self.game.render()

    def close(self) -> None:
        self.game.close()


class TetrisGymLimitSeed(gym.Env):
    """
    Create gym env with limited seed [0,100]
     """
    metadata = {'render.modes': ['human']}

    def __init__(self) -> None:
        seed = np.random.randint(0, 1000)
        self.game: TetrisBase = TetrisBase(seed=seed)

    def step(self, action: int) -> Tuple[np.ndarray, int, bool, Dict[str, int]]:
        return self.game.step(action)

    def reset(self) -> np.ndarray:
        return self.game.reset()

    def render(self, mode: str = 'human') -> None:
        self.game.render()

    def close(self) -> None:
        self.game.close()
