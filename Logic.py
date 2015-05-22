import random

class Logic(object):
    """docstring for Logic"""
    def __init__(self):
        print("Init Logic")
        self.dict_objects = {} # dict to store tower list, mob list, etc
        self.dict_objects['towers'] = []
        self.dict_objects['mobs'] = []
        self.dict_objects['bullets'] = []
        # Map Matrix containing Tiles (own class) with attributes like texture, towerBuildable, etc
        # self.dict_objects['map'] = [[0 for x in range(5)] for x in range(5)]

    def getDictObjects(self):
        return self.dict_objects

    def update(self, dt):
        for index, mob in enumerate(self.dict_objects['mobs']):
            x = (mob[0] + int(dt * 60)) % 500
            y = (mob[1] - int(dt * 60)) % 400
            self.dict_objects['mobs'][index] = (x, y)


        print(self.dict_objects)
        print(len(self.dict_objects['mobs']))

    def placeTower(self, x, y):
        if((x, y) not in self.dict_objects['towers']):
            self.dict_objects['towers'].append((x, y))
            # later
            # newTower = Tower("Type A", x, y)
            # self.dict_objects['towers'].append(newTower)
            print("T %s" %self.dict_objects['towers'])

    def placeMob(self, x, y):
        self.dict_objects['mobs'].append((x, y))
        print("M %s" %self.dict_objects['towers'])