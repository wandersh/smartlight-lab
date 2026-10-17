import unittest
from smart_light import SmartLight


class TestSmartLight(unittest.TestCase):
    def setUp(self):
        self.light = SmartLight("Test Light")

    def test_initial_state(self):
        self.assertFalse(self.light.is_on)
        self.assertEqual(self.light.brightness, 0)

    def test_turn_on(self):
        self.light.turn_on()
        self.assertTrue(self.light.is_on)
        self.assertEqual(self.light.brightness, 100)

    def test_turn_off(self):
        self.light.turn_on()
        self.light.turn_off()
        self.assertFalse(self.light.is_on)

    def test_set_brightness_valid(self):
        self.light.turn_on()
        self.light.set_brightness(40)
        self.assertEqual(self.light.brightness, 40)

    def test_set_brightness_too_high(self):
        with self.assertRaises(ValueError):
            self.light.set_brightness(150)

    def test_set_brightness_negative(self):
        with self.assertRaises(ValueError):
            self.light.set_brightness(-5)

    def test_set_brightness_wrong_type(self):
        with self.assertRaises(TypeError):
            self.light.set_brightness("bright")


if __name__ == "__main__":
    unittest.main(verbosity=2)
