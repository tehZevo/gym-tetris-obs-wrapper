from setuptools import setup

setup(
    name="gym_tetris_obs_wrapper",
    version="0.1.0",
    description="Wrapper for simpler gym-tetris observations",
    install_requires=[
      "gym-tetris",
      "skimage",
      "gym<=0.18.3",
      "numpy"
    ],
)
