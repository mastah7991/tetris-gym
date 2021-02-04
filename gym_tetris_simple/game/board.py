"""
Simple board with base moves
"""
from typing import Dict

import numpy as np
import gym_tetris_simple.game.constants


class Board:
    """
    Create board with seed
    """

    def __init__(self, height: int = 20, width: int = 10, *, seed: int = 0) -> None:
        """
        Create instance of Board
        :param height: height of the board
        :param width: width of the board
        :param seed: seed to generate game
        """
        self.height: int = height
        self.width: int = width
        self.seed = seed
        self.board: np.ndarray = None
        self.curr: np.ndarray = None
        self.next: int = 0
        self.position: np.ndarray = None

        self.reset()

    def reset(self) -> None:
        """
        Reset current game
         :return: None
        """
        np.random.seed(self.seed)
        self.board = np.zeros((self.height, self.width))
        self.next = np.random.randint(low=0, high=5)
        self._next_block()

    def get_board(self) -> np.ndarray:
        """
        Get the current table with the current block.
        The current block is marked with two.
        :return: numpy.array
        """
        board = self.board.copy()
        shape = self.curr.shape

        x_pos = (self.position[0], self.position[0] + shape[0])
        y_pos = (self.position[1], self.position[1] + shape[1])
        board[x_pos[0]:x_pos[1], y_pos[0]:y_pos[1]] += self.curr * 2

        return board

    def move_down(self) -> Dict[str, int]:
        """
        Make one move down.
        :rtype: map with information about the current state
        """
        new_position = self.position + np.array([1, 0])

        if self._check_collision(new_position, self.curr):
            self.position = new_position
            return {"lines": 0, "reward": 0, "done": False}

        return self._next_round()

    def move_fast_down(self) -> Dict[str, int]:
        """
        Place the current block on the bottom of the board as much as possible
        :rtype: map with information about the current state
        """

        new_position = self.position + np.array([1, 0])

        while self._check_collision(new_position, self.curr):
            self.position = new_position
            new_position = self.position + np.array([1, 0])

        return self._next_round()

    def move_left(self) -> Dict[str, int]:
        """
        Make one left.
        :rtype: map with information about the current state
        """
        new_position = self.position + np.array([0, -1])

        if self._check_collision(new_position, self.curr):
            self.position = new_position

        return {"lines": 0, "reward": 0, "done": False}

    def move_right(self) -> Dict[str, int]:
        """
        Make one right.
        :rtype: map with information about the current state
        """
        new_position = self.position + np.array([0, 1])

        if self._check_collision(new_position, self.curr):
            self.position = new_position

        return {"lines": 0, "reward": 0, "done": False}

    def rotate(self, k: int) -> Dict[str, int]:
        """
        Rotate current block if it is possible. \n
        k = 1 -> right \n
        k = 2 -> left \n
        :param k: rotate 90*k degrees
        :rtype: map with information about the current state
        """
        new_block = np.rot90(self.curr, k)

        if self._check_collision(self.position, new_block):
            self.curr = new_block

        return {"lines": 0, "reward": 0, "done": False}

    def _next_block(self) -> None:
        self.curr = gym_tetris_simple.game.constants.elements[self.next]
        self.next = np.random.randint(low=0, high=5)
        self.position = np.array([0, 4])

    def _next_round(self) -> Dict[str, int]:
        shape = self.curr.shape
        x_pos, y_pos = self.position[0], self.position[1]

        self.board[x_pos: x_pos + shape[0], y_pos: y_pos + shape[1]] += self.curr

        done = False
        lines = self.board.sum(axis=1) == 10

        for i, reward in enumerate(lines):
            if reward:
                self.board[1:i + 1] = self.board[0:i]
                self.board[0] = np.zeros(10)

        self._next_block()

        if not self._check_collision(self.position, self.curr):
            done = True

        return {"lines": lines.sum(), "reward": (lines.sum() ** 2) * 20, "done": done}

    def _check_collision(self, new_pos: np.ndarray, block: np.ndarray) -> bool:
        shape = block.shape

        if new_pos[0] + shape[0] > self.height \
                or new_pos[1] < 0 \
                or new_pos[1] + shape[1] > self.width:
            return False

        board = self.board.copy()
        board[new_pos[0]:new_pos[0] + shape[0], new_pos[1]:new_pos[1] + shape[1]] += block

        collision: int = (board > 1).sum()
        return collision == 0
