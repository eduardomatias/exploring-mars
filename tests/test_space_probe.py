import unittest
import builtins
from unittest import TestCase, mock
from packages.probe import Probe
from packages.area import Area


class TestSpaceProbe(TestCase):

    def setUp(self) -> None:
        with mock.patch.object(builtins, 'input', lambda _: '50 50'):
            self.area = Area()

    def tearDown(self) -> None:
        pass

    def test_instance_probe(self):
        initial_position = "1 2 N"
        movements = "LMLMLMLMM"
        probe = Probe(initial_position, movements, self.area)
        self.assertIsInstance(probe, Probe)

    def test_probe_execute_movement(self):
        initial_position = "1 2 N"
        movements = "LMLMLMLMM"
        probe = Probe(initial_position, movements, self.area)
        probe.execute_movement()
        self.assertEqual(probe.x, 1)
        self.assertEqual(probe.y, 3)
        self.assertEqual(probe.direction, "N")

    def test_probe_error_initial_position(self):
        initial_position = "1 2 X"
        movements = "LMLMLMLMM"
        with self.assertRaises(ValueError):
            Probe(initial_position, movements, self.area)

    def test_probe_error_movements(self):
        initial_position = "1 2 N"
        movements = "X"
        with self.assertRaises(ValueError):
            Probe(initial_position, movements, self.area)


if __name__ == '__main__':
    unittest.main()
