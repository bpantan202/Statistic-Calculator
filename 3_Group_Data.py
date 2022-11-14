from prettytable import PrettyTable

def user_input():
    input_data = []
    data_start = []
    data_end = []
    frequency = []
    first_start, first_end = input('First Data = ').split('-')
    first_I = (int(first_end) - int(first_start)) + 1
    last_start, last_end = input('Last Data = ').split('-')
    last_I = (int(last_end) - int(last_start)) + 1
    if first_I == last_I:
        I = first_I
        total_data = int(((int(last_start) - int(first_start)) / I) + 1)
        data_start.append(int(first_start))
        data_end.append(int(first_end))
        for x in range(1, total_data):
            start = int(data_end[x - 1] + 1)
            end = int(start + (I - 1))
            data_start.append(start)
            data_end.append(end)
        for x in range(0, total_data):
            create_data = str(data_start[x]) + '-' + str(data_end[x])
            input_data.append(create_data)
        for data in input_data:
            f = input('Frequency of ' + str(data) + ' : ')
            frequency.append(float(f))
    return input_data, frequency, data_start, data_end, I


def mean(data, frequency, data_start, data_end):
    class_mark = []
    fx = []
    total_sum = 0
    total_f = 0
    for count in range(0, len(data)):
        class_mark.append((data_start[count] + data_end[count]) / 2)
    for count in range(0, len(data)):
        fx.append(class_mark[count] * frequency[count])
    for count in range(0, len(data)):
        total_sum = total_sum + fx[count]
    for count in range(0, len(data)):
        total_f = total_f + frequency[count]
    mean = total_sum / total_f
    show_mean = PrettyTable(['  Classes  ', '    f    ',' class mark(x) ', '    fx    '])
    for z in range(len(data)):
        show_mean.add_row([data[z], frequency[z], class_mark[z] ,fx[z]])
    show_mean.add_row(['* Total *', 'N = ' + str(total_f), ' ','Σfx = ' + str(total_sum)])
    print('-----Mean-----')
    print(show_mean)
    print('Class mark (x)       >>>', class_mark)
    print('Class*frequency (fx) >>>', fx)
    print('Total sum (Σfx)      >>>', total_sum)
    print('Total data (N)       >>>', total_f)
    print('Mean (x̄)             >>>', mean)


def median(frequency, data_start, data_end, _I,data):
    cf = []
    create_cf = 0
    for x in range(0, len(frequency)):
        create_cf = create_cf + frequency[x]
        cf.append(create_cf)
    N = cf[len(cf) - 1]
    median_class = N / 2
    for m in range(0, len(cf)):
        if median_class <= cf[m]:
            median_class_position = m
            break
    L = data_start[median_class_position] - 0.5
    fmed = frequency[median_class_position]
    cfl = cf[median_class_position - 1]
    median = L + (_I * ((median_class - cfl) / fmed))
    display_line = 'Line ' + str(median_class_position + 1)
    show_median = PrettyTable(['  Classes  ', '    f    ', '    cf    '])
    for z in range(len(data)):
        show_median.add_row([data[z], frequency[z], cf[z]])
    print('-----Median-----')
    print(show_median)
    print('Cum frequency (cf)  >>>', cf)
    print('Total frequency (N) >>>', N)
    print('Median class (N/2)  >>>', median_class)
    print('Median class        >>>', display_line)
    print('L                   >>>', L)
    print('I                   >>>', _I)
    print('fmed                >>>', fmed)
    print('cfL                 >>>', cfl)
    print('Median              >>>', median)


def mode(frequency, data_start, data_end, _I,data):
    max_frequency = 0
    for x in range(0, len(frequency)):
        if max_frequency < frequency[x]:
            max_frequency = frequency[x]
            modal_class = x
        elif max_frequency == frequency[x]:
            max_frequency = False
            break
    show_mode = PrettyTable(['  Classes  ', '    f    '])
    for z in range(len(data)):
        show_mode.add_row([data[z], frequency[z]])
    print('-----Mode-----')
    if max_frequency == False:
        print("Proogram can't calculate this solution!")
    else:
        print(show_mode)
        L = data_start[modal_class] - 0.5
        d1 = frequency[modal_class] - frequency[modal_class - 1]
        d2 = frequency[modal_class] - frequency[modal_class + 1]
        mode = L + (_I * (d1 / (d1 + d2)))
        display_line = 'Line ' + str(modal_class + 1)
        print('Modal class       >>>', display_line)
        print('L                 >>>', L)
        print('I                 >>>', _I)
        print('d₁                >>>', d1)
        print('d₂                >>>', d2)
        print('Mode              >>>', mode)


data_D, frequency_D, data_start_D, data_end_D, I_D = user_input()
print()
print('Data (x)      >>>', data_D)
print('Frequency (f) >>>', frequency_D)
print()
mean(data_D, frequency_D, data_start_D, data_end_D)
print()
median(frequency_D, data_start_D, data_end_D, I_D, data_D)
print()
mode(frequency_D, data_start_D, data_end_D, I_D,data_D)
