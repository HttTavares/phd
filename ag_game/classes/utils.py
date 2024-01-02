import random

class Utils(dict):
    def __init__( self, **kwargs ):
        for key in kwargs.keys():
            self[key] = kwargs[key]
        self.symbols = 'qwertyuiopasdfghjklçzxcvbnmQWERTYUIOPASDFGHJKLÇZXCVBNM1234567890-=!@#$%*()\|_+`^:?'

    def generate_random_id( self, size = 20 ):
        ret = ''
        for i in range(size):
            ret += random.choice(self.symbols)  
        return ret
    

