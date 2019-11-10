from pprint import pprint
from Calculator.def_files.Proportion import Proportion
from Calculator.def_files.Variance import Variance

def Variance_sample_proportion(my_population):
    p,proportion_success= Proportion(my_population)
    return Variance(proportion_success)



