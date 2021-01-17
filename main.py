from gym.envs.registration import register

register(
    id='tetris-v0',
    entry_point='Env:TetrisGymOneSeed',
)

register(
    id='tetris-v1',
    entry_point='Env:TetrisGymRandomSeed',
)

register(
    id='tetris-v2',
    entry_point='Env:TetrisGymLimitSeed',
)
