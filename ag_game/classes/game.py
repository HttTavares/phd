import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset


class Game(dict):
    def __init__(self, metadata):
        for key, value in metadata.items():
            setattr(self, key, value)

    def run(self):
        self.initialize()
        # for tick in range(self.time_limit):
        #             self.step()
        print(self.agents.objects)
        print(self.plots.objects)
        print(self.crops.objects)
        print(self.resources.objects)

    def initialize(self):
        self.agents = self.world.objects["Category"](type="Agent")
        self.plots = self.world.objects["Category"](type="Plot")
        self.crops = self.world.objects["Category"](type="Crop")
        self.resources = self.world.objects["Category"](type="Resource")
        for resource_data in self.world.data["Resource Initialization Data"].values():
            resource = self.world.create_object(
                type="Resource", name=resource_data["name"], cost=resource_data["cost"]
            )
            self.resources.objects[resource.id] = resource
        for position in range(self.number_of_plots):
            plot = self.world.create_object(
                type="Plot", position=position, health=5, cultivar="Potato"
            )
            self.plots.objects[plot.id] = plot
            crop = self.world.create_object(type="Crop", health=5, growth=0, price=25)
            self.crops.objects[crop.id] = crop
            plot.crop = crop
            crop.plot = plot
            crop.necessities = {"Water": 3}
            crop.deficit = {"Water": 0}
            crop.quality = 1
            crop.resources = {"Water": 0, "Pesticide": 0}

        for player_number in range(self.number_of_players):
            agent = self.world.create_object(
                type="Agent", number=player_number, money=1000
            )
            agent.game = self
            agent.plots = self.world.objects["Category"](type="Plot")
            self.agents.objects[agent.id] = agent
            for agent in self.agents:
                for plot in self.plots:
                    agent.plots.objects[plot.id] = plot
                agent.receive_plots(self.plots.objects)

    def change_crop_health(self, crop, quantity):
        crop.change_health(quantity)

    def effect_pesticide(self, crop):
        crop.change_health(1)

    def effect_booster(self, crop):
        if self.world.random.randint(1, 100) < 30:
            crop.change_quality(1)

    def step(self):
        # water = list(self.resources.objects.values())[0]  # FIND PLACE FOR THIS
        # pesticide = list(self.resources.objects.values())[1]  # FIND PLACE FOR THIS
        # pesticide.effect = self.effect_pesticide
        for agent in self.agents:
            action = agent.figure_out_decision()
            real_action = torch.round(action * 100)
            print(action)
            print(real_action)
            for index in range(len(agent.action_vector_meaning)):
                combination = agent.action_vector_meaning[index]
                # for combination in agent.action_vector_meaning:
                plot = combination[0]
                resource = combination[1]
                plot.crop.apply_resource(resource, real_action[index])
                plot.crop.grow_crop()
                # if plot.crop.health < 3:
                #     plot.crop.apply_resource(pesticide, 1)
