import pygame
from Game import Consts


class GUI(object):
    def __init__(self, height, width):
        pygame.init()
        self.height = height
        self.width = width
        self.screen = pygame.display.set_mode((560, 640))
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def render(self, board, info):

        pygame.event.get()

        self.screen.fill((0, 0, 0))

        self._draw_info(info)
        self._draw_game(board)

        pygame.display.update()

    def close(self):
        self.screen = None
        pygame.quit()

    def _draw_game(self, board):

        rect = pygame.Rect(0, 0, 320, 640)
        pygame.draw.rect(self.screen, (127, 127, 127), rect)

        for h in range(self.height):
            for w in range(self.width):
                if board[h][w]:
                    rect = pygame.Rect(w * 32 + Consts.MARGIN, h * 32 + Consts.MARGIN, 32 - 2 * Consts.MARGIN,
                                       32 - 2 * Consts.MARGIN)
                    pygame.draw.rect(self.screen, Consts.colors[int(board[h][w]) - 1], rect)

    def _draw_info(self, info):
        self.screen.blit(self.font.render('TETRIS', True, (127, 127, 127)), (385, 32))
        self.screen.blit(self.font.render(f"Lines: {info['Lines']}", True, (127, 127, 127)), (330, 96))
        self.screen.blit(self.font.render(f"Score: {info['Score']}", True, (127, 127, 127)), (330, 160))