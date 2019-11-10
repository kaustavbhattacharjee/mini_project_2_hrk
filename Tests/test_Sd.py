import unittest

from Calculator.Calculator import Calculator
from CsvReader.Read_answer import read_answer
from CsvReader.Read_population import read_population


class MyTestCase(unittest.TestCase):
    calculator = Calculator()
    def test_sd(self):
        my_population = read_population("population.csv")
        expected_output = read_answer("answer_sd.csv")
        self.assertEqual(self.calculator.sd(my_population), expected_output)  # positive test
        self.assertNotEqual(self.calculator.sd(my_population), (expected_output + 1))  # negative test

if __name__ == '__main__':
    unittest.main()