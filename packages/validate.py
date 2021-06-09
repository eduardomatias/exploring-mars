import re
from packages.constants import DIRECTION, COMMAND


class Validate:

    @staticmethod
    def area(area):
        """
        Valida a entrada da area
        :param area: x e y
        :return: False se inválido, quando válido retorna o valor de x e y convertidos para inteiro
        """
        area_x_y = str(area).split()
        # verifica formato da entrada, necessário dois valores separados por espaço
        if len(area_x_y) != 2:
            return False

        # Verifica valores inteiros
        x, y = area_x_y
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            return False

        # Verifica se a coordenada é menor ou igual a Zero
        if x <= 0 or y <= 0:
            return False

        return x, y

    @staticmethod
    def probe(initial_position, movements, area):

        if not area:
            return False

        if not Validate.movement(movements):
            return False

        initial_position_valid = Validate.initial_position(initial_position, area)
        if not initial_position_valid:
            return False

        return initial_position_valid, movements, area

    @staticmethod
    def initial_position(initial_position, area):
        """
        Valida posição inicial da sonda
        :param initial_position: x y direção ("N", "E", "S", "W")
        :param area: instancia de Area
        :return: False se inválido, quando válido retorna o initial_position com as conversoções de tipo necessárias
        """
        initial_x_y_direction = str(initial_position).split()
        # verifica formato da entrada, necessário dois valores separados por espaço
        if len(initial_x_y_direction) != 3:
            return False

        x, y, direction = initial_x_y_direction

        # Verifica valores inteiros
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            return False

        # Verifica valores menores que Zero
        if x < 0 or y < 0:
            return False

        # Verifica valores maiores que o máximo permitido
        # Não é permitido soltar a sonda fora da malha definida pelo usuário
        if x > area.max_x or y > area.max_y:
            return False

        # Verifica direção inicial da sonda
        if direction not in DIRECTION:
            return False

        return x, y, direction

    @staticmethod
    def movement(movement):
        """
        Valida a movimentação da sonda
        :param movement: Movimentos esperados "L", "R", "M"
        :return: bool
        """
        return bool(re.fullmatch(f'[{"".join(COMMAND)}]*', movement))
