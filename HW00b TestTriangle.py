# HW00b TestTriangle
# Junyao Li
import unittest
from HW00b import classify_Triangle   

class TestTriangleClassification(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classify_Triangle(3, 3, 3), 'Equilateral')

    def test_isosceles(self):
        self.assertEqual(classify_Triangle(3, 3, 4), 'Isosceles')

    def test_scalene(self):
        self.assertEqual(classify_Triangle(3, 4, 5), 'Right')

    def test_right_triangle(self):
        self.assertEqual(classify_Triangle(3, 4, 5), 'Right')

    def test_not_a_triangle(self):
        self.assertEqual(classify_Triangle(1, 2, 3), 'NotATriangle')

    def test_invalid_input_negative(self):
        self.assertEqual(classify_Triangle(-1, 2, 3), 'InvalidInput')

    def test_invalid_input_zero(self):
        self.assertEqual(classify_Triangle(0, 2, 3), 'InvalidInput')

    def test_invalid_input_type(self):
        self.assertEqual(classify_Triangle(3.5, 4, 5), 'InvalidInput')

if __name__ == "__main__":
    unittest.main()
