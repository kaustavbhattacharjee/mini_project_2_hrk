from Calculator.def_files.Confidence_interval import Confidence_interval
from Calculator.def_files.Mean import Mean
from Calculator.def_files.Median import Median
from Calculator.def_files.Mode import Mode
from Calculator.def_files.P_value import P_value
from Calculator.def_files.Pop_correlation_coefficient import Pop_correlation_coefficient
from Calculator.def_files.Proportion import Proportion
from Calculator.def_files.Sample_mean import Sample_mean
from Calculator.def_files.Sample_sd import Sample_sd
from Calculator.def_files.Sd import Sd
from Calculator.def_files.Standardised_score import Standardised_score
from Calculator.def_files.Variance import Variance
from Calculator.def_files.Variance_popu_proportion import Variance_popu_proportion
from Calculator.def_files.Variance_sample_proportion import Variance_sample_proportion
from Calculator.def_files.Z_score import Z_score

class Calculator:
    def __init__(self):
        pass
    def mean(self,my_population):
        return Mean(my_population)

    def median(self, my_population):
        return Median(my_population)


    def mode(self, my_population):
        return Mode(my_population)

    def sd(self, my_population):
        return Sd(my_population)


    def variance_popu_proportion(self):
        # return Variance_popu_proportion()
        pass
    def z_score(self,my_population):
        new_z_score1 =  Z_score(my_population)
        new_z_score = list()
        for x in new_z_score1:
            new_z_score.append(round(x,2)) #creating rounded zscore upto 2 decimal points
        return new_z_score

    def standardised_score(self):
        #return Standardised_score()
        pass

    def pop_correlation_coefficient(self):
        #return Pop_correlation_coefficient(my_population)
        pass

    def confidence_interval(self):
        # return Confidence_interval()
        pass

    def variance(self,my_population):
        return Variance(my_population)

    def p_value(self):
        # return P_value()
        pass
    def proportion(self,my_population):
        return Proportion(my_population)

    def sample_mean(self,my_population):
        return Sample_mean(my_population)

    def sample_sd(self,my_population):
        return Sample_sd(my_population)
        pass
    def variance_sample_proportion(self,my_population):
        return Variance_sample_proportion(my_population)


