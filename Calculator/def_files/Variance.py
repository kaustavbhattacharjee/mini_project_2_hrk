from Calculator.def_files.Mean import Mean
def Variance(my_population):
        sum = 0
        index = 0
        my_variance = 0
        calculated_mean = Mean(my_population)
        for index in range(0, len(my_population)):
            sum += ((my_population[index] - calculated_mean) ** 2)
        my_variance = sum/len(my_population)
        return my_variance
