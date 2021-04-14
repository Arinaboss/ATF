import unittest
class VolumeBox():
    def __init__(self):
        pass


    def volume(self, h, w, l):
        try:
            if int(h) > 0:
                if int(w) > 0:
                    if int(l) > 0:
                        v = h * w * l
                        return v
                    else:
                        return False
        except ValueError:
            return 'not a number'


class TestVolume(unittest.TestCase):
    def setUp(self):
        self.volume_box = VolumeBox()


    def test_volume(self):
        self.assertEqual(self.volume_box.volume(70, 40, 50), 140000)


    def test_negative_number(self):
        self.assertEqual(self.volume_box.volume(5, -5, 5), 125)


    def test_only_two_parametres(self):
        self.assertEqual(self.volume_box.volume(5, ' ', 5), 125)


    def test_symbols_in_formula(self):
        self.assertEqual(self.volume_box.volume(5, '$', 5), 125)

    def test_zero(self):
        self.assertEqual(self.volume_box.volume(0, 5, 5), 0)
