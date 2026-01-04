import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Test suite for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Tests for the add method
    def test_addition(self):
        """Test addition of two positive numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, -20), -30)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(10, -5), 5)
        self.assertEqual(self.calc.add(-10, 5), -5)
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
        """Test addition of floating-point numbers."""
        self.assertAlmostEqual(self.calc.add(2.5, 3.7), 6.2)
        self.assertAlmostEqual(self.calc.add(-1.5, 1.5), 0.0)

    # Tests for the subtract method
    def test_subtraction(self):
        """Test subtraction of positive numbers."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(20, 8), 12)
        """Test subtraction resulting in a negative number."""
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(3, 8), -5)
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(5, -3), 8)
        """Test subtraction with zero."""
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        """Test subtraction of floating-point numbers."""
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.3), 3.2)
        self.assertAlmostEqual(self.calc.subtract(1.1, 1.1), 0.0)

    # Tests for the multiply method
    def test_multiplication(self):
        """Test multiplication of positive numbers."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(7, 6), 42)
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(3, -4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        """Test multiplication with zero."""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        """Test multiplication with one (identity property)."""
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.multiply(1, 5), 5)
        """Test multiplication of floating-point numbers."""
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0)
        self.assertAlmostEqual(self.calc.multiply(1.5, 2.0), 3.0)

    # Tests for the divide method
    def test_division(self):
        """Test division of positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        """Test division that results in a float."""
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.333333, places=5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        """Test division with negative numbers."""
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        """Test zero divided by a non-zero number."""
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -3), 0.0)
        """Test division of floating-point numbers."""
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.divide(5.5, 1.1), 5.0)


if __name__ == '__main__':
    unittest.main()