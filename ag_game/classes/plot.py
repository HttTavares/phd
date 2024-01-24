class Plot(dict):
    def __init__(self, metadata):
        for key, value in metadata.items():
            setattr(self, key, value)

    def get_state( self ):
        f"""
        gets the resource state of this crop
        """
        pass
