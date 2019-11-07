from Calculator.def_files.Variance_sample_proportion import Variance_sample_proportion

def Squareroot(num):
        if num == 0 or num == 1:
            return num
        root_val = 0
        root_val = float(root_val)
        prec_val = 0.001
        prec_val = float(prec_val)
        square = root_val
        square = float(square)
        while square <= num:
            root_val = root_val + prec_val
            square = root_val * root_val
        return (round(root_val, 2))

def Sample_sd(my_population):
    sample_variance = Variance_sample_proportion(my_population)
    return Squareroot(sample_variance)
