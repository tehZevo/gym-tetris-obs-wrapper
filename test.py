import numpy as np
from nes_py.wrappers import JoypadSpace
import gym_tetris
from gym_tetris.actions import MOVEMENT

from simple_tetris_board_wrapper import SimpleTetrisBoardWrapper

env = gym_tetris.make('TetrisA-v0')
env = JoypadSpace(env, MOVEMENT)
env = SimpleTetrisBoardWrapper(env)

import cv2

cv2.namedWindow("img", cv2.WINDOW_NORMAL)

done = False
while True:
    if done:
        state = env.reset()
        done = False
    state, reward, done, info = env.step(env.action_space.sample())
    cv2.imshow("img", state)
    cv2.waitKey(1)

env.close()
