import numpy as np
import agent


# -- -- -- -- HELPER FUNCTIONS -- -- -- -- -- --
def is_goal_state(state):
    # Check if all rooms are clean
    return not state.dirty_squares


def expand(node):
    # Generates child node based on action costs and restraints
    pass


def extract_solution(node):
    # Extract the solution path from the goal node
    pass


# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
def uniform_cost_tree_search():
    print("delete this")


def uniform_cost_graph_search():
    print("delete this")


def iterative_deepening_tree_search():
    print("delete this")


def depth_limited_search():
    # This is a helper function for iterative_deepening_tree_search
    print("delete this")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # initialize state
    agent_location = (2, 2)
    dirty_squares = [(1, 2), (2, 4), (3, 5)]
    initial_state = agent.State(agent_location, dirty_squares)
