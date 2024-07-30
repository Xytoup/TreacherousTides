# game.py in src/scenes
import pyglet
import os
from src.game_engine.player import Player  # Ensure this import is correct

class InfiniteSea:
    def __init__(self, window, player):
        self.window = window
        self.player = player
        script_dir = os.path.dirname(__file__)  # Get the directory of the current script
        assets_dir = os.path.join(script_dir, '../../assets/images')
        self.texture = pyglet.image.load(os.path.join(assets_dir, 'tex_Water.jpg'))  # Correct path to texture

    def draw(self):
        window_width = self.window.width
        window_height = self.window.height

        # Calculate the player's tile position
        tile_x = int(self.player.x // self.texture.width)
        tile_y = int(self.player.y // self.texture.height)

        # Determine how many tiles we need based on the window size
        tiles_x = int(window_width / self.texture.width) + 2
        tiles_y = int(window_height / self.texture.height) + 2

        # Starting positions for the tiling
        start_x = tile_x - tiles_x // 2
        start_y = tile_y - tiles_y // 2

        # Draw the tiles around the player
        for x in range(start_x, start_x + tiles_x):
            for y in range(start_y, start_y + tiles_y):
                tile_x = x * self.texture.width
                tile_y = y * self.texture.height
                self.texture.blit(tile_x, tile_y)

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self, dt):
        # Update player position here (example movement)
        self.x += dt * 100  # Move 100 pixels per second to the right
        self.y += dt * 50   # Move 50 pixels per second downwards

# game.py in src/scenes
import pyglet

# game.py in src/scenes
import pyglet
from src.game_engine.player import Player

class GameScene:
    def __init__(self, window):
        self.window = window
        self.player = Player()
        self.keys = pyglet.window.key.KeyStateHandler()
        self.window.push_handlers(self.keys)

    def on_draw(self):
        self.window.clear()
        self.player.draw()

    def update(self, dt):
        self.player.update(dt, self.keys)
