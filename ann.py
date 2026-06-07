# Import Libraries
import torch
import torch.nn as nn
import torch.optim as optim

# create training data
x=torch.tensor([[1000.0],[1200.0],[1500.0],1800.0],[2000.0]])
y=torch.tensor([[20.0],25.0],[30.0],[35.0],[40.0]])

# create neural network
model=nn.sequential(
    nn.Linear(1,4),
    nn.ReLU(),
    nn.Linear(4,1)
)   

