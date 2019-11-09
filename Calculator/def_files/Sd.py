from Calculator.def_files.Variance import Variance
def Squareroot(num):
     if num == 0 or num == 1:
       return num
     root_val = 0
     root_val = float(root_val)
     prec_val = 0.001
     prec_val = float(prec_val)
     square =  root_val
     square = float(square)
     while square <= num:
      root_val = root_val + prec_val
      square = root_val * root_val
     return (round(root_val,2))

def Sd(my_population):
    calculated_variance = Variance(my_population)
    return calculated_variance ** 0.5
