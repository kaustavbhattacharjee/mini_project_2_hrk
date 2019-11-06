import unittest

from Calculator.Calculator import Calculator
from CsvReader.Read_answer import read_answer
from CsvReader.Read_population import read_population


class MyTestCase(unittest.TestCase):
    calculator = Calculator()
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_mean(self):
        my_population=read_population("population.csv")
        expected_output=read_answer("answer_mean.csv")
        self.assertEqual(self.calculator.mean(my_population),expected_output) #positive test
        self.assertNotEqual(self.calculator.mean(my_population),(expected_output+1)) #negative test

    def test_median(self):
        my_population = read_population("population.csv")
        expected_output = read_answer("answer_median.csv")
        self.assertEqual(self.calculator.median(my_population), expected_output)  # positive test
        self.assertNotEqual(self.calculator.median(my_population), (expected_output + 1))  # negative test

    def test_mode(self):
        my_population = read_population("population.csv")
        expected_output = read_answer("answer_mode.csv")
        self.assertEqual(self.calculator.mode(my_population), expected_output)  # positive test
        self.assertNotEqual(self.calculator.mode(my_population), (expected_output + 1))  # negative test

    def test_sd(self):
        pass
    def test_variance_popu_proportion(self):
        pass
    def test_z_score(self):
        pass
    def test_standardised_score(self):
        pass
    def test_pop_correlation_coefficient(self):
        pass
    def test_confidence_interval(self):
        pass
    def test_variance(self):
        pass
    def test_p_value(self):
        pass
    def test_proportion(self):
        my_population = read_population("population.csv")
        expected_output = read_answer("answer_proportion.csv")
        self.assertEqual(self.calculator.proportion(my_population), expected_output)  # positive test
        self.assertNotEqual(self.calculator.proportion(my_population), (expected_output + 1))  # negative test

    def test_sample_mean(self):
        pass
    def test_sample_sd(self):
        pass
    def test_variance_sample_proportion(self):
        pass


if __name__ == '__main__':
    unittest.main()
