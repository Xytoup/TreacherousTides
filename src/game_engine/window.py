# window.py in src/game_engine
import pyglet
from src.scenes.game import GameScene

class Window(pyglet.window.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.current_scene = GameScene(self)

    def on_draw(self):
        self.clear()
        if self.current_scene:
            self.current_scene.on_draw()

    def update(self, dt):
        if hasattr(self.current_scene, 'update'):
            self.current_scene.update(dt)
