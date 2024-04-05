class Resource(dict):
    def __init__(self, metadata):
        for key, value in metadata.items():
            setattr(self, key, value)

    def state_action_state( self ):
        pass
    

    def perform_effect( self, resource_quantity, crop ):
        f"""
        changes crop, plot attributes based on self.effects
        iterates through the dict self.effect, key is attribute name and value is quantity
        """
        for attribute in self.effect:
            crop.change_attribute( 
                name = self.name, 
                quantity = self.effect[attribute]*resource_quantity, 
                distribution = self.distribution[attribute](resource_quantity)
                # should resource_effect_distribution be a function? 
                # I think yes, it's more scalable and flexible.
                # but for that i have to abstract distribution function creation. 
                # a function factory with parameters: dist_type, parameters.
            )
        
        
