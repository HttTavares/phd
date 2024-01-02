class State(dict):
    def __init__( self, **kwargs ):
        for key in kwargs.keys():
            self[key] = kwargs[key]
