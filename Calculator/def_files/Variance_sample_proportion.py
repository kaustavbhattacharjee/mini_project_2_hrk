from pprint import pprint

def Variance_sample_proportion(my_population):

    var1=sum(my_population)
    var2=(var1 * var1)/len(my_population)
    my_list=list()
    for index in range(0,len(my_population)):
        my_list.append(((my_population[index]) * (my_population[index])))
    var3=sum(my_list)
    var4= var3 - var2
    var5=len(my_population) - 1
    sample_varience=round(var4/var5,2)
    return sample_varience



