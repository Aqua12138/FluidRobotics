import gym
from gym import register

for env_name in ['LatteArt', 'LatteArtStir', 'Scooping', 'Gathering', 'GatheringO', 'IceCream', 'IceCreamSimple', 'Transporting', 'Stabilizing', 'Pouring', 'Circulation', 'Mixing', 'Showcase', 'RLTest', 'AAA']:
    for id in range(1):
        register(
            id = f'{env_name}-v{id}',
            entry_point=f'fluidlab.envs.{env_name.lower()}_env:{env_name}Env',
            kwargs={'version': id, 'loss_type': 'default'},
            max_episode_steps=10000
        )

for env_name in ['DemoSmoke', 'DemoSmoke2', 'DemoRigid', 'DemoElastic', 'DemoPlastic', 'DemoInviscid', 'DemoViscous', 'DemoLiquid']:
    for id in range(1):
        register(
            id = f'{env_name}-v{id}',
            entry_point=f'fluidlab.envs.{env_name.lower()}_env:{env_name}Env',
            kwargs={'version': id, 'loss_type': 'default'},
            max_episode_steps=10000
        )
