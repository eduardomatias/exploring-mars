from packages.constants import DIRECTION
from packages.validate import Validate


class Probe:

    def __init__(self, initial_position, movements, area):
        probe_valid = Validate.probe(initial_position, movements, area)
        if not probe_valid:
            raise ValueError

        self.initial_position, self.movements, self.area = probe_valid
        self.x, self.y, self.direction = self.initial_position
        self.flags = []
        self.move_functions = {
            'M': self.__move,
            'L': self.__turn_left,
            'R': self.__turn_rigth,
            'F': self.__flag
        }

    def execute_movement(self):
        for movement in self.movements:
            self.move_functions[movement]()

    def __move(self):
        # Move a sonda apenas se não ultrapassar o limite da area
        if self.direction == 'N' and (self.y + 1) <= self.area.max_y:
            self.y += 1
        elif self.direction == 'E' and (self.x + 1) <= self.area.max_x:
            self.x += 1
        elif self.direction == 'S' and (self.y - 1) >= 0:
            self.y -= 1
        elif self.direction == 'W' and (self.x - 1) >= 0:
            self.x -= 1

    def __turn_left(self):
        # Vira a sonda para esquerda
        index_direction = DIRECTION.index(self.direction)
        self.direction = DIRECTION[index_direction - 1]

    def __turn_rigth(self):
        # Vira a sonda para direita
        index_direction = DIRECTION.index(self.direction)
        self.direction = DIRECTION[index_direction + 1 if (index_direction + 1) < 4 else 0]

    def __flag(self):
        self.flags.append(f'{self.x} - {self.y}')
