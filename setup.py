from setuptools import setup, find_packages

setup(
    name="gym_tetris_obs_wrapper",
    version="0.1.0",
    description="Wrapper for simpler gym-tetris observations",
    install_requires=[
      "gym-tetris",
      "scikit-image",
      "gym<=0.18.3",
      "numpy"
    ],
    packages=find_packages()
)
