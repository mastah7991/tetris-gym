from setuptools import setup, find_packages

setup(
    name="gym_tetris_simple",
    version="0.0.9",
    author="mastah7991",
    author_email="mastah7991@gmail.com",
    description="Gym env",
    url="https://github.com/",
    packages=find_packages(),
    install_requires=['gym>=0.18.0', 'pygame>=2.0.1', 'numpy>=1.19.1', 'keyboard>=0.13.5'],
    python_requires='>=3.6',
)