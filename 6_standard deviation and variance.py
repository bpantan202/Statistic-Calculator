def user_input_comma():
    come = input('input data : ').split(',')
    data = []
    for i in come:
        data.append(int(i))
    return data


def find_range(data):
    lowest = data[0]
    highest = data[len(data) - 1]
    range = highest - lowest
    print('-----Range-----')
    print('Highest           >>>', highest)
    print('Lowest            >>>', lowest)
    print('Range             >>>', range)


def mean(data):
    total_sum = 0
    for count in range(0, len(data)):
        total_sum = total_sum + data[count]
    mean = total_sum / len(data)
    print('-----Mean-----')
    print('Total sum (Σx)  >>>', total_sum)
    print('Total data (N)  >>>', len(data))
    print('Mean (x̄)        >>>', mean)
    return mean


def standard_deviation_and_variance(data, mean):
    x_minus_mean_square = []
    zigma_xxx = 0
    for i in data:
        make_xxx = (i - mean) ** 2
        x_minus_mean_square.append(make_xxx)
        zigma_xxx += make_xxx
    s_square = zigma_xxx / len(data)
    s = s_square ** 0.5
    print('-----Standard_deviation and Variance-----')
    print('(x-x̄)                  >>>', x_minus_mean_square)
    print('Σ(x-x̄)                 >>>', zigma_xxx)
    print('Total data (N)         >>>', len(data))
    print('Variance (S**2)        >>>', s_square)
    print('Standard_deviation (S) >>>', s)


data_D = user_input_comma()
data_D.sort()
print(data_D)
print()
mean_D = mean(data_D)
print()
find_range(data_D)
print()
standard_deviation_and_variance(data_D, mean_D)
