import numpy as np
from numpy.random import randint
from actions import make_actions, action_to_str

EMPTY = -0.01
GOAL = 1
"""
ACTIONS:
    up: 0
    right: 1
    down: 2
    left: 3
    stay: 4
"""

class Environment:
    def __init__(self, x=5, y=5):
        self.x_goal = randint(x)
        self.y_goal = randint(y)
        self.rewards: np.array = _make_rewards(x, y, self.x_goal, self.y_goal)
        self.actions = make_actions(self.x(), self.y(), (self.x_goal, self.y_goal))

    def print_rewards(self):
        print(self.rewards.view(dtype=float))

    def x(self):
        return np.size(self.rewards, 0)

    def y(self):
        return np.size(self.rewards, 1)

    # Encode each position (pair of row, column) into a number
    def get_states(self):
        return range(self.x() * self.y())

    def random_state(self):
        return np.random.randint(0, self.x()*self.y(), dtype=int)

    def shape(self):
        return self.rewards.shape

    def get_actions(self, state) -> (set, bool):
        position = self.__decode(state)
        actions = self.actions[position]
        done = 4 in actions or not len(actions)
        return actions, done

    def reward(self, state):
        return self.rewards[self.__decode(state)]

    # list index (state) to matrix index (position)
    def __decode(self, state):
        return int(state/self.y()), state % self.y()

    # execute an action in a state
    def execute(self, state, action):
        x, y = self.__decode(state)
        if action == 0:
            x = x - 1
        elif action == 1:
            y = y + 1
        elif action == 2:
            x = x + 1
        elif action == 3:
            y = y - 1
        return x*(self.y()) + y


def _make_rewards(x, y, x_goal, y_goal):
    rewards = np.reshape(np.repeat(EMPTY, x*y), (x, y))
    rewards = _set_goal(rewards, x_goal, y_goal)
    return rewards


def _set_goal(rewards, x_goal, y_goal):
    rewards[x_goal, y_goal] = GOAL
    return rewards


