import unittest

from Calculator.Calculator import Calculator
from CsvReader.Read_answer import read_answer
from CsvReader.Read_population import read_population
from CsvReader.Read_answer_list import read_answer_list


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
        my_population = read_population("population.csv")
        expected_output = read_answer("answer_sd.csv")
        self.assertEqual(self.calculator.sd(my_population), expected_output)  # positive test
        self.assertNotEqual(self.calculator.sd(my_population), (expected_output + 1))  # negative test

    def test_variance_popu_proportion(self):
        my_population = read_population("population.csv")
        #expected_output = read_answer("answer_variance_popu_proportion.csv")
        self.assertEqual(self.calculator.variance_popu_proportion(my_population), read_answer("answer_variance_popu_proportion.csv"))  # positive test
        self.assertNotEqual(self.calculator.variance_popu_proportion(my_population),(read_answer("answer_variance_popu_proportion.csv") + 1))  # negative test

    def test_z_score(self):
        my_population = read_population("population.csv")
        expected_output = read_answer_list("answer_zscore.csv")
        self.assertListEqual(self.calculator.z_score(my_population), expected_output)  # positive test
        self.assertNotEqual(self.calculator.z_score(my_population), (list(map(lambda x: x + 1, expected_output))))  # negative test


    def test_standardised_score(self):
        my_population = read_population("population.csv")
        expected_output = read_answer_list("answer_zscore.csv")
        self.assertListEqual(self.calculator.z_score(my_population), expected_output)  # positive test
        self.assertNotEqual(self.calculator.z_score(my_population),(list(map(lambda x: x + 1, expected_output))))  # negative test

    def test_pop_correlation_coefficient(self):
        my_population = read_population("population.csv")
        expected_output = read_answer("answer_pop_correlation_coefficient.csv")
        self.assertEqual(self.calculator.pop_correlation_coefficient(my_population), expected_output)  # positive test
        self.assertNotEqual(self.calculator.pop_correlation_coefficient(my_population), (expected_output + 1))  # negative test

    def test_confidence_interval(self):
        my_population = read_population("population.csv")
        expected_output = read_answer("answer_confidence_interval.csv")
        self.assertEqual(self.calculator.confidence_interval(my_population), expected_output)  # positive test
        self.assertNotEqual(self.calculator.confidence_interval(my_population), (expected_output + 1))  # negative test

    def test_variance(self):
        my_population = read_population("population.csv")
        expected_output = read_answer("answer_variance.csv")
        self.assertEqual(self.calculator.variance(my_population), expected_output)  # positive test
        self.assertNotEqual(self.calculator.variance(my_population), expected_output + 1)  # negative test

    def test_p_value(self):
        pass
    def test_proportion(self):
        my_population = read_population("population.csv")
        expected_output = read_answer("answer_proportion.csv")
        self.assertEqual(self.calculator.proportion(my_population), expected_output)  # positive test
        self.assertNotEqual(self.calculator.proportion(my_population), (expected_output + 1))  # negative test

    def test_sample_mean(self):
        my_population = read_population("population.csv")
        self.assertEqual(self.calculator.sample_mean(my_population), read_answer("answer_sample_mean.csv"))  # positive test
        self.assertNotEqual(self.calculator.sample_mean(my_population), (read_answer("answer_sample_mean.csv") + 1))  # negative test

    def test_sample_sd(self):
        my_population = read_population("population.csv")
        self.assertEqual(self.calculator.sample_sd(my_population), read_answer("answer_sample_sd.csv"))  # positive test
        self.assertNotEqual(self.calculator.sample_sd(my_population), (read_answer("answer_sample_sd.csv") + 1.5))  # negative test

    def test_variance_sample_proportion(self):
        my_population = read_population("population.csv")
        #expected_output = read_answer("answer_variance_sample_proportion.csv")
        self.assertEqual(self.calculator.variance_sample_proportion(my_population), read_answer("answer_variance_sample_proportion.csv"))  # positive test
        self.assertNotEqual(self.calculator.variance_sample_proportion(my_population), (read_answer("answer_variance_sample_proportion.csv") + 1))  # negative test


if __name__ == '__main__':
    unittest.main()
