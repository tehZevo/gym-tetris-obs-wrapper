import numpy as np
from skimage.transform import resize
import gym
from gym.spaces import Box

class GymTetrisObsWrapper(gym.ObservationWrapper):
  def __init__(self, env):
    super().__init__(env)
    self.observation_space = Box(shape=(20, 10), low=0, high=1)

  def observation(self, obs):
    #minos are 7x7 with a shared 1 px border, making them technically 8x8 with a 1px border on top/left side
    #this trims 1px off the bottom and right edges to account for this so the board is divisible by 8
    obs = obs[47:-33, 95:-81]
    #then scale by 8
    h, w = np.array(obs.shape[:2]) // 8
    obs = resize(obs, (h, w), anti_aliasing=False)
    #map to 0/1 range
    obs = (np.mean(obs, axis=-1) > 0.1).astype("float32")
    return obs
