
# structures and helper function definitions were generated by ChatGPT
# changes and implementation made by Jade Neeley
# additional comments, cleanup, and structure by Nina Rubanovich and Gavin Boley

# Define the 2D grid
GRID_ROWS = 4
GRID_COLS = 5

# Define the actions
ACTIONS = ['Left', 'Right', 'Up', 'Down', 'Suck']

# Define the action costs
ACTION_COSTS = {
    'Left': 1.0,
    'Right': 0.9,
    'Up': 0.8,
    'Down': 0.7,
    'Suck': 0.6
}

# Define the problem instances
PROBLEM_INSTANCES = [
    {
        'initial_location': (2, 2),
        'dirty_squares': [(1, 2), (2, 4), (3, 5)]
    },
    {
        'initial_location': (3, 2),
        'dirty_squares': [(1, 2), (2, 1), (2, 4), (3, 3)]
    }
]

# Define helper functions
class VacuumWorldProblem:
    def __init__(self, initial_location, dirty_squares):
        
        # Create the Vacuum World initial state
        self.initial_location = initial_location
        self.dirty_squares = set(dirty_squares)
        self.current_location = initial_location

    def is_goal_state(self):
        return not self.dirty_squares # If any dirty squares exist, goal state not met

    def get_successors(self): # Generate potential states for successor actions.
        successors = []
        for action in ACTIONS:
            new_state = self.apply_action(action)
            if new_state != self:
                successors.append((action, new_state))
        return successors

    def apply_action(self, action): # Apply the specified action to the current state, creates new iteration
        if action == 'Left':
            new_location = (self.current_location[0], max(1, self.current_location[1] - 1))
        elif action == 'Right':
            new_location = (self.current_location[0], min(GRID_COLS, self.current_location[1] + 1))
        elif action == 'Up':
            new_location = (max(1, self.current_location[0] - 1), self.current_location[1])
        elif action == 'Down':
            new_location = (min(GRID_ROWS, self.current_location[0] + 1), self.current_location[1])
        else:
            new_location = self.current_location

        if new_location == self.current_location: # No impact on state, nothing changed, return same state
            return self

        new_dirty_squares = self.dirty_squares.copy()
        if new_location in new_dirty_squares: # Agent has successfully cleaned a dirty square by moving to it
            new_dirty_squares.remove(new_location) # Therefore removes the location of the dirty square

        return VacuumWorldProblem(new_location, new_dirty_squares) # New State
