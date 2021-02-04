from unittest.mock import MagicMock
from typing import Any
import time as computer_time

import pytest

from gym_tetris_simple.game import constants
from gym_tetris_simple.movement.human_movement import HumanMovement
from gym_tetris_simple.movement.movement import Movement

import keyboard as computer_keyboard


@pytest.mark.parametrize("key,expected", [
    ('a', constants.LEFT),
    ('d', constants.RIGHT),
    ('s', constants.DOWN),
    (' ', constants.DOWN_FAST),
    ('w', constants.ROTATE_R),
])
def test_next(key, expected) -> None:
    # arrange
    keyboard: Any = computer_keyboard
    time: Any = computer_time
    movement: Movement = HumanMovement(keyboard, time)

    keyboard.is_pressed = MagicMock()
    time.sleep = MagicMock()

    def pressed(*args, **kwargs) -> object:
        if args[0] == key:
            return True
        return False

    keyboard.is_pressed.side_effect = pressed

    # act
    action, end_game = movement.next(0)

    # assert
    assert action == expected


@pytest.mark.parametrize("key,expected", [
    (' ', constants.DOWN_FAST),
    ('w', constants.ROTATE_R),
])
def test_next_release(key, expected) -> None:
    # arrange
    keyboard: Any = computer_keyboard
    time: Any = computer_time
    movement: HumanMovement = HumanMovement(keyboard, time)

    keyboard.is_pressed = MagicMock()
    time.sleep = MagicMock()

    def pressed(*args, **kwargs) -> object:
        if args[0] == key:
            return True
        return False

    def pressed_none(*args, **kwargs) -> object:
        return False

    keyboard.is_pressed.side_effect = pressed

    # act
    action, end_game = movement.next(0)

    # assert
    assert action == expected
    assert movement.pressed[key]

    # arrange
    keyboard.is_pressed.side_effect = pressed_none

    # act
    action, end_game = movement.next(0)

    # assert
    assert action == constants.NONE
    assert not movement.pressed[key]


def test_next_none() -> None:
    # arrange
    keyboard: Any = computer_keyboard
    time: Any = computer_time
    movement: Movement = HumanMovement(keyboard, time)

    keyboard.is_pressed = MagicMock()
    time.sleep = MagicMock()

    keyboard.is_pressed.return_value = False

    # act
    movement.next(0)

    # assert
    assert time.sleep.call_count == constants.FPS
