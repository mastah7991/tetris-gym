"""
Base human movement
"""
from typing import Tuple, Any, Dict, Type, TypeVar

import time as computer_time
import keyboard as computer_keyboard

from gym_tetris_simple.game import constants
from gym_tetris_simple.movement.movement import Movement

TypeObject = TypeVar('TypeObject', bound='HumanMovement')


class HumanMovement(Movement):
    """
    Simple human movement
    """
    def __init__(self, keyboard: Any, time: Any) -> None:
        self.keyboard: Any = keyboard
        self.time: Any = time
        self.pressed: Dict[str, bool] = {'w': False, ' ': False}

    @classmethod
    def base_movement(cls: Type[TypeObject]) -> TypeObject:
        """
        Create human movement using real timer and keyboard
        :return: HumanMovement
        """
        return cls(computer_keyboard, computer_time)

    def next(self, time_next: float) -> Tuple[int, bool]:
        """
        Get from keyboard next move
        :param time_next: time to make move
        :return: action, end
        :rtype: (int, bool)
        """
        action = constants.NONE
        end_game = False

        for _ in range(constants.FPS):

            if self.keyboard.is_pressed('esc'):
                end_game = True
                print("END")
                break

            if self.keyboard.is_pressed('a'):
                action = constants.LEFT
            elif self.keyboard.is_pressed('d'):
                action = constants.RIGHT
            elif self.keyboard.is_pressed('s'):
                action = constants.DOWN
            elif self.keyboard.is_pressed(' ') and not self.pressed[' ']:
                self.pressed[' '] = True
                action = constants.DOWN_FAST
            elif self.keyboard.is_pressed('w') and not self.pressed['w']:
                self.pressed['w'] = True
                action = constants.ROTATE_R

            if not self.keyboard.is_pressed('w'):
                self.pressed['w'] = False

            if not self.keyboard.is_pressed(' '):
                self.pressed[' '] = False

            if action != constants.NONE:
                break

            self.time.sleep(time_next / constants.FPS)

        return action, end_game
