# window.py in src/game_engine
import pyglet
from src.scenes.menu import MainMenu

class Window(pyglet.window.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.current_scene = MainMenu(self, self.switch_scene)
        pyglet.clock.schedule_interval(self.update, 1/60.0)

    def switch_scene(self, new_scene_class):
        print("Switching scene")
        self.current_scene = new_scene_class(self)

    def on_draw(self):
        self.clear()
        if self.current_scene:
            self.current_scene.on_draw()

    def on_mouse_press(self, x, y, button, modifiers):
        print("Window mouse press detected")
        self.current_scene.on_mouse_press(x, y, button, modifiers)

    def update(self, dt):
        if hasattr(self.current_scene, 'update'):
            self.current_scene.update(dt)
