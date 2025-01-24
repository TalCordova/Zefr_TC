import torch
import torch.nn as nn
import torch.nn.functional as F

class TinyVGG(nn.Module):
    def __init__(self, input_channels: int, hidden_units: int, output_shape: int = 1):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=input_channels,
                               out_channels=hidden_units,
                               kernel_size=3,
                               stride=1,
                               padding=1)
        self.pool = nn.MaxPool2d(2)
        self.conv2 = nn.Conv2d(in_channels=hidden_units,
                               out_channels=hidden_units,
                               kernel_size=3,
                               stride=1,
                               padding=1)
        self.flatten = nn.Flatten()
        self.linear = nn.Linear(hidden_units * 56 * 56, output_shape)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = self.flatten(x)
        x = self.linear(x)
        return torch.sigmoid(x)