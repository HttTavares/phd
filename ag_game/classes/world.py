import random 

try:
    from classes.agent import Agent 
    from classes.category import Category 
    from classes.crop import Crop 
    from classes.game import Game 
    from classes.gameresource import Resource 
    from classes.history import History 
    from classes.plot import Plot 
    from classes.state import State 
    from classes.utils import Utils 
except:
    from agent import Agent 
    from category import Category 
    from crop import Crop 
    from game import Game 
    from gameresource import Resource 
    from history import History 
    from plot import Plot 
    from state import State 
    from utils import Utils 



class World(dict):
    def __init__(self, metadata):
        for key, value in metadata.items():
            setattr(self, key, value)
        self.utils = Utils()
        self.objects = {
            ### PLACE EVERY CLASS HERE LIKE SO:
            # 'ClassName': class,
            'Game': Game,
            'Plot': Plot,
            'Agent': Agent,
            'Crop': Crop,
            'Game': Game,
            'Resource': Resource,
            'State': State,
            'Category': Category,
        }
        self.categories = Category( type = 'Category' ) 
        self.data = {

            'Resource Initialization Data': {

                'Water': {
                    'name': 'Water',
                    'cost': 1,
                },
                'Pesticide': {
                    'name': 'Pesticide',
                    'cost': 10,
                },
                'Herbicide': {
                    'name': 'Herbicide',
                    'cost': 10,
                },
                'Booster': {
                    'name': 'Booster',
                    'cost': 5,
                },

            }

        }
        self.random = random

    def make_object_metadata( self, object ):
        object.world = self
        object.id = self.utils.generate_random_id()
        object.state = State( {'object': object} )
        # object.type = metadata['type']

    def run( self ):
        for object_type in self.objects:
            self.categories[object_type] = Category( object_type = object_type )
        game = self.create_object(type = 'Game', number_of_players = 1, number_of_plots = 5, time_limit = 30)
        self.game = game
        game.run()


    def create_object( self, **metadata ):
        object = self.objects[metadata['type']](metadata)
        self.make_object_metadata( object )
        self.categories[object.type][object.id] = object

        return object

    # def read_object( self, object_id ):
    #     object = None
    #     for object_type in self.topos:
    #         if object_id in self.topos[object_type]:
    #             object = self.topos[object_type][object_id]
    #     if object == None:
    #         print('read_object method returned None')
    #     return object

    def show_object( self, object_id ):
        print()
        object_data = self.vniversvs.read_object( object_id ).via.get_current_data()
        print('basic data for', object_data['basic']['name'])
        for key in object_data['basic']:
            print(key, object_data['basic'][key])
        print()
        print('advanced data for', object_data['basic']['name'])
        for key in object_data['advanced']:
            print(key, object_data['advanced'][key])
        print()


    def read_object():
        pass

    def update_object():
        pass

    def delete_object():
        pass



