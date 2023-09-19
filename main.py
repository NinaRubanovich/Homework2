import numpy as np
import agent1


def uniform_cost_tree_search():
    pass


def uniform_cost_graph_search():
    pass


def iterative_deepening_tree_search(initial_state, max_depth):
    for depth in range(max_depth + 1):
        result = depth_limited_search(initial_state, depth)
        if result:
            return result


def depth_limited_search(initial_state, depth):
    # This is a helper function for iterative_deepening_tree_search
    def recursive_dls(node, problem, limit):
        if agent1.is_goal_state(node.state):
            return agent1.extract_solution(node)
        elif limit == 0:
            return "cutoff"
        else:
            cutoff_occured = False
            for child_node in agent1.expand(node):
                result = recursive_dls(child_node, problem, limit - 1)
                if result == "cutoff":
                    cutoff_occured = True
                elif result != "failure":
                    return result
                return "cutoff" if cutoff_occured else "failure"

    return recursive_dls(agent1.Node(initial_state, None, None, 0), None, depth)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # initialize state
    agent_location = (2, 2)
    dirty_squares = [(1, 2), (2, 4), (3, 5)]

