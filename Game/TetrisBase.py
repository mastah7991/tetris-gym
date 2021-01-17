from datetime import time

import numpy as np

from Game import Consts
from Game.GUI import GUI
from Game.Board import Board


class TetrisBase(object):
    def __init__(self, *, seed=0):
        self.board = Board(Consts.HEIGHT, Consts.WIDTH, seed=seed)
        self.GUI = GUI(Consts.HEIGHT, Consts.WIDTH)
        self.last_down = 0

        self.glob_info = {'Score': 0, 'Lines': 0}

    def step(self, action):
        info = {}

        self.last_down += 1

        if action == Consts.LEFT:
            info = self.board.move_left()
        elif action == Consts.RIGHT:
            info = self.board.move_right()
        elif action == Consts.DOWN_FAST:
            info = self.board.move_fast_down()
            self.last_down = 0
        elif action == Consts.DOWN:
            info = self.board.move_down()
            self.last_down = 0
        elif action == Consts.ROTATE_L:
            info = self.board.rotate(1)
        elif action == Consts.ROTATE_R:
            info = self.board.rotate(3)

        if self.last_down >= Consts.AUTO_MOVE:
            self.last_down = 0
            info = self.board.move_down()

        reward, done, info_tetris = self._get_info(info)

        return self.board.board, reward, done, info_tetris

    def reset(self):
        self.board.reset()
        return self.board.get_board()

    def render(self):
        self.GUI.render(self.board.get_board(), self.glob_info)

    def _get_info(self, info):
        reward = 0
        done = False
        lines = 0

        if 'done' in info:
            done = info['done']

        if 'reward' in info:
            reward = info['reward']
            self.glob_info['Score'] += reward

        if 'lines' in info:
            lines = info['lines']
            self.glob_info['Lines'] += lines

        self.glob_info['Next'] = self.board.next
        self.glob_info['NewLine'] = lines > 0

        return reward, done, self.glob_info

    def close(self):
        self.GUI.close()
