from Calculator.def_files.Variance_sample_proportion import Variance_sample_proportion


def Sample_sd(my_population):
    sample_variance = Variance_sample_proportion(my_population)
    return (sample_variance ** 0.5)
