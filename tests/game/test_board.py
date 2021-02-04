import numpy as np

from gym_tetris_simple.game.board import Board


def test_reset() -> None:
    # arrange
    board: Board = Board()
    board.board = np.ones((board.height, board.width))

    # act
    board.reset()

    # assert
    assert np.array_equal(board.board, np.zeros((board.height, board.width)))


def test_get_board() -> None:
    # arrange
    board: Board = Board(seed=0)
    board.board[19:] = 1

    board.next = 0
    board._next_block()
    board.position = np.array([5, 4])

    expected = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]).astype(float)

    # act
    result = board.get_board()

    # assert
    assert expected.shape == board.get_board().shape
    assert np.array_equal(result, expected)


def test_move_down() -> None:
    # arrange
    board: Board = Board(seed=0)

    board.next = 0
    board._next_block()
    board.position = np.array([4, 4])
    expected = np.array([5, 4])

    # act
    board.move_down()

    # assert
    assert np.array_equal(board.position, expected)

def test_move_down_placed() -> None:
    # arrange
    board: Board = Board(seed=0)

    board.next = 0
    board._next_block()
    board.position = np.array([18, 4])

    # act
    board.move_down()

    # assert
    assert np.array_equal(board.board.sum(), 4)


def test_move_down_line() -> None:
    # arrange
    board: Board = Board(seed=0)
    board.board[19:] = 1
    board.board[19][0] = 0
    board.board[19][1] = 0
    board.next = 0
    board._next_block()
    board.position = np.array([18, 0])
    expected = np.array([0, 4])

    # act
    info = board.move_down()

    # assert
    assert info['reward'] == 20
    assert info['lines'] == 1
    assert np.array_equal(board.position, expected)

def test_move_down_two_lines() -> None:
    # arrange
    board: Board = Board(seed=0)
    board.board[18:20] = 1
    board.board[18, 0:2] = 0
    board.board[19, 0:2] = 0
    board.next = 0

    board._next_block()
    board.position = np.array([18, 0])
    expected = np.array([0, 4])

    # act
    info = board.move_down()

    # assert
    assert info['reward'] == 80
    assert info['lines'] == 2
    assert np.array_equal(board.position, expected)

def test_move_fast_down() -> None:
    # arrange
    board: Board = Board(seed=0)

    board.next = 0
    board._next_block()
    board.position = np.array([0, 4])

    # act
    board.move_fast_down()

    # assert
    assert np.array_equal(board.board.sum(), 4)

def test_move_fast_down_toutch() -> None:
    # arrange
    board: Board = Board(seed=0)
    board.board[19][4] = 1

    board.next = 0
    board._next_block()
    board.position = np.array([0, 4])
    board.next = 0

    expected = np.array([
        [0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    ]).astype(float)

    # act
    board.move_fast_down()
    result = board.get_board()

    # assert
    assert expected.shape == board.get_board().shape
    assert np.array_equal(result, expected)


def test_move_left() -> None:
    # arrange
    board: Board = Board(seed=0)

    board.next = 0
    board._next_block()
    board.position = np.array([4, 4])
    expected = np.array([4, 3])

    # act
    board.move_left()

    # assert
    assert np.array_equal(board.position, expected)


def test_move_right() -> None:
    # arrange
    board: Board = Board(seed=0)

    board.next = 0
    board._next_block()
    board.position = np.array([4, 4])
    expected = np.array([4, 5])

    # act
    board.move_right()

    # assert
    assert np.array_equal(board.position, expected)


def test_rotate() -> None:
    # arrange
    board: Board = Board(seed=0)

    board.next = 2
    board._next_block()
    board.position = np.array([4, 4])
    shape = board.curr.shape

    # act
    board.rotate(1)

    # assert
    assert board.curr.shape == (shape[1], shape[0])


def test_rotate_L() -> None:
    # arrange
    board: Board = Board(seed=0)

    board.next = 1
    board._next_block()
    board.position = np.array([4, 4])
    shape = board.curr.shape
    expected = expected = np.array([
        [0, 0, 1],
        [1, 1, 1]
    ])

    # act
    board.rotate(1)

    # assert
    assert board.curr.shape == (shape[1], shape[0])
    assert np.array_equal(board.curr, expected)

def test_rotate_R() -> None:
    # arrange
    board: Board = Board(seed=0)

    board.next = 1
    board._next_block()
    board.position = np.array([4, 4])
    shape = board.curr.shape
    expected = expected = np.array([
        [1, 1, 1],
        [1, 0, 0]
    ])

    # act
    board.rotate(3)

    # assert
    assert board.curr.shape == (shape[1], shape[0])
    assert np.array_equal(board.curr, expected)