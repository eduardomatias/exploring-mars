from packages.validate import Validate


class Area:
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0

    def __init__(self):
        self.create()

    def create(self):
        """
        Solicita a dimensão da matriz para limitar a malha do planalto onde as sondas se movem
        :return:
        """
        area = input("Informe a coordenada do ponto superior-direito da malha do planalto (X Y):")
        area_valid = Validate.area(area)
        if not area_valid:
            print("Formato invádido. Informe dois valores inteiros maiores que Zero e separados por espaço.")
            return self.create()

        self.max_x, self.max_y = area_valid
