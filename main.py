import numpy as np
import iterativeDeepeningTreeSearch


def uniform_cost_tree_search():
    pass


def uniform_cost_graph_search():
    pass


def iterative_deepening_tree_search(state):
    depth_limit = 0
    while True:
        result, solution = depth_limited_search(state, depth_limit)
        if result == "found":
            return solution  # Return the solution path
        elif result == "cutoff":
            depth_limit += 1
        elif result == "not_found":
            return None


def depth_limited_search(state, depth_limit):
    # This is a helper function for iterative_deepening_tree_search
    return recursive_dls(iterativeDeepeningTreeSearch.Node(state, None, None, 0), depth_limit, [])


def recursive_dls(node, depth_limit, path):
    if node.state.current_room_is_clean() and len(node.state.dirty_squares) == 0:
        return "found", path  # Return the solution path when found

    if depth_limit == 0:
        return "cutoff", None

    cutoff_occurred = False

    for action in ["Left", "Right", "Up", "Down", "Suck"]:
        if iterativeDeepeningTreeSearch.action_is_applicable(node.state, action):
            child_state = iterativeDeepeningTreeSearch.apply_action(node.state, action)
            if child_state:
                child_node = iterativeDeepeningTreeSearch.Node(child_state, action, node,
                                                               iterativeDeepeningTreeSearch.get_action_cost(action))
                result, result_path = recursive_dls(child_node, depth_limit - 1, path + [action])
                if result == "found":
                    return "found", result_path
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

    # Uniform Cost Tree Search

    # Uniform Cost Graph Search

    # Iterative Deepening Tree search
    initial_state = iterativeDeepeningTreeSearch.State(agent_location, dirty_squares)
    idts_solution = iterative_deepening_tree_search(initial_state)
    if idts_solution:
        print("Solution found in IDTS! Actions to clean all dirty squares:")
        print(idts_solution)  # Print the sequence of actions
    else:
        print("No solution found.")
