from Calculator.def_files.Mean import Mean
from Calculator.def_files.Sd import Sd

def Z_score(my_population):
    my_mean = Mean(my_population)
    my_sd = Sd(my_population)
    zscore = list()
    for x in my_population:
        my_score = (x-my_mean)/my_sd
        zscore.append(my_score)
    return zscore




