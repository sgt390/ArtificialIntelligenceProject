from QLearning import Agent
from environment import Environment
from graph import connected_components
from tqdm import tqdm
from graphics import draw


# env.print_rewards()
height = 30
width = 40

epochs = [256]
random_start = [True]
repetitions = 1

components = {}

for epoch, rs in zip(epochs, random_start):
    components[f'epochs:{epoch}-randstart:{rs}'] = []
    exploit = 0.05
    for _ in tqdm(range(repetitions)):  # execute the algorithm multiple times just for experimenting it
        env = Environment(height, width)
        agent = Agent(env=env, discount=0.9)
        agent.learn(epochs=epoch, exploit=exploit,  random_start=rs)
        policy = agent.policy()
        components[f'epochs:{epoch}-randstart:{rs}'].append(connected_components(policy))


for i in components:
    comp = components[i]
    print(f'{i}: {comp}')
    print(f'average:{sum(comp)/len(comp)}\n')

# draw last policy
draw(env, policy)
