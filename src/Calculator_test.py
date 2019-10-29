import unittest
from Calculator import Calculator

class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_mean(self):
        pass
    def test_median(self):
        pass
    def test_mode(self):
        pass
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
        pass
    def test_sample_mean(self):
        pass
    def test_sample_sd(self):
        pass
    def test_variance_sample_proportion(self):
        pass


if __name__ == '__main__':
    unittest.main()
