import math as mt
def fact(k):
    if k==1 or k==0:
        return 1
    else:
        return k * fact(k-1)
def estimate_pi():
    mult_value=(2*mt.sqrt(2))/9801
    sub_res=1
    k=0
    sum_res=0
    while sub_res>=10**(-15):
        sub_res=(fact(4*k))*(1103+(26390 * k))/((fact(k)**4)*(396**(4*k)))
        sum_res+=sub_res
        k+=1
    return 1/(mult_value * sum_res)
print("Estimate PI:",estimate_pi())
print("Built-in PI:",mt.pi)