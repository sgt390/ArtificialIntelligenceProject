from QLearning import AgentQ
from enviromentQ import EnviromentQ


env = EnviromentQ(20, 20)
env.print()

agent = AgentQ(env, 0.9)

agent.learn(epochs=100, swap=30)
print(agent.policy())
