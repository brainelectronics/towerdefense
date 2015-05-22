import pyglet
from pyglet.gl import *
blueDot = pyglet.resource.image('blue-dot.png')
redDot = pyglet.resource.image('red-dot.png')

class Window(pyglet.window.Window):
    """docstring for Window"""
    def __init__(self):
        print("Init Window")
        super(Window, self).__init__(500, 400, vsync=False)
        self.fps_display = pyglet.clock.ClockDisplay()
        self.dict_objects = {}
        redDot.width, redDot.height = 10, 10
        blueDot.width, redDot.height = 10, 10

    def setLogic(self, logic):
        self.logic = logic
        self.dict_objects = self.logic.getDictObjects()

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            super(Window, self).close()
        else:
            print("Key pressed: " + str(symbol))

    def on_mouse_press(self, x, y, button, modifiers):
        # detect where the click goes (tower -> upgrade menu, building place, etc...)
        # maybe a (x,y) grid might be useful instead ob the list so an iteration
        # over the list is unnecessary
        x = int(x / 50) * 50
        y = int(y / 50) * 50
        if button == pyglet.window.mouse.LEFT:
            print("Left click at (" + str(x) + "," + str(y) + ")")
            self.logic.placeTower(x, y)
        elif button == pyglet.window.mouse.RIGHT:
            print("Right click at (" + str(x) + "," + str(y) + ")")
            self.logic.placeMob(x, y)

    def redraw(self):
        super(Window, self).clear()
        self.fps_display.draw()
        # late each Tower or Mob carries its own texture and its won draw method?

        batch = pyglet.graphics.Batch()
        pyglet.gl.glPointSize(3)
        
        for mob in self.dict_objects['mobs']:
            """
            pyglet.text.Label("M", font_size=30,
                              x=(mob[0] + 25), y=(mob[1] + 25),
                              anchor_x='center', anchor_y='center').draw()
            """
            #print("Mob x=%d y=%d" %(mob[0], mob[1]))
            #redDot.blit((mob[0] + 25), (mob[1] + 25))
            vertex_list = batch.add(1, pyglet.gl.GL_POINTS,None,
                ('v2i', (mob[0]+25, mob[1]+25)),
                ('c3B', (0, 255, 0)))

        for tower in self.dict_objects['towers']:
            """
            pyglet.text.Label("T", font_size=30,
                              x=(tower[0] + 25), y=(tower[1] + 25),
                              anchor_x='center', anchor_y='center').draw()
            """
            #print("Tower x=%d %s y=%d %s" 
            #   %(tower[0], type(tower[0]), tower[1], type(tower[1])))
            #blueDot.blit(tower[0], tower[1])
            #redDot.blit(350,200)
            vertex_list = batch.add(1, pyglet.gl.GL_POINTS,None,
                ('v2i', (tower[0]+25, tower[1]+25)),
                ('c3B', (0, 0, 255)))
        batch.draw()

