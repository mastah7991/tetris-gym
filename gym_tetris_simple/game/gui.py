"""
Simple Gui to render preview of game
"""
from typing import Dict, Any

import numpy as np
import pygame
from gym_tetris_simple.game import constants


class Gui:
    """
       A class to create base Gui
    """
    def __init__(self, height: int, width: int):
        """
        Create Base Gui
        :param height: height of board
        :param width: width of board
        """
        pygame.init()
        self.screen: Any = pygame.display.set_mode((width*32+240, height*32))

        self.height: int = height
        self.width: int = width
        self.font: Any = pygame.font.Font('freesansbold.ttf', 32)

    def render(self, board: np.ndarray, info: Dict[str, int])->None:
        """
        Render current frame
        :param board: current board
        :param info: current info about game
        :return: None
        """
        pygame.event.get()

        self.screen.fill((0, 0, 0))

        self._draw_info(info)
        self._draw_game(board)

        pygame.display.update()

    def close(self) -> None:
        """
        Close the pygame window
        :return: None
        """
        pygame.quit()
        self.screen = None

    def _draw_game(self, board: np.ndarray) -> None:

        rect = pygame.Rect(0, 0, self.width*32, self.height*32)
        pygame.draw.rect(self.screen, (127, 127, 127), rect)

        for height in range(self.height):
            for width in range(self.width):
                if board[height][width]:
                    rect = pygame.Rect(
                        width * 32 + constants.MARGIN,
                        height * 32 + constants.MARGIN,
                        32 - 2 * constants.MARGIN,
                        32 - 2 * constants.MARGIN
                    )

                    pygame.draw.rect(self.screen,
                                     constants.colors[int(board[height][width]) - 1],
                                     rect)

    def _draw_info(self, info: Dict[str, int]) -> None:
        self.screen.blit(
            self.font.render('TETRIS',
                             True,
                             (127, 127, 127)
                             ),
            (self.width*32+64, 32)
        )
        self.screen.blit(
            self.font.render(f"Lines: {info['Lines']}",
                             True,
                             (127, 127, 127)
                             ),
            (self.width*32+10, 96)
        )
        self.screen.blit(
            self.font.render(f"Score: {info['Score']}",
                             True,
                             (127, 127, 127)
                             ),
            (self.width*32+10, 160)
        )
