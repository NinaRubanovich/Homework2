# algorithms coded by Jade Neeley
# additions made to report running results

from agent import *
import time

def uniform_cost_tree_search(problem):
    fringe = [((problem.initial_location,), 0, problem)]  # Initialize fringe with an empty path and dirty squares
    
    nodes_expanded = 0
    nodes_generated = 1  
    start_time = time.time()

    while fringe:
        fringe.sort(key=lambda x: (x[1], x[0]))  # Sort by cost, then coordinates for tie-breaking
        path, cost, current_state = fringe.pop(0)

        if current_state.is_goal_state():
            execution_time = time.time() - start_time
            return path[1:], nodes_expanded, nodes_generated, execution_time

        nodes_expanded += 1
        successors = current_state.get_successors()
        for action, successor in successors:
            nodes_generated += 1
            fringe.append((path + (action,), cost + ACTION_COSTS[action], successor))

    return None

def uniform_cost_graph_search(problem):
    closed = set()  
    fringe = [((problem.initial_location,), 0, problem, problem.dirty_squares)]  # Initialize fringe with an empty path and dirty squares
    
    nodes_expanded = 0
    nodes_generated = 1 
    start_time = time.time()

    while fringe:
        fringe.sort(key=lambda x: (x[1], x[2].current_location, x[3]))  # Sort by cost, then location, then dirty squares for tie-breaking
        path, cost, current_state, dirty_squares = fringe.pop(0)

        if current_state.is_goal_state():
            execution_time = time.time() - start_time
            return path[1:], nodes_expanded, nodes_generated, execution_time

        if current_state not in closed: 
            closed.add(current_state)
            nodes_expanded += 1
            successors = current_state.get_successors()
            for action, successor in successors:
                    nodes_generated += 1
                    new_dirty_squares = successor.dirty_squares
                    fringe.append((path + (action,), cost + ACTION_COSTS[action], successor, new_dirty_squares))

    return None

def iterative_deepening_tree_search(problem):
    max_depth = 0
    while True:
        result = depth_limited_tree_search(problem, max_depth)
        if result is not None:
            return result
        max_depth += 1


def depth_limited_tree_search(problem, limit):
    fringe = [((problem.initial_location,), 0, problem)] # Initialize the closed set as an empty set
    
    nodes_expanded = 0
    nodes_generated = 1 
    start_time = time.time()

    while fringe:
        fringe.sort(key=lambda x: (x[1], x[0]))  # Sort by cost, then coordinates for tie breaking
        path, cost, current_state = fringe.pop(0)

        if current_state.is_goal_state():
            execution_time = time.time() - start_time
            return path[1:], nodes_expanded, nodes_generated, execution_time

        if len(path) <= limit:
            nodes_expanded += 1
            successors = current_state.get_successors()
            for action, successor in successors:
                nodes_generated += 1
                fringe.append((path + (action,), cost + ACTION_COSTS[action], successor))

    return None


def main():
    for instance_num, instance in enumerate(PROBLEM_INSTANCES, start=1):
        initial_location = instance['initial_location']
        dirty_squares = instance['dirty_squares']

        print(f"Instance #{instance_num}:")
        print("Initial Location:", initial_location)
        print("Dirty Squares:", dirty_squares)

        problem = VacuumWorldProblem(initial_location, dirty_squares)

        # Uniform Cost Tree Search
        print("\nUniform Cost Tree Search:")
        result = uniform_cost_tree_search(problem)
        if result:
            path, nodes_expanded, nodes_generated, execution_time = result
            print("Path:", path)
            print("Nodes Expanded:", nodes_expanded)
            print("Nodes Generated:", nodes_generated)
            print("Execution Time (s):", execution_time)
            print("Number of Moves in Solution:", len(path))
            print("Cost of Solution:", sum(ACTION_COSTS[action] for action in path))
        else:
            print("No solution found.")

        # Uniform Cost Graph Search
        print("\nUniform Cost Graph Search:")
        result = uniform_cost_graph_search(problem)
        if result:
            path, nodes_expanded, nodes_generated, execution_time = result
            print("Path:", path)
            print("Nodes Expanded:", nodes_expanded)
            print("Nodes Generated:", nodes_generated)
            print("Execution Time (s):", execution_time)
            print("Number of Moves in Solution:", len(path))
            print("Cost of Solution:", sum(ACTION_COSTS[action] for action in path))
        else:
            print("No solution found.")

        # Iterative Deepening Tree Search
        print("\nIterative Deepening Tree Search:")
        result = iterative_deepening_tree_search(problem)
        if result:
            path, nodes_expanded, nodes_generated, execution_time = result
            print("Path:", path)
            print("Nodes Expanded:", nodes_expanded)
            print("Nodes Generated:", nodes_generated)
            print("Execution Time (s):", execution_time)
            print("Number of Moves in Solution:", len(path))
            print("Cost of Solution:", sum(ACTION_COSTS[action] for action in path))
        else:
            print("No solution found.")

        print("\n------------------------\n")


if __name__ == "__main__":
    main()


### RESULTS ###

# Instance #1:
# Initial Location: (2, 2)
# Dirty Squares: [(1, 2), (2, 4), (3, 5)]

# Uniform Cost Tree Search:
# Path: ('Up', 'Down', 'Right', 'Right', 'Down', 'Right')
# Nodes Expanded: 1321
# Nodes Generated: 4471
# Execution Time (s): 0.2973511219024658
# Number of Moves in Solution: 6
# Cost of Solution: 4.9

# Uniform Cost Graph Search:
# Path: ('Up', 'Down', 'Right', 'Right', 'Down', 'Right')
# Nodes Expanded: 1304
# Nodes Generated: 4441
# Execution Time (s): 0.2837197780609131
# Number of Moves in Solution: 6
# Cost of Solution: 4.9

# Iterative Deepening Tree Search:
# Path: ('Up', 'Down', 'Right', 'Right', 'Down', 'Right')
# Nodes Expanded: 756
# Nodes Generated: 2541
# Execution Time (s): 0.19977903366088867
# Number of Moves in Solution: 6
# Cost of Solution: 4.9

# ------------------------

# Instance #2:
# Initial Location: (3, 2)
# Dirty Squares: [(1, 2), (2, 1), (2, 4), (3, 3)]

# Uniform Cost Tree Search:
# Path: ('Right', 'Right', 'Up', 'Left', 'Left', 'Up', 'Down', 'Left')
# Nodes Expanded: 26434
# Nodes Generated: 88099
# Execution Time (s): 170.33823204040527
# Number of Moves in Solution: 8
# Cost of Solution: 7.1

# Uniform Cost Graph Search:
# Path: ('Right', 'Up', 'Right', 'Left', 'Left', 'Up', 'Down', 'Left')
# Nodes Expanded: 26027
# Nodes Generated: 86607
# Execution Time (s): 448.6521439552307
# Number of Moves in Solution: 8
# Cost of Solution: 7.1

# Iterative Deepening Tree Search:
# Path: ('Right', 'Right', 'Up', 'Left', 'Left', 'Up', 'Down', 'Left')
# Nodes Expanded: 8509
# Nodes Generated: 28533
# Execution Time (s): 47.01594805717468
# Number of Moves in Solution: 8
# Cost of Solution: 7.1

# ------------------------