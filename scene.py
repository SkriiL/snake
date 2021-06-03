import os


class Scene:
    def __init__(self, x_size=64, y_size=25):
        self.x_size: int = x_size
        self.y_size: int = y_size
        self.scene_list: list = []

    def build_empty_scene_list(self):
        self.scene_list = []
        for row in range(0, self.y_size):
            self.scene_list.append([])
            for col in range(0, self.x_size):
                self.scene_list[row].append(" ")

    def print_scene(self):
        os.system('cls')
        for x in range(0, self.x_size + 2):  # print upper line
            print("-", end='')
        print()
        for y in range(0, self.y_size):
            print("|", end='')
            for x in range(0, self.x_size):
                element = self.scene_list[y][x]
                print(element, end='')
            print("|")
        for x in range(0, self.x_size + 2):  # print lower line
            print("-", end='')
        print()

    def get_list(self) -> list:
        return self.scene_list

    def update_list(self, lst: list):
        self.scene_list = lst
        self.print_scene()


if __name__ == '__main__':
    s = Scene()
    s.print_scene()
