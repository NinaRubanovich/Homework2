import numpy as np
from queue import PriorityQueue


# Will be an important part of Node class. Includes agent location and list of dirty squares
class State:

    def __init__(self, agent_location, dirty_squares):
        self.agent_location = agent_location  # tuple
        self.dirty_squares = dirty_squares  # list of tuples

    def get_agent_location(self):
        return self.agent_location

    def set_agent_location(self, agent_location):
        self.agent_location = agent_location

    def clean_room(self, room_tuple):
        self.dirty_squares.pop(room_tuple)

    def current_room_is_clean(self):
        # Check if room tuple exists in dirty tuple list
        if self.agent_location in self.dirty_squares:
            return True
        else:
            return False


class Node:
    def __init__(self, state, action, parent, cost):
        self.state = state  # refer to State class
        self.action = action  # can be Left, Right, Up, Down, or Suck
        self.parent = parent
        self.cost = cost  # 1.0 for Left, 0.9 for Right, 0.8 for Up, 0.7 for Down, 0.6 for Suck
        self.room_history = None


# -- -- -- -- HELPER FUNCTIONS -- -- -- -- -- --
def is_goal_state(state):
    # Check if all rooms are clean
    return not state.dirty_squares


def action_is_applicable(state, action):
    # Checks whether action is actually possible, i.e you can't suck a clean room
    current_location = state.get_agent_location()
    possible_actions = ['Left', 'Right', 'Up', 'Down', 'Suck']

    # Can't go left if agent is on leftmost column
    if current_location[1] == 1:
        possible_actions.remove('Left')

    # Can't go right is agent is in rightmost column
    if current_location[1] == 5:
        possible_actions.remove('Right')

    # Can't go up if agent is in top row
    if current_location[0] == 1:
        possible_actions.remove('Up')

    # Can't go down if agent is in bottom row
    if current_location[0] == 4:
        possible_actions.remove('Down')

    # Can't suck if current room is clean
    if state.current_room_is_clean():
        possible_actions.remove('Suck')

    if action in possible_actions:
        return True
    else:
        return False


def apply_action(state, action):
    current_location = state.get_agent_location()

    # Implement the logic to apply an action and generate the resulting state
    if action == 'Left':
        # shift the second integer of location tuple up by one
        state.set_agent_location((current_location[0], current_location[1]+1))
    if action == 'Right':
        # shift the second integer of the location tuple down by one
        state.set_agent_location((current_location[0], current_location[1]-1))
    if action == 'Up':
        # shift the first integer in the location tuple up by one
        state.set_agent_location((current_location[0]+1, current_location[1]))
    if action == 'Down':
        # shift the first integer in the location tuple down by one
        state.set_agent_location((current_location[0]-1, current_location[1]))
    if action == 'Suck':
        # remove current room from dirty room list. Location is not affected
        state.clean_room(current_location)
    return state


def get_action_cost(action):
    # Implement the logic to return the cost of an action
    if action == 'Left':
        return 1.0
    if action == 'Right':
        return 0.9
    if action == 'Up':
        return 0.8
    if action == 'Down':
        return 0.7
    if action == 'Suck':
        return 0.6


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


def extract_solution(final_node):
   pass
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
