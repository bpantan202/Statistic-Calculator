from prettytable import PrettyTable

def user_input():
    input_data = []
    frequency = []
    print('ใส่ข้อมูลเสร็จให้ใส่ -')
    count_data = 0
    while True:
        count_data += 1
        x = input('Data ' + str(count_data) + ' = ')
        if x == '-':
            input_data.sort()
            break
        else:
            input_data.append(int(x))
    for data in input_data:
        f = input('Frequency of ' + str(data) + ' : ')
        frequency.append(float(f))
    return input_data, frequency


def mean(data, frequency):
    fx = []
    for x in range(0, len(data)):
        fx.append(int(data[x] * frequency[x]))
    total_fx = 0
    for count in range(0, len(fx)):
        total_fx = total_fx + fx[count]
    total_f = 0
    for count2 in range(0, len(frequency)):
        total_f = total_f + frequency[count2]
    mean = total_fx / total_f
    show_mean = PrettyTable(['    x    ', '    f    ', '    fx    '])
    for z in range(len(data)):
        show_mean.add_row([data[z], frequency[z], fx[z]])
    show_mean.add_row(['* Total *','N = '+str(total_f),'Σfx = '+str(total_fx)])
    print('===== Mean =====')
    print(show_mean)
    print('Data*frequency (fx) >>>', fx)
    print('Total sum (Σfx)     >>>', total_fx)
    print('Total frequency (N) >>>', total_f)
    print('Mean (x̄)            >>>', mean)


def median(data, frequency):
    cf = []
    create_cf = 0
    for x in range(0, len(frequency)):
        create_cf = create_cf + frequency[x]
        cf.append(create_cf)
    cf_position = []
    for x in range(0, len(frequency)):
        if cf[x] - (frequency[x] - 1) == cf[x]:
            create_cf_position = str(cf[x])
        else:
            create_cf_position = str(cf[x] - (frequency[x] - 1)) + '-' + str(cf[x])
        cf_position.append(create_cf_position)
    median_position = (cf[len(cf) - 1] + 1) / 2
    median = 0
    if (median_position % 1) == 0.5:
        between_case = median_position - 0.5
        if between_case in cf:
            for m in range(0, len(cf)):
                if between_case == cf[m]:
                    median = (data[m] + data[m + 1]) / 2
                    display_line = 'Between Line ' + str(m + 1) + ',' + str(m + 2)
                    break
        else:
            for o in range(0, len(cf)):
                if median_position <= cf[o]:
                    median = data[o]
                    display_line = 'Line ' + str(o + 1)
                    break
    else:
        for m in range(0, len(cf)):
            if median_position <= cf[m]:
                median = data[m]
                break
        display_line = 'Line ' + str(m + 1)
    show_median = PrettyTable(['    x    ', '    f    ', '    cf    ','  position  '])
    for z in range(len(data)):
        show_median.add_row([data[z], frequency[z], cf[z],cf_position[z]])
    print('===== Median =====')
    print(show_median)
    print('Cum frequency (cf)  >>>', cf)
    print('cf position         >>>', cf_position)
    print('Total frequency (N) >>>', cf[len(cf) - 1])
    print('Median position     >>>', median_position)
    print('Median position     >>>', display_line)
    print('Median              >>>', median)


def mode(data, frequency):
    max_frequency = 0
    for x in range(0, len(frequency)):
        if max_frequency < frequency[x]:
            mode = [data[x]]
            max_frequency = frequency[x]
        elif max_frequency == frequency[x]:
            mode.append(data[x])
    print('===== Mode =====')
    if len(mode) <= 2:
        print('Max Frequency     >>>', max_frequency)
        print('Mode              >>>', mode)
    else:
        print('Mode    >>>  No Mode !!!')


def find_range(data):
    lowest = data[0]
    highest = data[len(data) - 1]
    range = highest - lowest
    print('===== Range =====')
    print('Highest           >>>', highest)
    print('Lowest            >>>', lowest)
    print('Range             >>>', range)


data_B, frequency_B = user_input()
print()
print('Data (x)      >>>', data_B)
print('Frequency (f) >>>', frequency_B)
print()
mean(data_B, frequency_B)
print()
median(data_B, frequency_B)
print()
mode(data_B, frequency_B)
print()
find_range(data_B)
