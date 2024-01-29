class Crop(dict):
    def __init__(self, metadata):
        for key, value in metadata.items():
            setattr(self, key, value)

    def grow_crop( self ):
        if self.world.random.randint( 1, 100 ) < 20:
            self.change_health( -1 )
        if self.growth == 10:
            self.collect()
        else:
            self.growth += 1
            for resource_name in self.necessities:
                self.deficit[resource_name] += self.necessities[resource_name]
        # self.state.reset() # should i do a reset? 

    def collect( self ):
        self.plot.owner.money += self.price*self.quality*self.health
        self.growth = 0
        self.plot.health = self.plot.health - 1

    def apply_resource( self, resource, quantity ):

        if resource.name in self.deficit:
            self.deficit[resource.name] -= quantity
        self.plot.owner.money -= resource.cost*quantity
        # if not resource.name in self.state:
        #     self.state[resource.name] = 0
        if resource.name == "Booster":
            self.quality += quantity
        # self.state[resource.name] += quantity
        try:
            resource.effect( self )
        except:
            pass

    def change_health( self, quantity ):
        self.health += quantity

    def change_quality( self, quantity):
        self.quality += quantity

    def update_state( self ):
        f"""
        updates the resource and intrinsic state of this crop
        """
        self.state.quality = self.quality
        self.state.health = self.health
        self.state.deficit = self.deficit
        # self.state.queued_resources = self.queued_resources

    def get_state( self ):
        self.update_state()
        return {
            'quality': self.state.quality,
            'health': self.state.health,
            'deficit': self.state.deficit,
        }


