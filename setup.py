"""
Register all the necessary information to create a PIP package
"""
import os.path
import sys

from setuptools import setup

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'gym_tetris_simple'))

setup(
    name="gym_tetris_simple",
    version="0.1.6",
    author="mastah7991",
    author_email="mastah7991@gmail.com",
    description="Gym env",
    url="https://github.com/",
    packages=['gym_tetris_simple', 'gym_tetris_simple.env', 'gym_tetris_simple.game'],


    install_requires=['gym>=0.18.0', 'pygame>=2.0.1', 'numpy>=1.19.1', 'keyboard>=0.13.5'],
    python_requires='>=3.6',
)
