from Calculator.def_files.Proportion import Proportion

def Variance_popu_proportion(my_population):
    my_proportion= Proportion(my_population)
    intermediate_calc = (my_proportion*(1-my_proportion))
    var_pop_prop = (intermediate_calc/len(my_population))
    my_var_pop_prop = var_pop_prop ** 0.5
    return my_var_pop_prop
