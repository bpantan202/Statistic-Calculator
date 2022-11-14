from prettytable import PrettyTable

quanti = {'M': 2, 'Q': 4, 'D': 10, 'P': 100}

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
    print()
    cf = []
    make_cf = 0
    for i in frequency:
        make_cf += i
        cf.append(int(make_cf))
    show_data = PrettyTable(['  Classes  ', '    f    ', '    cf    '])
    for z in range(len(input_data)):
        show_data.add_row([input_data[z],frequency[z],cf[z]])
    print(show_data)
    return input_data, frequency, data_start, data_end, I,cf


def find_ans(data,frequency,data_start,find_alpa,find_num,I,cf):
    N = cf[len(cf) - 1]
    column = quanti[find_alpa]
    classs = find_num * N / column
    loca = 0
    for i in range(0, len(cf)):
        if cf[i] > classs:
            loca = i
            break
    L = data_start[loca] - 0.5
    cfL = cf[loca - 1]
    fD = int(frequency[loca])
    ans = L + (I * ((classs - cfL) / fD))
    # print('cf        >>>', cf)
    print('N         >>>', int(N))
    print('4/10/100  >>>', column)
    print(find_alpa + str(find_num) + ' class  >>> ' + str(classs) + '__')
    print(' - - -')
    print(f'location  >>> line {loca + 1} ({data[loca]})')
    print('L         >>>', L)
    print('I         >>>', I)
    print('rN/***    >>>', classs)
    print('cfL       >>>', cfL)
    print('f(Q/D/R)  >>>', fD)
    print(find_alpa + str(find_num) + '        >>> ' + str(ans))

data_C, frequency_C, data_start_C, data_end_C, I_C, cf = user_input()
while True:
    print()
    find = input('find : ').upper()
    if find == '-':
        break
    else:
        alpa = find[0]
        num = int(find[1:len(find)])
        find_ans(data_C , frequency_C, data_start_C, alpa ,num ,I_C,cf)





