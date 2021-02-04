from unittest.mock import MagicMock

from gym_tetris_simple import Human
from gym_tetris_simple.game.tetris_base import TetrisBase
from gym_tetris_simple.movement.human_movement import HumanMovement
from gym_tetris_simple.movement.movement import Movement


def test_play_done() -> None:
    # arrange
    game: TetrisBase = TetrisBase()
    movement: Movement = HumanMovement.base_movement()
    tetris: Human = Human(game, movement)

    movement.next = MagicMock()
    game.reset = MagicMock()
    game.step = MagicMock()
    game.render = MagicMock()
    game.close = MagicMock()

    movement.next.return_value = (0, False)
    game.step.return_value = (0, 0, True, 0)

    # act
    tetris.play()

    # assert
    game.reset.assert_called_once()
    game.step.assert_called_once()
    game.render.assert_called_once()
    game.close.assert_called_once()

def test_play_quit() -> None:
    # arrange
    game: TetrisBase = TetrisBase()
    movement: Movement = HumanMovement.base_movement()
    tetris: Human = Human(game, movement)

    movement.next = MagicMock()
    game.reset = MagicMock()
    game.step = MagicMock()
    game.render = MagicMock()
    game.close = MagicMock()

    movement.next.return_value = (0, True)
    game.step.return_value = (0, 0, False, 0)

    # act
    tetris.play()

    # assert
    game.reset.assert_called_once()
    game.step.assert_called_once()
    game.render.assert_called_once()
    game.close.assert_called_once()


