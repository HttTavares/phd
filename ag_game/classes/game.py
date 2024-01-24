class Game(dict):
    def __init__(self, metadata):
        for key, value in metadata.items():
            setattr(self, key, value)


    def run( self ):
        self.initialize()
        for tick in range(self.time_limit):
            self.advance_tick()
        print(self.agents.objects)
        print(self.plots.objects)
        print(self.crops.objects)
        print(self.resources.objects)


    def initialize(self):
        self.agents = self.world.objects['Category']( type = 'Agent')
        self.plots = self.world.objects['Category']( type = 'Plot')
        self.crops = self.world.objects['Category']( type = 'Crop')
        self.resources = self.world.objects['Category']( type = 'Resource')
        for resource_data in self.world.data['Resource Initialization Data'].values():
            resource = self.world.create_object( type = 'Resource', name = resource_data['name'], cost = resource_data['cost'] )
            self.resources.objects[resource.id] = resource
        for position in range(self.number_of_plots):
            plot = self.world.create_object( type = 'Plot', position = position , health = 5, cultivar = 'Potato' )
            self.plots.objects[plot.id] = plot
            crop = self.world.create_object( type = 'Crop', health = 5, growth = 0, price = 25 )
            self.crops.objects[crop.id] = crop
            plot.crop = crop
            crop.plot = plot
            crop.necessities = {
                'Water': 3
            }
            crop.deficit = {
                'Water': 0
            }
            crop.quality = 1

        for player_number in range(self.number_of_players):
            agent = self.world.create_object( type = 'Agent', number = player_number, money = 1000 )
            self.agents.objects[agent.id] = agent
            for agent in self.agents:
                agent.receive_plots( self.plots.objects )

    def change_crop_health( self, crop, quantity ):
        crop.change_health( quantity )

    def effect_pesticide( self, crop ):
        crop.change_health( 1 )

    def effect_booster( self, crop ):
        if self.world.random.randint( 1, 100 ) < 30:
            crop.change_quality( 1 )

    def advance_tick(self):
        water = list(self.resources.objects.values())[0] # FIND PLACE FOR THIS
        pesticide = list(self.resources.objects.values())[1] # FIND PLACE FOR THIS
        pesticide.effect = self.effect_pesticide
        for agent in self.agents:
            for plot in agent.plots.values():
                plot.crop.apply_resource( water, 3 )
                plot.crop.grow_crop()
                if plot.crop.health < 3:
                    plot.crop.apply_resource( pesticide, 1 )
                






