import gym
import numpy as np

from Game import Consts
from Game.TetrisBase import TetrisBase


class TetrisGymOneSeed(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.game = TetrisBase()

    def step(self, action):
        return self.game.step(action)

    def reset(self):
        return self.game.reset()

    def render(self, mode='human'):
        self.game.render()

    def close(self):
        self.game.close()


class TetrisGymRandomSeed(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        seed = np.random.randint(0, Consts.MAX_INT)
        self.game = TetrisBase(seed=seed)

    def step(self, action):
        return self.game.step(action)

    def reset(self):
        return self.game.reset()

    def render(self, mode='human'):
        self.game.render()

    def close(self):
        self.game.close()


class TetrisGymLimitSeed(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        seed = np.random.randint(0, 1000)
        self.game = TetrisBase(seed=seed)

    def step(self, action):
        return self.game.step(action)

    def reset(self):
        return self.game.reset()

    def render(self, mode='human'):
        self.game.render()

    def close(self):
        self.game.close()
