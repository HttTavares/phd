import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset


class NN(nn.Module):
    def __init__(self, state_size, action_size):
        super(NN, self).__init__()
        self.fc1 = nn.Linear(state_size, 24)
        self.fc2 = nn.Linear(24, 24)
        self.fc3 = nn.Linear(24, action_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    # # Assuming state_data and actions are your features and labels, respectively
    # # Convert data to torch tensors
    # features = torch.tensor(state_data, dtype=torch.float32)
    # labels = torch.tensor(actions, dtype=torch.float32)  # Adjust dtype if actions are categorical

    # # Create dataset and dataloader for batching
    # dataset = TensorDataset(features, labels)
    # dataloader = DataLoader(dataset, batch_size=64, shuffle=True)

    # # Instantiate the neural network
    # model = NN(state_size=features.shape[1], action_size=labels.shape[1])

    # # Define loss function and optimizer
    # loss_fn = nn.MSELoss()  # Or nn.CrossEntropyLoss() for classification
    # optimizer = optim.Adam(model.parameters(), lr=0.001)

    # # Training loop
    # for epoch in range(num_epochs):
    #     for batch_features, batch_labels in dataloader:
    #         # Forward pass
    #         predictions = model(batch_features)
    #         loss = loss_fn(predictions, batch_labels)

    #         # Backward pass and optimize
    #         optimizer.zero_grad()
    #         loss.backward()
    #         optimizer.step()

    #     print(f"Epoch {epoch+1}, Loss: {loss.item()}")


class Agent(dict):
    def __init__(self, metadata):
        for key, value in metadata.items():
            setattr(self, key, value)
        self.max_money = 10000
        # self.plots = {}

    def initialize_nn(self):
        self.update_state()
        state_data = self.get_state_data()
        actions = []
        for resource in self.game.resources:
            for plot in self.plots:
                actions.append(1)
        self.nn = NN(state_size=len(state_data), action_size=len(actions))
        self.optimizer = optim.Adam(self.nn.parameters(), lr=0.001)

    def receive_plots(self, plots):
        f"""
        wrapper to set owner property of given plots as self
        """
        for id, plot in plots.items():
            plot.owner = self
            # self.plots[id] = plot
            plot.player = self

    def update_state(self):
        f"""
        gets the resource state of every owned plot and crop
        """
        # self.state =
        # ret = {"crops": {}, "plots": {}, "agent": {}, "weather": {}, "market": {}}
        self.state = {
            "crops": {},
            "plots": {},
            "agent": {},
            "weather": {},
            "market": {},
        }
        for plot in self.plots:
            self.state["plots"][plot.id] = plot.get_state()
            self.state["crops"][plot.crop.id] = plot.crop.get_state()
        self.state["agent"]["money"] = self.money
        return self.state

    def use_nn(self):
        f"""
        uses agent's NN in order to decide resource usage
        """
        self.state_space = []
        self.update_state()
        for thing in self.plots:
            for thing2 in thing.state:
                self.state_space.append(thing2)
                print(thing)
            for thing3 in thing.crop.state:
                self.state_space.append(thing3)
        # return self.nn(self.get_state())

    def make_decision(self):
        f"""
        exports the decision given by the nn for the game to apply the resources.
        """
        pass

    def get_state_data(self):
        ret = [self.money / self.max_money]
        for plot in self.plots:
            for parameter in plot.get_state().values():
                ret.append(parameter)
            for parameter in plot.crop.get_state().values():
                ret.append(parameter)
        return ret
