class Resource(dict):
    def __init__(self, metadata):
        for key, value in metadata.items():
            setattr(self, key, value)

    def perform_effect( self, resource_quantity, crop ):
        f"""
        changes crop, plot attributes based on self.effects
        iterates through the dict self.effect, key is attribute name and value is quantity
        """
        for attribute in self.effect:
            crop.change_attribute( name = attribute, quantity = self.effect[attribute]*resource_quantity)
        
        
