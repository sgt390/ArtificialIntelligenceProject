from QLearning import Agent
from environment import Environment
from graph import connected_components
from tqdm import tqdm
from graphics import draw


# env.print_rewards()
height = 6
width = 7

epochs = [1]
random_start = [True, True, True, True]
components = {}

for epoch, rs in zip(epochs, random_start):
    components[f'epochs:{epoch}-randstart:{rs}'] = []
    exploit = 0
    for _ in tqdm(range(5)):
        env = Environment(height, width)
        agent = Agent(env=env, gamma=0.9)
        agent.learn(epochs=epoch, exploit=exploit,  random_start=rs)
        policy = agent.policy()
        components[f'epochs:{epoch}-randstart:{rs}'].append(connected_components(policy))


for i in components:
    comp = components[i]
    print(f'{i}: {comp}')
    print(f'average:{sum(comp)/len(comp)}\n')

# draw last policy
draw(env, policy)
