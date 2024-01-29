class Agent(dict):
    def __init__(self, metadata):
        for key, value in metadata.items():
            setattr(self, key, value)
        self.plots = {}
        

    def receive_plots( self, plots ):
        f"""
        wrapper to set owner property of given plots as self
        """
        for id, plot in plots.items():
            plot.owner = self
            self.plots[id] = plot
            plot.player = self

    def get_state( self ):
        f"""
        gets the resource state of every owned plot and crop
        """
        ret = { 'crops': {}, 'plots': {}, 'agent': {}, 'weather': {}, "market": {} }
        for plot in self.plots:
            ret['plots'][plot.id] = plot.get_state()
            ret['crops'][plot.crop.id] = plot.crop.get_state()
        ret['agent']['money'] = self.money

        return ret

    def use_nn( self ):
        f"""
        uses agent's NN in order to decide resource usage
        """
        return self.nn( self.state() )

    def make_decision( self ):
        f"""
        exports the decision given by the nn for the game to apply the resources.
        """
        pass



