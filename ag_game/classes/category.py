class Category(dict):
    f"""
        How to implement category class?
        This is supposed to help deal with objects instances as a mathematical category.
    """
    def __init__( self, **kwargs ):
        for key in kwargs.keys():
            self[key] = kwargs[key]
        self.objects = {}

    def __iter__(self):
        return iter(self.objects.values())