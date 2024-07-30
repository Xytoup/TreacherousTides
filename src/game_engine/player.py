# player.py in src/game_engine
import pyglet
import os
import math

class Player:
    def __init__(self):
        print("Initializing Player")
        script_dir = os.path.dirname(__file__)
        assets_dir = os.path.join(script_dir, '../../assets/images')
        ship_image_path = os.path.join(assets_dir, 'pirateship.png')
        self.ship_image = pyglet.image.load(ship_image_path)
        self.sprite = pyglet.sprite.Sprite(self.ship_image, x=400, y=300)
        self.sprite.scale = 1 / 3  # Adjust the scale to 1/3 of its original size

        self.rotation_speed = 150  # Degrees per second
        self.speed = 0
        self.acceleration = 50  # Pixels per second squared
        self.max_speed = 300  # Maximum speed in pixels per second
        self.deceleration = 30  # Deceleration rate

    def update(self, dt, keys):
        # Handle rotation based on speed
        if keys[pyglet.window.key.A]:
            self.sprite.rotation += self.get_rotation_speed() * dt
        if keys[pyglet.window.key.D]:
            self.sprite.rotation -= self.get_rotation_speed() * dt

        # Handle acceleration and deceleration
        if keys[pyglet.window.key.W]:
            self.speed += self.acceleration * dt
        else:
            self.speed = max(0, self.speed - self.deceleration * dt)

        self.speed = max(0, min(self.speed, self.max_speed))

        angle_radians = -math.radians(self.sprite.rotation)
        self.sprite.x += self.speed * math.cos(angle_radians) * dt
        self.sprite.y += self.speed * math.sin(angle_radians) * dt

    def get_rotation_speed(self):
        # Progressive rotation speed based on current speed
        if self.speed == 0:
            return 0
        elif self.speed < self.max_speed / 2:
            return 5
        else:
            return 10

    def draw(self):
        self.sprite.draw()
