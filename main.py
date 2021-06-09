from os import listdir
from os.path import isfile, join
from packages.area import Area
from packages.probe import Probe


class SpaceProbe:
    probes = []
    dir_probes = "probes"

    def __init__(self):
        self.area = Area()
        self.load_probes_file()
        self.move_probes()

    def load_probes_file(self):
        """
        Carrega os arquivos das Sondas e adicina em self.probes
        :return: void
        """
        probes_files = [file for file in listdir(self.dir_probes) if isfile(join(self.dir_probes, file))]
        if not probes_files:
            print("Nenhuma Sonda para enviar a Marte.")
            exit()

        probes_files.sort()
        for probe_file in probes_files:
            probe = open(f'{self.dir_probes}/{probe_file}')
            initial_position = probe.readline().strip()
            movements = probe.readline().strip()
            try:
                # Tenta cria a Sonda
                new_probe = Probe(initial_position, movements, self.area)
            except ValueError:
                print(f"Não foi possivel enviar a Sonda {probe_file[:-4]} a Marte.")
                continue
            self.probes.append(new_probe)

    def move_probes(self):
        if not self.probes:
            print("Nenhuma Sonda enviada a Marte.")
            exit()

        # Movimenta as sondas
        for probe in self.probes:
            probe.execute_movement()
            # print com o local que a sonda parou
            print(probe.x, probe.y, probe.direction)


if __name__ == "__main__":
    SpaceProbe()
