"""
Module to create base tetris with seed
"""
from typing import Tuple, Dict, Any

import numpy as np

from gym_tetris_simple.game import constants
from gym_tetris_simple.game.gui import Gui
from gym_tetris_simple.game.board import Board


class TetrisBase:
    """
    Class to create base tetris
    """

    def __init__(self, *, seed: int = 0) -> None:
        """
        Create instance of TetrisBase
        :param seed: seed to create object

        """
        self.board: Board = Board(constants.HEIGHT, constants.WIDTH, seed=seed)
        self.gui: Any = None
        self.last_down: int = 0

        self.glob_info: Dict[str, int] = {'Score': 0, 'Lines': 0}

    def step(self, action: int) -> Tuple[np.ndarray, int, bool, Dict[str, int]]:
        """
        Make move in game
        :param action:
        :return: board, reward, done, info
        """
        info = {}

        self.last_down += 1

        if action == constants.LEFT:
            info = self.board.move_left()
        elif action == constants.RIGHT:
            info = self.board.move_right()
        elif action == constants.DOWN_FAST:
            info = self.board.move_fast_down()
            self.last_down = 0
        elif action == constants.DOWN:
            info = self.board.move_down()
            self.last_down = 0
        elif action == constants.ROTATE_L:
            info = self.board.rotate(1)
        elif action == constants.ROTATE_R:
            info = self.board.rotate(3)

        if self.last_down >= constants.AUTO_MOVE:
            self.last_down = 0
            info = self.board.move_down()

        reward, done, info_tetris = self._get_info(info)

        return self.board.get_board(), reward, done, info_tetris

    def reset(self) -> np.ndarray:
        """
        This method is for reset board

        :rtype: np.ndarray
        """
        self.last_down = 0
        self.glob_info = {'Score': 0, 'Lines': 0}
        self.board.reset()
        return self.board.get_board()

    def render(self) -> None:
        """
        This method is used to render the next game frame
        Uses pygame!
        :rtype: None
        """
        if not self.gui:
            self.gui = Gui(constants.HEIGHT, constants.WIDTH)

        self.gui.render(self.board.get_board(), self.glob_info)

    def _get_info(self, info: Dict[str, int]) -> Tuple[int, bool, Dict[str, int]]:
        reward: int = 0
        done: bool = False
        lines: int = 0

        if 'done' in info:
            done = bool(info['done'])

        if 'reward' in info:
            reward = info['reward']
            self.glob_info['Score'] += reward

        if 'lines' in info:
            lines = info['lines']
            self.glob_info['Lines'] += lines

        self.glob_info['Next'] = self.board.next
        self.glob_info['NewLine'] = lines > 0

        return reward, done, self.glob_info

    def close(self) -> None:
        """
        This method is intended for a closed desktop environment
        Uses pygame!
        :rtype: None
        """
        self.gui.close()
        self.gui = None
