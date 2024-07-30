# menu.py in src/scenes
import os
import pyglet
from pyglet.window import key, mouse
from src.scenes.game import GameScene  # Make sure GameScene is properly imported


class MainMenu:
    def __init__(self, window, switch_scene_callback):
        self.window = window
        self.switch_scene_callback = switch_scene_callback

        script_dir = os.path.dirname(__file__)
        assets_dir = os.path.join(script_dir, '../../assets/images')

        # Load background image using the full path
        background_image_path = os.path.join(assets_dir, 'Background.png')
        self.background_image = pyglet.image.load(background_image_path)
        self.background_sprite = pyglet.sprite.Sprite(self.background_image)

        self.background_sprite.scale = max(window.width / self.background_image.width,
                                           window.height / self.background_image.height)

        self.labels = {
            'play': pyglet.text.Label('Play', font_name='Times New Roman', font_size=36,
                                      x=self.window.width // 2, y=self.window.height // 2 + 60,
                                      anchor_x='center', anchor_y='center'),
            'options': pyglet.text.Label('Options', font_name='Times New Roman', font_size=36,
                                         x=self.window.width // 2, y=self.window.height // 2,
                                         anchor_x='center', anchor_y='center'),
            'exit': pyglet.text.Label('Exit', font_name='Times New Roman', font_size=36,
                                      x=self.window.width // 2, y=self.window.height // 2 - 60,
                                      anchor_x='center', anchor_y='center')
        }

    def on_draw(self):
        self.window.clear()
        self.background_sprite.draw()
        for label in self.labels.values():
            label.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            for name, label in self.labels.items():
                if (label.x - label.content_width // 2 <= x <= label.x + label.content_width // 2 and
                        label.y - label.content_height // 2 <= y <= label.y + label.content_height // 2):
                    if name == 'play':
                        self.switch_scene_callback(GameScene)  # Pass the GameScene class
                    elif name == 'options':
                        # Options logic here
                        pass
                    elif name == 'exit':
                        self.window.close()
