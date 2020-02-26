import numpy as np
from numpy.random import randint


EMPTY = -1
GOAL = 1000
ACTIONS = {
    'up': 0,
    'right': 1,
    'down': 2,
    'left': 3,
    'stay': 4
}


class EnviromentQ:
    def __init__(self, x=5, y=5):
        self.x_goal = randint(x)
        self.y_goal = randint(y)
        self.field: np.array = self.new_world(x, y, self.x_goal, self.y_goal)

    @staticmethod
    def new_world(x, y, x_goal, y_goal):
        """
        The actual world is (x+2, y+2). The added space is
        a wall the agent cannot surpass.
        """
        field = np.reshape(np.repeat(EMPTY, x*y), (x, y))
        field = EnviromentQ.create_goal(field, x_goal, y_goal)
        return field

    """    @staticmethod
        def build_wall(field):
            field = np.array(field)
            field[0] = [WALL for _ in range(np.size(field, 1))]
            field[-1] = [WALL for _ in range(np.size(field, 1))]
            field[:, 0] = [WALL for _ in range(np.size(field, 0))]
            field[:, -1] = [WALL for _ in range(np.size(field, 0))]
            return field.tolist()
    """
    @staticmethod
    def create_goal(field, x_goal, y_goal):
        field[x_goal][y_goal] = GOAL
        return field

    def print(self):
        print(self.field.view(dtype=int))

    def x(self):
        return np.size(self.field, 1)

    def y(self):
        return np.size(self.field, 0)

    def score(self, position):
        return self.field[position]

    def get_states(self):
        return range(self.x() * self.y())

    def shape(self):
        return self.field.shape

    def get_actions(self, state):
        x, y = self.__decode(state)
        if x == self.x_goal and y == self.y_goal:
            return np.array([4]), True
        actions = [0, 1, 2, 3]
        if x == 0:
            actions.remove(0)
        elif x == self.x()-1:
            actions.remove(2)
        if y == 0:
            actions.remove(3)
        elif y == self.y()-1:
            actions.remove(1)
        return np.array(actions), False

    def reward(self, state):
        return self.field[self.__decode(state)]

    def __decode(self, state):
        return int(state/self.y()), state % self.y()

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


