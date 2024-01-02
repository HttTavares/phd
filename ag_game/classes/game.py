class Game(dict):
    def __init__(self, metadata):
        for key, value in metadata.items():
            setattr(self, key, value)

    def run( self ):
        self.initialize()
        for tick in range(self.time_limit):
            self.advance_tick()

    def initialize(self):
        self.agents = self.world.objects['Category']( type = 'Agent')
        self.plots = self.world.objects['Category']( type = 'Plot')
        self.crops = self.world.objects['Category']( type = 'Crop')
        for position in range(self.number_of_plots):
            plot = self.world.create_object( type = 'Plot', position = position , health = 5 )
            self.plots.objects[plot.id] = plot
            crop = self.world.create_object( type = 'Crop', health = 5, growth = 0, price = 25 )
            self.crops.objects[crop.id] = crop
            plot.crop = crop
            crop.plot = plot
        for player_number in range(self.number_of_players):
            agent = self.world.create_object( type = 'Agent', number = player_number, money = 1000 )
            self.agents.objects[agent.id] = agent
            for agent in self.agents:
                agent.receive_plots( self.plots.objects )

    def advance_tick(self):
        for agent in self.agents:
            print('money', agent.money)
            for plot in agent.plots.values():
                plot.crop.grow_crop()
                print('plot', plot.crop.id, 'growth', plot.crop.growth)
            print('money', agent.money)






