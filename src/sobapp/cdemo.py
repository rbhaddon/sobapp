import cocos
from cocos.director import director
import pyglet
from pyglet.gl import (glPushMatrix, glPopMatrix)


class KeyboardLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super().__init__()

        label = cocos.text.Label(
            'Hello, world',
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center', anchor_y='center'
        )
        label.position = 640, 400
        self.add(label)

        self.text = cocos.text.Label("", x=100, y=280)

        # To keep track of which keys are pressed:
        self.keys_pressed = set()
        self.update_text()
        self.add(self.text)

    def update_text(self):
        key_names = [pyglet.window.key.symbol_string(k) for k in self.keys_pressed]
        text = 'Keys: '+','.join(key_names)
        # Update self.text
        self.text.element.text = text

    def on_key_press(self, key, modifiers):
        """This function is called when a key is pressed.
        'key' is a constant indicating which key was pressed.
        'modifiers' is a bitwise or of several constants indicating which
            modifiers are active at the time of the press (ctrl, shift, capslock, etc.)
        """

        self.keys_pressed.add(key)
        self.update_text()

    def on_key_release(self, key, modifiers):
        """This function is called when a key is released.

        'key' is a constant indicating which key was pressed.
        'modifiers' is a bitwise or of several constants indicating which
            modifiers are active at the time of the press (ctrl, shift, capslock, etc.)

        Constants are the ones from pyglet.window.key
        """

        self.keys_pressed.remove(key)
        self.update_text()

    def on_mouse_press(self, x, y, buttons, modifiers):
        """This function is called when any mouse button is pressed

        (x, y) are the physical coordinates of the mouse
        'buttons' is a bitwise or of pyglet.window.mouse constants LEFT, MIDDLE, RIGHT
        'modifiers' is a bitwise or of pyglet.window.key modifier constants
           (values like 'SHIFT', 'OPTION', 'ALT')
        """
        x, y = director.get_virtual_coordinates(x, y)
        print('KeyboardLayer:', (x, y))


class MouseDisplay(cocos.layer.Layer):

    is_event_handler = True     #: enable director.window events

    def __init__(self, background):
        super().__init__()
        self.background = background

        self.posx = 100
        self.posy = 240
        self.text = cocos.text.Label('No mouse events yet', font_size=18, x=self.posx, y=self.posy)
        self.add(self.text)

    def update_text(self, x, y):
        text = 'Mouse @ %d,%d' % (x, y)
        self.text.element.text = text
        self.text.element.x = self.posx
        self.text.element.y = self.posy

    def on_mouse_motion(self, x, y, dx, dy):
        """Called when the mouse moves over the app window with no button pressed

        (x, y) are the physical coordinates of the mouse
        (dx, dy) is the distance vector covered by the mouse pointer since the
          last call.
        """
        self.update_text(x, y)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        """Called when the mouse moves over the app window with some button(s) pressed

        (x, y) are the physical coordinates of the mouse
        (dx, dy) is the distance vector covered by the mouse pointer since the
          last call.
        'buttons' is a bitwise or of pyglet.window.mouse constants LEFT, MIDDLE, RIGHT
        'modifiers' is a bitwise or of pyglet.window.key modifier constants
           (values like 'SHIFT', 'OPTION', 'ALT')
        """
        self.update_text(x, y)

    def on_mouse_press(self, x, y, buttons, modifiers):
        """This function is called when any mouse button is pressed

        (x, y) are the physical coordinates of the mouse
        'buttons' is a bitwise or of pyglet.window.mouse constants LEFT, MIDDLE, RIGHT
        'modifiers' is a bitwise or of pyglet.window.key modifier constants
           (values like 'SHIFT', 'OPTION', 'ALT')
        """
        self.posx, self.posy = director.get_virtual_coordinates(x, y)
        self.update_text(x, y)
        # print(self.background.sprite.contains(x, y))


def glpushpop(func):
    def wrapper(instance):
        glPushMatrix()
        func(instance)
        glPopMatrix()
    return wrapper


class Background(cocos.layer.Layer):
    is_event_handler = False     #: enable director.window events

    def __init__(self):
        super().__init__()
        # self.img = pyglet.resource.image('assets/dummy_map.tmx')
        sprite = cocos.sprite.Sprite('world_default.png')
        #sprite = cocos.sprite.Sprite('assets/world_default_high.jpg')
        #sprite = cocos.sprite.Sprite('dummy_map.png')
        wsize = director.get_window_size()
        sprite.position = wsize[0] / 2, wsize[1] / 2
        sprite.scale_x = wsize[0] / sprite.width
        sprite.scale_y = wsize[1] / sprite.height
        # sprite.scale_x = self.scale_x
        # sprite.scale_y = self.scale_y
        self.add(sprite, z=1)

    def on_enter(self):
        print('Background becoming active')

    def on_exit(self):
        print('Background becoming inactive')


    # @glpushpop
    # def draw(self):
    #     #glPushMatrix()
    #     self.transform()
    #     self.img.blit(0, 0)
    #     #glPopMatrix()


def main():
    global scroller, old_ij, old_cell, old_highlighted_color
    director.init(
        width=1280,
        height=800,
        caption="Eat Shit",
        fullscreen=True,
        autoscale=False,
    )
    print('[x]', director.get_window_size())
    print('[x]', director.window)

    # scene = cocos.scene.Scene()
    #background = Background()
    scroller = cocos.layer.ScrollingManager()
    #map_resource = cocos.tiles.load('world_ortho.tmx')
    #map_resource = cocos.tiles.load('world_hex.tmx')
    map_resource = cocos.tiles.load('large_hex.tmx')
    #map_resource = cocos.tiles.load('hexmap.tmx')
    map_layer = map_resource['hex_layer']
    #map_layer = map_resource['world']
    scroller.add(map_layer)
    #scene = cocos.scene.Scene(scroller)
    scene = cocos.scene.Scene()
    #scene.add(background, z=0)
    scene.add(scroller, z=1)
    #scene.add(MouseDisplay(background), z=2)
    #scene.add(KeyboardLayer(), z=3)

    old_ij = 'nonexist'
    old_highlighted_color = None
    old_cell = None

    def on_mouse_motion(x, y, dx, dy ):
        global scroller, old_ij, old_cell, old_highlighted_color
        #vh, vy = director.get_virtual_coordinates(x, y)
        vx, vy = scroller.pixel_from_screen(x,y)
        ij = map_layer.get_key_at_pixel(vx, vy)
        if ij == old_ij:
            return
        # restore color
        if old_cell:
            p, q = old_ij
            if old_highlighted_color is None:
                map_layer.set_cell_color(p, q, (255, 255, 255))
                del old_cell.properties['color4']
            else:
                map_layer.set_cell_color(p, q, old_highlighted_color[:3])

        # record info and set color
        old_ij = ij
        i, j = ij
        print(i,j)
        old_cell = map_layer.get_cell(i, j)
        if old_cell is None:
            return
        old_highlighted_color = old_cell.properties.get('color4', None)
        map_layer.set_cell_color(i, j, (255, 0, 0))

    director.window.push_handlers(on_mouse_motion)

    director.run(scene)


if __name__ == '__main__':
    main()
