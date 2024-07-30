# main.py in src
import pyglet
from src.game_engine.window import Window

def main():
    window = Window(1920, 1080, "Treacherous Tides")
    pyglet.clock.schedule_interval(window.update, 1/60.0)
    pyglet.app.run()

if __name__ == "__main__":
    main()
