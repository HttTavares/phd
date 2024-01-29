class Plot(dict):
    def __init__(self, metadata):
        for key, value in metadata.items():
            setattr(self, key, value)

    def update_state( self ):
        f"""
        updates the resource and intrinsic state of this crop
        """
        self.state.quality = self.quality
        self.state.health = self.health

    def get_state( self ):
        self.update_state()
        return {
            'quality': self.state.quality,
            'health': self.state.health,
        }


