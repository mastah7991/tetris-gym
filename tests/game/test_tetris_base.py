from unittest.mock import MagicMock
from typing import Any

from gym_tetris_simple.game import constants
from gym_tetris_simple.game.board import Board
from gym_tetris_simple.game.gui import Gui
from gym_tetris_simple.game.tetris_base import TetrisBase


def test_step_left() -> None:
    # arrange
    tetris: TetrisBase = TetrisBase(seed=0)
    board = Board(seed=0)
    board.move_left = MagicMock()
    tetris.board = board

    # act
    tetris.step(constants.LEFT)

    # assert
    board.move_left.assert_called_once()


def test_step_right() -> None:
    # arrange
    tetris: TetrisBase = TetrisBase(seed=0)
    board = Board(seed=0)
    board.move_right = MagicMock()
    tetris.board = board

    # act
    tetris.step(constants.RIGHT)

    # assert
    board.move_right.assert_called_once()

def test_step_down_fast() -> None:
    # arrange
    tetris: TetrisBase = TetrisBase(seed=0)
    board = Board(seed=0)
    board.move_fast_down = MagicMock()
    tetris.board = board

    # act
    tetris.step(constants.DOWN_FAST)

    # assert
    board.move_fast_down.assert_called_once()

def test_step_down() -> None:
    # arrange
    tetris: TetrisBase = TetrisBase(seed=0)
    board = Board(seed=0)
    board.move_down = MagicMock()
    tetris.board = board

    # act
    tetris.step(constants.DOWN)

    # assert
    board.move_down.assert_called_once()

def test_step_rotate_l() -> None:
    # arrange
    tetris: TetrisBase = TetrisBase(seed=0)
    board = Board(seed=0)
    board.rotate = MagicMock()
    tetris.board = board

    # act
    tetris.step(constants.ROTATE_L)

    # assert
    board.rotate.assert_called_once_with(1)

def test_step_rotate_r() -> None:
    # arrange
    tetris: TetrisBase = TetrisBase(seed=0)
    board = Board(seed=0)
    board.rotate = MagicMock()
    tetris.board = board

    # act
    tetris.step(constants.ROTATE_R)

    # assert
    board.rotate.assert_called_once_with(3)

def test_step_down_auto() -> None:
    # arrange
    tetris: TetrisBase = TetrisBase(seed=0)
    board = Board(seed=0)
    board.move_down = MagicMock()
    tetris.board = board

    # act
    tetris.step(constants.NONE)
    tetris.step(constants.NONE)
    tetris.step(constants.NONE)
    tetris.step(constants.NONE)
    tetris.step(constants.NONE)

    # assert
    board.move_down.assert_called_once()
    assert tetris.last_down == 0

def test_step_none() -> None:
    # arrange
    tetris: TetrisBase = TetrisBase(seed=0)
    board = Board(seed=0)
    board.move_down = MagicMock()
    tetris.board = board

    # act
    tetris.step(constants.NONE)
    assert tetris.last_down == 1
    tetris.step(constants.NONE)
    assert tetris.last_down == 2
    tetris.step(constants.NONE)
    assert tetris.last_down == 3
    tetris.step(constants.NONE)
    assert tetris.last_down == 4

    # assert
    board.move_down.assert_not_called()

def test_step_get_info() -> None:
    # arrange
    tetris: TetrisBase = TetrisBase(seed=0)
    board = Board(seed=0)
    board.get_board = MagicMock()
    board.move_down = MagicMock()

    board.get_board.return_value = "TEST"
    board.move_down.return_value = {"lines": 1, "reward": 50, "done": True}

    tetris.board = board

    # act
    result = tetris.step(constants.DOWN)

    # assert
    assert result == ("TEST", 50, True, {'Score': 50, 'Lines': 1, 'Next': 0, 'NewLine': True})

def test_step_update_info() -> None:
    # arrange
    tetris: TetrisBase = TetrisBase(seed=0)
    tetris.glob_info['Score'] = 128
    tetris.glob_info['Lines'] = 6
    board = Board(seed=0)
    board.get_board = MagicMock()
    board.move_down = MagicMock()

    board.get_board.return_value = "TEST"
    board.move_down.return_value = {"lines": 1, "reward": 50, "done": True}

    tetris.board = board

    # act
    result = tetris.step(constants.DOWN)

    # assert
    assert result == ("TEST", 50, True, {'Score': 178, 'Lines': 7, 'Next': 0, 'NewLine': True})

def test_reset() -> None:
    # arrange
    tetris: TetrisBase = TetrisBase(seed=0)
    tetris.glob_info['Score'] = 128
    tetris.glob_info['Lines'] = 6

    board = Board(seed=0)
    board.get_board = MagicMock()
    board.get_board.return_value = "TEST"
    tetris.board = board

    # act
    result = tetris.reset()

    # assert
    assert result == "TEST"
    assert tetris.glob_info['Score'] == 0
    assert tetris.glob_info['Lines'] == 0


def test_render() -> None:
    # arrange
    tetris: TetrisBase = TetrisBase(seed=0)

    board = Board(seed=0)
    board.get_board = MagicMock()
    board.get_board.return_value = "TEST"
    tetris.board = board

    gui = Gui(20, 10)
    gui.render = MagicMock()

    tetris.gui = gui

    # act
    tetris.render()

    # assert
    gui.render.assert_called_once()


def test_close() -> None:
    # arrange
    tetris: TetrisBase = TetrisBase(seed=0)

    gui: Any = Gui(20, 10)
    gui.close = MagicMock()

    tetris.gui = gui

    # act
    tetris.close()

    # assert
    gui.close.assert_called_once()
    assert tetris.gui == None