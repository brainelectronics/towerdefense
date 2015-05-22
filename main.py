import pyglet

import Logic
import Gui

class TowerDefense(object):
    """docstring for TowerDefense"""
    def __init__(self):
        print("Init")
        self.targetFPS = 60
        self.logic = Logic.Logic()
        self.gui = Gui.Window()
        #self.config = ?

    def main(self):
        print("Main")
        self.gui.setLogic((self.logic))
        #pyglet.clock.schedule_interval(self.update, 1/self.targetFPS)
        pyglet.clock.schedule(self.update)
        pyglet.app.run()

    def update(self, dt):
        print(dt)
        self.logic.update(dt)
        self.gui.redraw()

if __name__ == '__main__':
    towerDefense = TowerDefense()
    towerDefense.main()