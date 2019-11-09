from Calculator.def_files.Variance import Variance

def Sd(my_population):
    calculated_variance = Variance(my_population)
    return calculated_variance ** 0.5
