# import pygame
# import numpy as np
# from time import sleep
# import random
# import keyboard
#
# MARGIN = 4
# HEIGHT = 20
# WIDTH = 10
#
# DONE = 0
# END_GAME = 1
# R_LINE = 2
#
# magic_numbers = np.asarray([0.00765143, 0.00988836, 0.01277928, 0.01651537, 0.02134373,
#                             0.02758369, 0.03564793, 0.0460698, 0.05953856, 0.07694498,
#                             0.09944026, 0.12851216, 0.16608338, 0.21463876, 0.27738957,
#                             0.35848592, 0.46329123, 0.59873694, 0.77378094, 1])
#
#
# class RewardSystem():
#
#     def __init__(self, obs):
#
#         self.prev_holes = self.holes(obs)
#         x, y = self.solid_system(obs)
#
#         self.prev_block_counter = x
#
#     def calc_board(self, lines, obs, last_pos, done):
#         reward = self.reward(lines, last_pos, done, obs)
#         return reward
#
#     def holes(self, obs):
#         copy_obs = obs.copy()
#         stack = [(0, 5), (0, 4)]
#
#         for x, y in stack:
#             if 0 <= x < HEIGHT and 0 <= y < WIDTH and copy_obs[x][y] == 0:
#                 copy_obs[x][y] = 9
#                 stack.append((x - 1, y))
#                 stack.append((x + 1, y))
#                 stack.append((x, y - 1))
#                 stack.append((x, y + 1))
#
#         # print(copy_obs == 0.)
#         return (copy_obs == 0.).sum(axis=1).astype(float)
#
#     def height(self, obs):
#         heights = np.zeros(10)
#
#         for w in range(WIDTH):
#             for h in range(HEIGHT):
#                 if obs[h][w]:
#                     heights[w] = HEIGHT - h
#                     break
#
#         h_max = heights.max()
#
#         bumpiness = 0
#         for x, y in zip(heights, heights[1:]):
#             if x != y:
#                 bumpiness += np.abs(x - y) - 1
#
#         return h_max, bumpiness
#
#     def solid_system(self, obs):
#         solid = np.ones(20)
#
#         for h in range(HEIGHT):
#             groups = 0
#             last = False
#             for w in range(WIDTH):
#                 if obs[h][w] == last:
#                     continue
#                 elif obs[h][w]:
#                     groups += 1
#                     last = True
#                 elif not obs[h][w]:
#                     last = False
#             else:
#                 solid[h] = groups == 1
#
#         block_counter = obs.sum(axis=1)
#
#         return block_counter, solid
#
#     def reward(self, lines, last_pos, done, obs):
#
#         if done == END_GAME:
#             return 0
#
#         reward = 0
#         block_counter, solid = self.solid_system(obs)
#         holes = self.holes(obs)
#
#         lines_sum = lines.sum()
#         if lines_sum != 0:
#             reward += ((lines * lines_sum) * 40 * magic_numbers).sum()
#         else:
#             prev_bc = self.prev_block_counter
#             reward_bc = block_counter - prev_bc
#             reward_bc *= block_counter / 5
#             reward_bc[reward_bc < 0] = 0
#             reward_bc = reward_bc + reward_bc * solid
#             reward_bc *= magic_numbers
#             reward += reward_bc.sum() / 2
#
#             # print(self.prev_holes)
#             holes_reward = 1.5 * (self.prev_holes - holes)
#             # print(holes_reward)
#             holes_reward += (self.prev_holes == 0) * holes_reward
#             # print(holes_reward)
#             holes_reward *= magic_numbers
#
#             # print("HR, ", holes_reward.sum())
#
#             reward += holes_reward.sum()
#
#         self.prev_holes = holes
#         self.prev_block_counter = block_counter
#
#         return reward
#
#
# elements = [
#     np.array([
#         [1, 1],
#         [1, 1]
#     ]),
#     np.array([
#         [1, 0],
#         [1, 0],
#         [1, 1]
#     ]),
#     np.array([
#         [1],
#         [1],
#         [1],
#         [1]
#     ]),
#     np.array([
#         [1, 0],
#         [1, 1],
#         [1, 0]
#     ]),
#     np.array([
#         [0, 1],
#         [1, 1],
#         [1, 0]
#     ]),
#     np.array([
#         [1, 0],
#         [1, 1],
#         [0, 1]
#     ])
# ]
#
# colors = [
#     (255, 255, 0),
#     (0, 255, 0),
#     (0, 0, 255)
# ]
#
#
# class Tetris():
#
#     def __init__(self):
#         pass
#
#     def step(self, action):
#         self.last_down += 1
#
#         done = DONE
#         info = {}
#         reward = 0
#
#         if action == 1:
#             self._move_lr(-1)
#         elif action == 2:
#             self._move_lr(1)
#         elif action == 3:
#             reward, done = self._move_d(1)
#             self.last_down = 0
#         elif action == 4:
#             self._rotate()
#
#         if self.last_down >= 5:
#             self.last_down = 0
#             reward, done = self._move_d(1)
#
#         info = {"lines": self.lines_done}
#
#         return self._fast_fix(self.get_board()), reward, done, info
#
#     def one_hot(self, a, num_classes):
#         return np.squeeze(np.eye(num_classes)[a.reshape(-1)])
#
#     def _fast_fix(self, board):
#         return board
#         # return self.one_hot(board.astype(int), 3).reshape(-1)
#
#     def reset(self):
#         self.board = np.zeros((20, 10))
#         self.curr = elements[random.randint(0, 5)]
#         self.position = [0, 4]
#         self.screen = None
#         self.last_down = 0
#         self.lines_done = 0
#         self.moves = 0
#
#         # if np.random.randint(low=0, high=100) < 50:
#         #    self.train()
#
#         self.reward_system = RewardSystem(self.board)
#
#         return self._fast_fix(self.get_board())
#
#     def train(self):
#         random = np.random.binomial(1, 0.50, 10)
#         if random.sum() == 10:
#             random[np.random.randint(low=0, high=10)] = 0
#
#         self.board[19] = random
#
#         random = np.random.binomial(1, 0.25, 10)
#
#         self.board[18] = random * self.board[19]
#
#     def _move_lr(self, move):
#         next_position = self.position.copy()
#         next_position[1] += move
#
#         if not self._check_colision_pos(next_position):
#             return
#
#         self.position = next_position
#
#     def _move_d(self, move):
#         next_position = self.position.copy()
#         next_position[0] += move
#
#         if self._check_colision_pos(next_position):
#             self.position = next_position
#             return 0, False
#
#         return self._next_round()
#
#     def _next_round(self):
#         shape = self.curr.shape
#         self.board[self.position[0]:self.position[0] + shape[0],
#         self.position[1]:self.position[1] + shape[1]] += self.curr
#
#         done = DONE
#
#         lines = self.board.sum(axis=1) == 10
#
#         for i, r in enumerate(lines):
#             if r:
#                 done = R_LINE
#                 self.board[1:i + 1] = self.board[0:i]
#                 self.board[0] = np.zeros(10)
#
#         prev_position = self.position
#
#         self.curr = elements[random.randint(0, 5)]
#         self.position = [0, 4]
#
#         if not self._check_colision_pos(self.position):
#             done = END_GAME
#
#         self.lines_done += lines.sum()
#         reward = self.reward_system.calc_board(lines, self.board, prev_position, done)
#
#         return reward, done
#
#     def _rotate(self):
#
#         new_block = np.rot90(self.curr)
#         board = self.board.copy()
#         shape = new_block.shape
#
#         try:
#             board[self.position[0]:self.position[0] + shape[0],
#             self.position[1]:self.position[1] + shape[1]] += new_block
#             if (board > 1).sum() == 0:
#                 self.curr = new_block
#         except:
#             pass
#
#     def _check_colision_pos(self, position):
#         board = self.board.copy()
#         shape = self.curr.shape
#
#         if position[0] >= 20 or position[1] < 0 or position[1] >= 10:
#             return False
#
#         try:
#             board[position[0]:position[0] + shape[0], position[1]:position[1] + shape[1]] += self.curr
#             return (board > 1).sum() == 0
#         except:
#             return False
#
#     def close(self):
#         pygame.quit()
#         self.screen = None
#
#     def get_board(self):
#         board = self.board.copy()
#         shape = self.curr.shape
#
#         board[self.position[0]:self.position[0] + shape[0],
#         self.position[1]:self.position[1] + shape[1]] += self.curr * 2
#         board[board == 3] = 2
#
#         return board
#
#     def render(self):
#         if not self.screen:
#             pygame.init()
#             self.screen = pygame.display.set_mode((320, 640))
#
#         board = self.get_board()
#         self.screen.fill((0, 0, 0))
#
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 # Press Esc to quit.
#                 if event.key == pygame.K_ESCAPE:
#                     pass
#
#         for h in range(20):
#             for w in range(10):
#                 if board[h][w]:
#                     pygame.draw.rect(self.screen, colors[int(board[h][w]) - 1],
#                                      pygame.Rect(w * 32 + MARGIN, h * 32 + MARGIN, 32 - 2 * MARGIN, 32 - 2 * MARGIN))
#
#         pygame.display.update()
#         sleep(0.11)
