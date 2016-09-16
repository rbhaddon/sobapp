import cocos
from cocos.director import director
import pyglet
from pyglet.gl import (glPushMatrix, glPopMatrix)


class Background(cocos.layer.ScrollableLayer):
    is_event_handler = False     #: enable director.window events

    def __init__(self):
        super().__init__()
        sprite = cocos.sprite.Sprite('world_default.png')
        self.add(sprite)


class Hexagons(cocos.layer.ScrollableLayer):
    is_event_handler = False     #: enable director.window events

    def __init__(self):
        super().__init__()
        hex_resource = cocos.tiles.load('large_hex.tmx')
        hex_layer = hex_resource['hex_layer']
        self.add(hex_layer)


class Scroller(cocos.layer.ScrollingManager):
    is_event_handler = True     #: enable director.window events

    def __init__(self):
        super().__init__()
        self._background_layer = None
        self._tile_layer = None
        self._old_ij = 'Non-existent'
        self._old_cell = None
        self._old_hl_color = None

    def on_mouse_motion(self, x, y, dx, dy):
        """Called when the mouse moves over the app window with no button pressed

        (x, y) are the physical coordinates of the mouse
        (dx, dy) is the distance vector covered by the mouse pointer since the
          last call.
        """
        print('Scroller mouse:', x, y)
        if self._tile_layer is None:
            return

        # vx, vy = director.get_virtual_coordinates(x, y)
        vx, vy = self.screen_to_world(x, y)
        ij = self.tile_layer.get_key_at_pixel(vx, vy)
        if ij == self._old_ij:
            return
        # restore color
        if self._old_cell is not None:
            p, q = self._old_ij
            if self._old_hl_color is None:
                self.tile_layer.set_cell_color(p, q, (255, 255, 255))
                del self._old_cell.properties['color4']
            else:
                self.tile_layer.set_cell_color(p, q, self._old_hl_color[:3])

        # record info and set color
        self._old_ij = ij
        i, j = ij
        print(i, j)
        self._old_cell = self.tile_layer.get_cell(i, j)
        if self._old_cell is None:
            return
        self._old_hl_color = self._old_cell.properties.get('color4', None)
        self.tile_layer.set_cell_color(i, j, (255, 0, 0))

    def on_key_press(self, key, modifiers):
        print('Scroller key:', key)
        if key == pyglet.window.key.Z:
            if self.scale == .24:
                self.do(cocos.actions.ScaleTo(1, 0.5))
            else:
                self.do(cocos.actions.ScaleTo(.24, 0.5))
        elif key == pyglet.window.key.D:
            print('Scroller: debug')
            # [child.set_debug(True) for child in self.get_children()]
        elif key == pyglet.window.key.Q:
            print('Scroller: q')

    @property
    def background_layer(self):
        return self._background_layer

    @background_layer.setter
    def background_layer(self, layer):
        if self._background_layer is not None:
            # FIXME delete it
            pass
        else:
            self._background_layer = layer
            self.add(layer, z=0)

    @property
    def tile_layer(self):
        return self._tile_layer

    @tile_layer.setter
    def tile_layer(self, layer):
        if self._tile_layer is not None:
            # FIXME delete it
            pass
        else:
            self._tile_layer = layer
            self.add(layer, z=1)


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
    scroller = Scroller()
    background = Background()
    #hexagons = Hexagons()
    #hex_resource = cocos.tiles.load('large_hex.tmx')
    hex_resource = cocos.tiles.load('hexmap.tmx')
    #hexagons = hex_resource['hex_layer']
    hexagons = hex_resource['tile_layer_1']
    #scroller.background_layer = background
    scroller.tile_layer = hexagons
    scene = cocos.scene.Scene()
    scene.add(scroller)
    #scene.add(KeyboardLayer(), z=3)

    director.run(scene)


if __name__ == '__main__':
    main()
