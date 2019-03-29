import unittest
import volumes


class Test_volumes(unittest.TestCase):

    def test_get_cube_vol_basic1(self):
        self.assertEqual(27, volumes.get_cube_vol(3))

    def test_get_cube_vol_basic2(self):
        self.assertEqual(64, volumes.get_cube_vol(4))


