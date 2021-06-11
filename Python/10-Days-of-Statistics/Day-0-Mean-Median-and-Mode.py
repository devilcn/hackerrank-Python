from decimal import Decimal

N = int(input())
array_input=input().split(' ')
array_input.sort(key=lambda x: (len(str(x)), x ))

def output_custimization(x):  # output custimization
    x_out = Decimal(x).quantize(Decimal("0.0"))
    return x_out
   
def mean_cal(array_input,N):  # mean cal
    sum_temp = 0
    for i in array_input:
        sum_temp = int(i)+sum_temp
    mean = output_custimization(sum_temp/N)
    return mean
    
def median_cal(array_input):  # median cal
    if len(array_input)%2 == 1:
        if len(array_input) ==1:
            result = array_input[0]
        else:
            result = array_input[len(array_input)//2]
    else:
        m,n = len(array_input) // 2 - 1, len(array_input) // 2
        print(m,n)
        result = output_custimization((int(array_input[m]) + int(array_input[n])) / 2)
    return int(result)

def mode_cal(array_input,N):  # mode cal
    result = max(array_input,key=array_input.count)
    return result

print(mean_cal(array_input,N))
print(median_cal(array_input,N))
print(mode_cal(array_input,N))
