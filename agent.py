import numpy as np


class State:

    def __init__(self, agent_location, dirty_squares):
        self.agent_location = agent_location  # tuple
        self.dirty_squares - dirty_squares  # list of tuples

        # method for state comparison??


class Node:
    def __init__(self, state, action, parent, cost):
        self.state = state
        self.action = action  # can be Left, Right, Up, Down, or Suck
        self.parent = parent
        self.cost = cost  # 1.0 for Left, 0.9 for Right, 0.8 for Up, 0.7 for Down, 0.6 for Suck

    def __breaktie__(self):
        # breaks tie based on location coordinates

