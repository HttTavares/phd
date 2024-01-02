class Crop(dict):
    def __init__(self, metadata):
        for key, value in metadata.items():
            setattr(self, key, value)

    def grow_crop( self ):
        if self.growth == 10:
            self.collect()
        else:
            self.growth += 1

    def collect( self ):
        self.plot.owner.money += self.price
        self.growth = 0
        self.plot.health = self.plot.health - 1

