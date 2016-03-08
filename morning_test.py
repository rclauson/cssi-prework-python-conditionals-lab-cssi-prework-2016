import sys
import unittest

from morning import coffee, commute, wake_up

class TestMorning(unittest.TestCase):

    def test_wake_up(self):
        self.assertEqual(wake_up("Sunday"), "Go back to bed")
        self.assertEqual(wake_up("saturday"), "Go back to bed")
        self.assertEqual(wake_up("wednesday"), "Stop hitting snooze")

    def test_commute(self):
        self.assertEqual(commute("rainy", 200), "Better take the car")
        self.assertEqual(commute("Rainy", 0), "Better take the car")
        self.assertEqual(commute("sunny", 1), "Better take the car")
        self.assertEqual(commute("Sunny", 40), "Enjoy a bike ride!")
        self.assertEqual(commute("Sunny", 30), "Hop on the bus")

    def test_coffee(self):
        self.assertEqual(coffee(200), "Time for a triple shot espresso")
        self.assertEqual(coffee(100), "Time for a triple shot espresso")
        self.assertEqual(coffee(99), "Go for a large black coffee")
        self.assertEqual(coffee(50), "Go for a large black coffee")
        self.assertEqual(coffee(49), "A latte will serve you well")
        self.assertEqual(coffee(0), "You have reached the Nirvana of 21st century communication!")



if __name__ == '__main__':
    unittest.main()
