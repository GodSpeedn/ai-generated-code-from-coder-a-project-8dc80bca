import unittest

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance for each test."""
        from simple_calculator import SimpleCalculator # Assuming the class is in simple_calculator.py
        self.calculator = SimpleCalculator()

    # --- Test cases for add method ---
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(self.calculator.add(5, 3), 8)

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        self.assertEqual(self.calculator.add(-5, -3), -8)

    def test_add_zero_and_positive(self):
        """Test adding zero to a positive number."""
        self.assertEqual(self.calculator.add(0, 7), 7)

    def test_add_positive_and_zero(self):
        """Test adding a positive number to zero."""
        self.assertEqual(self.calculator.add(7, 0), 7)

    def test_add_zero_and_negative(self):
        """Test adding zero to a negative number."""
        self.assertEqual(self.calculator.add(0, -7), -7)

    def test_add_mixed_numbers(self):
        """Test adding a positive and a negative number."""
        self.assertEqual(self.calculator.add(10, -3), 7)
        self.assertEqual(self.calculator.add(-10, 3), -7)

    def test_add_float_numbers(self):
        """Test adding float numbers."""
        self.assertAlmostEqual(self.calculator.add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(self.calculator.add(-1.5, 2.0), 0.5)

    # --- Test cases for subtract method ---
    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        self.assertEqual(self.calculator.subtract(10, 4), 6)
        self.assertEqual(self.calculator.subtract(4, 10), -6)

    def test_subtract_negative_numbers(self):
        """Test subtracting two negative numbers."""
        self.assertEqual(self.calculator.subtract(-10, -4), -6)
        self.assertEqual(self.calculator.subtract(-4, -10), 6)

    def test_subtract_zero_from_positive(self):
        """Test subtracting zero from a positive number."""
        self.assertEqual(self.calculator.subtract(5, 0), 5)

    def test_subtract_positive_from_zero(self):
        """Test subtracting a positive number from zero."""
        self.assertEqual(self.calculator.subtract(0, 5), -5)

    def test_subtract_zero_from_negative(self):
        """Test subtracting zero from a negative number."""
        self.assertEqual(self.calculator.subtract(-5, 0), -5)

    def test_subtract_negative_from_zero(self):
        """Test subtracting a negative number from zero."""
        self.assertEqual(self.calculator.subtract(0, -5), 5)

    def test_subtract_mixed_numbers(self):
        """Test subtracting a positive from a negative, and vice versa."""
        self.assertEqual(self.calculator.subtract(-5, 3), -8)
        self.assertEqual(self.calculator.subtract(5, -3), 8)

    def test_subtract_float_numbers(self):
        """Test subtracting float numbers."""
        self.assertAlmostEqual(self.calculator.subtract(7.5, 2.5), 5.0)
        self.assertAlmostEqual(self.calculator.subtract(2.0, 3.5), -1.5)

    # --- Test cases for multiply method ---
    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        self.assertEqual(self.calculator.multiply(5, 3), 15)

    def test_multiply_negative_numbers(self):
        """Test multiplying two negative numbers."""
        self.assertEqual(self.calculator.multiply(-5, -3), 15)

    def test_multiply_positive_and_negative(self):
        """Test multiplying a positive and a negative number."""
        self.assertEqual(self.calculator.multiply(5, -3), -15)
        self.assertEqual(self.calculator.multiply(-5, 3), -15)

    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        self.assertEqual(self.calculator.multiply(10, 0), 0)
        self.assertEqual(self.calculator.multiply(-10, 0), 0)
        self.assertEqual(self.calculator.multiply(0, 0), 0)

    def test_multiply_by_one(self):
        """Test multiplying by one."""
        self.assertEqual(self.calculator.multiply(10, 1), 10)
        self.assertEqual(self.calculator.multiply(-10, 1), -10)

    def test_multiply_float_numbers(self):
        """Test multiplying float numbers."""
        self.assertAlmostEqual(self.calculator.multiply(2.5, 2.0), 5.0)
        self.assertAlmostEqual(self.calculator.multiply(-1.5, 3.0), -4.5)

    # --- Test cases for divide method ---
    def test_divide_positive_numbers_exact(self):
        """Test dividing positive numbers with an exact integer result."""
        self.assertEqual(self.calculator.divide(10, 2), 5)

    def test_divide_positive_numbers_float(self):
        """Test dividing positive numbers with a float result."""
        self.assertAlmostEqual(self.calculator.divide(10, 4), 2.5)

    def test_divide_negative_numbers(self):
        """Test dividing two negative numbers."""
        self.assertEqual(self.calculator.divide(-10, -2), 5)

    def test_divide_positive_by_negative(self):
        """Test dividing a positive by a negative number."""
        self.assertEqual(self.calculator.divide(10, -2), -5)

    def test_divide_negative_by_positive(self):
        """Test dividing a negative by a positive number."""
        self.assertEqual(self.calculator.divide(-10, 2), -5)

    def test_divide_by_one(self):
        """Test dividing by one."""
        self.assertEqual(self.calculator.divide(7, 1), 7)
        self.assertEqual(self.calculator.divide(-7, 1), -7)

    def test_divide_zero_by_number(self):
        """Test dividing zero by a non-zero number."""
        self.assertEqual(self.calculator.divide(0, 5), 0)
        self.assertEqual(self.calculator.divide(0, -5), 0)

    def test_divide_float_results(self):
        """Test division resulting in float numbers."""
        self.assertAlmostEqual(self.calculator.divide(7, 2), 3.5)
        self.assertAlmostEqual(self.calculator.divide(-7, 2), -3.5)
        self.assertAlmostEqual(self.calculator.divide(1.0, 3.0), 1/3)

    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            self.calculator.divide(10, 0)
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            self.calculator.divide(-5, 0)
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            self.calculator.divide(0, 0)

# To run these tests from the command line, you would typically save this
# as a Python file (e.g., test_calculator.py) and run:
# python -m unittest test_calculator.py