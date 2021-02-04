"""
Simple interface for human movement
"""
from typing import Tuple
from abc import abstractmethod


class Movement:
    """
    Interface to create movement
    """
    @abstractmethod
    def next(self, time_next: float) -> Tuple[int, bool]:
        """
        Get next move
        :param time_next: time to make move
        :return: action, end
        :rtype: (int, bool)
        """
