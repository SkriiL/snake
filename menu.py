from scene import Scene
from pynput import keyboard
import time


class Menu(Scene):
    def __init__(self, x_size=64, y_size=25):
        super().__init__(x_size, y_size)
        self.entries = ["Play", "Options", "Exit"]
        self.selected = 0
        self.build_empty_scene_list()
        self.print_menu()
        self.wait_for_input()

    def print_menu(self):
        self.build_empty_scene_list()
        gamefield = self.get_list()
        y_center = int(self.y_size / 2)
        for i in range(0, len(self.entries)):
            word = self.entries[i]
            if i == self.selected:
                word = "-> " + word + " <-"
            y_position = y_center + (i - int(len(self.entries) / 2)) * 2
            x_position = int(self.x_size / 2) - int(len(word) / 2) - 1
            for letter in word:
                gamefield[y_position][x_position] = letter
                x_position += 1
        self.print_scene()

    def move_up_selection(self):
        self.selected = len(self.entries) - 1 if self.selected == 0 else self.selected - 1

    def move_down_selection(self):
        self.selected = 0 if self.selected == len(self.entries) - 1 else self.selected + 1

    def wait_for_input(self): # TODO pynput Doku
        while True:
            time.sleep(0.2)
            with keyboard.Events() as events:
                event = events.get(1e6)
                if event.key == keyboard.KeyCode.from_char("w"): # TODO to up
                    self.move_up_selection()
                    self.print_menu()
                elif event.key == keyboard.KeyCode.from_char("s"): # TODO to down
                    self.move_down_selection()
                    self.print_menu()


if __name__ == '__main__':
    m = Menu()