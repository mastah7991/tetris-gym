"""
Register gym environment
"""

from gym.envs.registration import register
from gym_tetris_simple.env.tetris_gym import TetrisGymOneSeed
from gym_tetris_simple.env.tetris_gym import TetrisGymRandomSeed
from gym_tetris_simple.env.tetris_gym import TetrisGymLimitSeed

from gym_tetris_simple.env.human import Human


register(
    id='tetris-v0',
    entry_point='gym_tetris_simple:TetrisGymOneSeed',
)

register(
    id='tetris-v1',
    entry_point='gym_tetris_simple:TetrisGymRandomSeed',
)

register(
    id='tetris-v2',
    entry_point='gym_tetris_simple:TetrisGymLimitSeed',
)
