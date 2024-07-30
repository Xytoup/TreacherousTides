# game.py in src/scenes
import pyglet
import os
from src.game_engine.player import Player


class GameScene:
    def __init__(self, window):
        print("Initializing GameScene")
        self.window = window
        self.player = Player()
        self.keys = pyglet.window.key.KeyStateHandler()
        self.window.push_handlers(self.keys)
        print("GameScene initialized")

        # Load sea texture
        script_dir = os.path.dirname(__file__)
        assets_dir = os.path.join(script_dir, '../../assets/images')
        sea_texture_path = os.path.join(assets_dir, 'tex_Water.jpg')
        self.sea_texture = pyglet.image.load(sea_texture_path)

    def on_draw(self):
        self.window.clear()
        self.draw_sea()
        self.player.draw()

    def update(self, dt):
        self.player.update(dt, self.keys)

    def draw_sea(self):
        window_width = self.window.width
        window_height = self.window.height

        # Calculate the player's tile position
        tile_x = int(self.player.sprite.x // self.sea_texture.width)
        tile_y = int(self.player.sprite.y // self.sea_texture.height)

        # Determine how many tiles we need based on the window size
        tiles_x = int(window_width / self.sea_texture.width) + 2
        tiles_y = int(window_height / self.sea_texture.height) + 2

        # Starting positions for the tiling
        start_x = tile_x - tiles_x // 2
        start_y = tile_y - tiles_y // 2

        # Draw the tiles around the player
        for x in range(start_x, start_x + tiles_x):
            for y in range(start_y, start_y + tiles_y):
                self.sea_texture.blit(x * self.sea_texture.width, y * self.sea_texture.height)
