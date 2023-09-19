import numpy as np
import agent1
# feel free to import your personal files here


def uniform_cost_tree_search():
    pass


def uniform_cost_graph_search():
    pass


def iterative_deepening_tree_search(initial_state):
    depth_limit = 0
    while True:
        result, cutoff = depth_limited_search(initial_state, depth_limit)
        if result == "found":
            return cutoff
        elif result == "cutoff":
            depth_limit += 1
        elif result == "not_found":
            return None


def depth_limited_search(state, depth_limit):
    # This is a helper function for iterative_deepening_tree_search
    return recursive_dls(agent1.Node(state, None, None, 0), depth_limit)


def recursive_dls(node, depth_limit):
    if node.state.current_room_is_clean() and len(node.state.dirty_squares) == 0:
        return "found", node

    if depth_limit == 0:
        return "cutoff", None

    cutoff_occurred = False

    for action in ["Left", "Right", "Up", "Down", "Suck"]:
        if agent1.action_is_applicable(node.state, action):
            child_state = agent1.apply_action(node.state, action)
            if child_state:
                child_node = agent1.Node(child_state, action, node, agent1.get_action_cost(action))
                result, result_node = recursive_dls(child_node, depth_limit - 1)
                if result == "found":
                    return "found", result_node
                elif result == "cutoff":
                    cutoff_occurred = True

    if cutoff_occurred:
        return "cutoff", None
    else:
        return "not_found", None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # initialize state
    agent_location = (2, 2)
    dirty_squares = [(1, 2), (2, 4), (3, 5)]

    # initial_state = agent1.State(agent_location, dirty_squares)
    # iterative_deepening_tree_search(initial_state)

