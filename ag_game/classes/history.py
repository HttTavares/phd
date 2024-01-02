class History(dict):
    f"""
        Class to store the metadata of every object instance
        There is one "mega" history in World, and this mega history has one history for each object. ??
    """
    def __init__(self, metadata):
        for key, value in metadata.items():
            setattr(self, key, value)
