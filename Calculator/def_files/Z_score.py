from pprint import pprint

from Calculator.def_files.Mean import Mean

def Z_score(my_Population):
    my_list=list()
    for row in my_Population:
         my_list.append(row)
         pprint(mylist)
    zscore = (my_list[0] - Mean(my_Population))
    return round(zscore, 2)



