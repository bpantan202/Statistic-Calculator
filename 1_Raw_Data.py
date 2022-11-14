def user_input():
    input_data = []
    print('ใส่ข้อมูลเสร็จให้ใส่ -')
    count_data = 0
    while True:
        count_data += 1
        x = input('Data ' + str(count_data) + ' = ')
        if x == '-':
            return input_data
            break
        else:
            input_data.append(int(x))

def user_input_comma():
    come = input('input data : ').split(',')
    data = []
    for i in come:
        data.append(int(i))
    return data


def mean(data):
    total_sum = 0
    for count in range(0, len(data)):
        total_sum = total_sum + data[count]
    mean = total_sum / len(data)
    print('-----Mean-----')
    print('Total sum (Σx)  >>>', total_sum)
    print('Total data (N)  >>>', len(data))
    print('Mean (x̄)        >>>', mean)


def median(data):
    median_position = (len(data) + 1) / 2
    if (median_position % 1) == 0.5:
        position = median_position // 1
        data1 = data[int(position - 1)]
        data2 = data[int(position)]
        median = (data1 + data2) / 2
    else:
        median = data[int(median_position - 1)]
    print('-----Median-----')
    print('Median position  >>>', median_position)
    print('Median           >>>', median)


def mode(data):
    count_data = {}
    mode = []
    for x in data:
        if x in count_data:
            count_data[x] += 1
        else:
            count_data[x] = 1
    max_frequency = 0
    for y in count_data:
        if max_frequency < count_data[y]:
            mode = [y]
            max_frequency = count_data[y]
        elif max_frequency == count_data[y]:
            mode.append(y)
    print('-----Mode-----')
    if len(mode) <= 2:
        print('Max Frequency     >>>', max_frequency)
        print('Mode              >>>', mode)
    else:
        print('Mode    >>>  No Mode !!!')


def find_range(data):
    lowest = data[0]
    highest = data[len(data) - 1]
    range = highest - lowest
    print('-----Range-----')
    print('Highest           >>>', highest)
    print('Lowest            >>>', lowest)
    print('Range             >>>', range)


# data_A = user_input()
data_A = user_input_comma()
print()
print('Raw data', data_A)
data_A.sort()
print('น้อย->มาก', data_A)
print()
mean(data_A)
print()
median(data_A)
print()
mode(data_A)
print()
find_range(data_A)
