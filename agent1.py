import numpy as np
from queue import PriorityQueue


class State:

    def __init__(self, agent_location, dirty_squares):
        self.agent_location = agent_location  # tuple
        self.dirty_squares - dirty_squares  # list of tuples
        def __eq__(self, other):
            return (self.agent_location == other.agent_location) and (self.dirty_squares == other.dirty_squares)


class Node:
    def __init__(self, state, action, parent, cost):
        self.state = state
        self.action = action  # can be Left, Right, Up, Down, or Suck
        self.parent = parent
        self.cost = cost  # 1.0 for Left, 0.9 for Right, 0.8 for Up, 0.7 for Down, 0.6 for Suck

    def breaktie(self):
        # breaks tie based on location coordinates

# -- -- -- -- HELPER FUNCTIONS -- -- -- -- -- --
def is_goal_state(state):
    # Check if all rooms are clean
    return not state.dirty_squares

def apply_action(state, action):
    # Implement the logic to apply an action and generate the resulting state
    pass

def get_action_cost(action):
    # Implement the logic to return the cost of an action
    pass

def expand(node):
    # Generates child node based on action costs and restraints
    actions = ['Left', 'Right', 'Up', 'Down', 'Suck']
    successors = []
    for action in actions:
        child_state = apply_action(node.state, action)
        if child_state:
            cost = get_action_cost(action)
            child_node = Node(child_state, action, node, cost)
            successors.append(child_node)
        return successors

def extract_solution(node):
    # Extract the solution path from the goal node
    pass

 # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --