# 0 represents a clean room, 1 represents a dirty room
environment = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]
action_cost = {
    "Left": 1.0,
    "Right": 0.9,
    "Up": 0.8,
    "Down": 0.7,
    "Suck": 0.6
}

#goal state: All rooms are clean
def is_goal_state(state):
    for row in state:
        for room in row:
            if room == 1:
                return False
    return True

def get_successors(state):
    successors = []
    rows, cols = len(state), len(state[0])
    for i in range(rows):
        for j in range(cols):
            if state[i][j] == 1:
                # If the room is dirty, you can choose to suck it
                successor = [row[:] for row in state]  # Create a copy of the current state
                successor[i][j] = 0  # Suck the dirt
                successors.append(("Suck", successor))
            else:
                # If the room is clean, you can move or stay
                if i > 0:
                    # Move Up
                    successor = [row[:] for row in state]
                    successors.append(("Up", successor))
                if i < rows - 1:
                    # Move Down
                    successor = [row[:] for row in state]
                    successors.append(("Down", successor))
                if j > 0:
                    # Move Left
                    successor = [row[:] for row in state]
                    successors.append(("Left", successor))
                if j < cols - 1:
                    # Move Right
                    successor = [row[:] for row in state]
                    successors.append(("Right", successor))
    return successors



# Uniform Cost Search function
def uniform_cost_search(start_state):
    queue = [(0, start_state, [])]  # (cost, state, path) tuple
    visited = set()
    best_path = None
    best_cost = float("inf")

    while queue:
        cost, state, path = queue.pop(0)
        print("Step state:")
        for row in state:
            print(row)
        if is_goal_state(state):
            if cost < best_cost:
                best_cost = cost
                best_path = path
                print("Complete path found:", best_path)
            elif cost == best_cost:
                print("Complete path found:", path)

        # Convert the state (list) to a tuple before adding it to the set
        if tuple(map(tuple, state)) not in visited:
            visited.add(tuple(map(tuple, state)))
            successors = get_successors(state)
            for action, successor_state in successors:
                successor_cost = cost + action_cost[action]
                successor_path = path + [action]
                queue.append((successor_cost, successor_state, successor_path))
                queue.sort(key=lambda x: x[0])  # Sort by cost
                #print(f"Taking action: {action}, Cost: {successor_cost}")

    return best_path

# Main function
if __name__ == '__main__':
    start_state = environment
    print("Starting state:")
    for row in start_state:
        print(row)
    best_path = uniform_cost_search(start_state)
    print("Best path:", best_path)
    print("Total cost of the best path:", sum(action_cost[action] for action in best_path))
