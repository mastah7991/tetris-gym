import time

import keyboard
import numpy as np

from Game import Consts
from Game.TetrisBase import TetrisBase


class Human(object):
    def __init__(self):
        seed = np.random.randint(0, Consts.MAX_INT)
        self.game = TetrisBase(seed=seed)

    def play(self):
        self.game.reset()

        end_game = False
        info = {'Score': 0, 'Lines': 0}
        pressed = {'w': False, ' ': False}

        while not end_game:
            action = Consts.NONE

            time_next = 1.0 / (info['Lines'] // 5 + 1) / Consts.FPS

            for i in range(Consts.FPS):

                if keyboard.is_pressed('esc'):
                    end_game = True
                    print("END")
                    break

                if keyboard.is_pressed('a'):
                    action = Consts.LEFT
                elif keyboard.is_pressed('d'):
                    action = Consts.RIGHT
                elif keyboard.is_pressed('s'):
                    action = Consts.DOWN
                elif keyboard.is_pressed(' ') and not pressed[' ']:
                    pressed[' '] = True
                    action = Consts.DOWN_FAST
                elif keyboard.is_pressed('w') and not pressed['w']:
                    pressed['w'] = True
                    action = Consts.ROTATE_R

                if not keyboard.is_pressed('w'):
                    pressed['w'] = False

                if not keyboard.is_pressed(' '):
                    pressed[' '] = False

                if action != Consts.NONE:
                    break

                time.sleep(time_next / Consts.FPS)

            board, reward, done, info = self.game.step(action)
            self.game.render()

            if done:
                break

            if action == Consts.NONE:
                time.sleep(0.035)
            else:
                time.sleep(0.07)

        self.game.close()
