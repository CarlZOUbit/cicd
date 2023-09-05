import wandb

print(f'the version of wandb is: {wandb.__version__}')

assert wandb.__version__ == '0.15.9',f'Expected version 0.15.9,but got {wandb.__version__}'
