import numpy as np


INITIAL_STATE = 0


class AgentQ:
    def __init__(self, env, gamma):
        self.env = env
        self.Q = np.array([{a: 0 for a in env.get_actions(s)[0]} for s in env.get_states()])
        self.gamma = gamma

    def qlearning(self, exploit):
        state = INITIAL_STATE
        while True:
            actions, over = self.env.get_actions(state)
            if over:
                break
            action = argmax_dict(self.Q[state]) if exploit else random_action(actions)
            new_state = self.env.execute(state, action)
            reward = self.env.reward(new_state)
            self.Q[state][action] = reward + self.gamma * np.max([self.Q[new_state][a] for a in self.Q[new_state]])
            state = new_state

    def learn(self, epochs, swap):
        exploit = False
        for x in range(epochs):
            if x == swap:
                exploit = True
            self.qlearning(exploit)

    def policy(self):
        return np.array([argmax_dict(actions) for actions in self.Q]).reshape(self.env.shape())


def random_action(actions):
    return actions[np.random.randint(actions.size)]


def argmax_dict(d):
    return [x for x, v in d.items() if v == max(d.values())][0]
