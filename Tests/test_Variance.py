import unittest

from Calculator.Calculator import Calculator
from CsvReader.Read_answer import read_answer
from CsvReader.Read_population import read_population


class MyTestCase(unittest.TestCase):
    calculator = Calculator()

    def test_variance(self):
        my_population = read_population("population.csv")
        expected_output = read_answer("answer_variance.csv")
        self.assertEqual(self.calculator.variance(my_population), expected_output)  # positive test
        self.assertNotEqual(self.calculator.variance(my_population), expected_output + 1)  # negative test

if __name__ == '__main__':
    unittest.main()