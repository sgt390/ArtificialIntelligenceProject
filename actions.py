import numpy as np


# Create a matrix of allowed actions for each position in the environment
def make_actions(x_dim, y_dim, goal):
    actions = np.array([[{0, 1, 2, 3} for _ in range(y_dim)] for _ in range(x_dim)])
    for x in range(x_dim):
        for y in range(y_dim):
            neighbors = {}
            if x > 0:
                neighbors[0] = actions[x-1, y]
            if y > 0:
                neighbors[3] = actions[x, y-1]
            if x < x_dim-1:
                neighbors[2] = actions[x+1, y]
            if y < y_dim-1:
                neighbors[1] = actions[x, y+1]
            action, neighbors = update_action(x, y, actions[x, y], x_dim, y_dim, neighbors)
            actions[x, y] = action
            actions = update_neighbors(x, y, actions, neighbors)
    actions[goal] = {4}
    return actions


# Main function to compute operations on a single action and its neighbors
def update_action(x, y, action, x_dim, y_dim, neighbor):
    action = remove_edges_action((x, y), action, x_dim, y_dim)
    action, neighbor = random_wall(action, neighbor)
    return action, neighbor


# Removes the edges from a set of actions
def remove_edges_action(position, actions: set, x_dim, y_dim):
    x, y = position
    if x == 0:
        actions.discard(0)
    elif x == x_dim-1:
        actions.discard(2)
    if y == 0:
        actions.discard(3)
    elif y == y_dim-1:
        actions.discard(1)
    return actions


# Create walls in the environment, removing random actions
def random_wall(action, neighbor):
    p = np.random.uniform(0, 10)
    if p > 1:
        return action, neighbor
    if p < 0.25:
        action.discard(0)
        if 0 in neighbor:
            neighbor[0].discard(2)
    elif p < 0.5:
        action.discard(1)
        if 1 in neighbor:
            neighbor[1].discard(3)
    elif p < 0.75:
        action.discard(2)
        if 2 in neighbor:
            neighbor[2].discard(0)
    else:
        action.discard(3)
        if 3 in neighbor:
            neighbor[3].discard(1)
    return action, neighbor


# Eg (up, left) => "1001"; (goal) => "4444"
def action_to_str(action):
    result = '1' if 0 in action else '0'
    result += '1' if 1 in action else '0'
    result += '1' if 2 in action else '0'
    result += '1' if 3 in action else '0'
    if 4 in action:
        result = '4444'
    return result


# Make each action's neighbors consistent with the actions matrix
def update_neighbors(x, y, actions, neighbors):
    for key in neighbors:
        if key == 0:
            actions[x-1, y] = neighbors[key]
        elif key == 1:
            actions[x, y+1] = neighbors[key]
        elif key == 2:
            actions[x+1, y] = neighbors[key]
        elif key == 3:
            actions[x, y-1] = neighbors[key]
    return actions