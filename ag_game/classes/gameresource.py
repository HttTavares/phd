class Resource(dict):
    def __init__(self, metadata):
        for key, value in metadata.items():
            setattr(self, key, value)

    # def perform_effect( self ):
    #     self.eff

