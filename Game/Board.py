import numpy as np
from Game.Consts import elements


class Board(object):
    def __init__(self, height=20, width=10, *, seed=0):
        self.height = height
        self.width = width

        np.random.seed(seed)
        self.board = None
        self.curr = None
        self.next = None
        self.position = None

        self.reset()

    def reset(self):
        self.board = np.zeros((self.height, self.width))
        self.next = np.random.randint(low=0, high=5)
        self.next_block()

    def next_block(self) -> None:
        self.curr = elements[self.next]
        self.next = np.random.randint(low=0, high=5)
        self.position = np.array([0, 4])

    def get_board(self):
        board = self.board.copy()
        shape = self.curr.shape

        board[self.position[0]:self.position[0] + shape[0], self.position[1]:self.position[1] + shape[1]] += self.curr*2

        return board

    def move_down(self):
        new_position = self.position + np.array([1, 0])

        if self._check_collision(new_position, self.curr):
            self.position = new_position
            return {"lines": 0, "reward": 0, "done": False}

        return self._next_round()

    def move_fast_down(self):
        new_position = self.position + np.array([1, 0])

        while self._check_collision(new_position, self.curr):
            self.position = new_position
            new_position = self.position + np.array([1, 0])

        return self._next_round()

    def move_left(self):
        new_position = self.position + np.array([0, -1])

        if self._check_collision(new_position, self.curr):
            self.position = new_position

        return {"lines": 0, "reward": 0, "done": False}

    def move_right(self):
        new_position = self.position + np.array([0, 1])

        if self._check_collision(new_position, self.curr):
            self.position = new_position

        return {"lines": 0, "reward": 0, "done": False}

    def rotate(self, k):

        new_block = np.rot90(self.curr, k)

        if self._check_collision(self.position, new_block):
            self.curr = new_block

        return {"lines": 0, "reward": 0, "done": False}

    def _next_round(self):
        shape = self.curr.shape
        x, y = self.position[0], self.position[1]

        self.board[x: x + shape[0], y: y + shape[1]] += self.curr

        done = False
        lines = self.board.sum(axis=1) == 10

        for i, r in enumerate(lines):
            if r:
                self.board[1:i + 1] = self.board[0:i]
                self.board[0] = np.zeros(10)

        self.next_block()

        if not self._check_collision(self.position, self.curr):
            done = True

        return {"lines": lines.sum(), "reward": (lines.sum() ** 2) * 20, "done": done}

    def _check_collision(self, new_pos, block):
        if new_pos[0] >= self.height or new_pos[1] < 0 or new_pos[1] >= self.width:
            return False

        shape = block.shape
        board = self.board.copy()

        try:
            board[new_pos[0]:new_pos[0] + shape[0], new_pos[1]:new_pos[1] + shape[1]] += block
            return (board > 1).sum() == 0
        except:
            return False
