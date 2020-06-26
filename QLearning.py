import random
import numpy as np
from itertools import count
INITIAL_STATE = 0


class Agent:
    def __init__(self, env, discount):
        self.env = env
        self.Q = np.array([{a: 0 for a in env.get_actions(s)[0]} for s in env.get_states()])
        self.discount = discount

    def _qlearning(self, exploit, random_start):
        state = self.env.random_state() if random_start else INITIAL_STATE
        done = False
        while not done:
            actions, done = self.env.get_actions(state)
            exp = np.random.uniform(0, 1)
            action = argmax_dict(self.Q[state]) if exp < exploit else random_action(actions)
            new_state = self.env.execute(state, action)
            reward = self.env.reward(new_state)
            self.Q[state][action] = reward + self.discount * np.max([self.Q[new_state][a] for a in self.Q[new_state]])
            state = new_state

    def learn(self, epochs, exploit, random_start=False):
        for x in range(epochs):
            self._qlearning(exploit, random_start)

    def policy(self):
        return np.array([argmax_dict(actions) for actions in self.Q]).reshape(self.env.shape())


# Extract a random action from an action container
def random_action(actions):
    return random.sample(actions, 1)[0]


def argmax_dict(d):
    try:
        res = [x for x, v in d.items() if v == max(d.values())][0]
    except IndexError:
        res = []
    return res
