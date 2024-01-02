class Agent(dict):
    def __init__(self, metadata):
        for key, value in metadata.items():
            setattr(self, key, value)
        self.plots = {}
        
    def receive_plots( self, plots ):
        for id, plot in plots.items():
            plot.owner = self
            self.plots[id] = plot
            plot.player = self



