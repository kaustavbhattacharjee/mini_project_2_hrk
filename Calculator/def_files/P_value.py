from Calculator.def_files.Z_score import Z_score


def P_value(my_populatio):
    df=(len(my_population))* 2
    p = 1 - stats.t.cdf(Z_score(my_populatio),df=df)

