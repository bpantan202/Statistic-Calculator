def user_input():
    input_data = []
    print('ใส่ข้อมูลเสร็จให้ใส่ end')
    count_data = 0
    while True:
        count_data += 1
        x = input('Data ' + str(count_data) + ' = ')
        if x == 'end':
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

def input_fff():
    input_data = []
    frequency = []
    data = []
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
    for round in input_data:
        f = input('Frequency of ' + str(round) + ' : ')
        frequency.append(float(f))
    for i in range(len(input_data)):
        for j in range(int(frequency[i])):
            data.append(input_data[i])
    return data

quanti = {'M': 2, 'Q': 4, 'D': 10, 'P': 100}


def find_partition(data, alpa, num):
    loca = ((num / quanti[alpa]) * (len(data) + 1))
    print('locataion >>>', loca)
    inte,dec = str(loca).split('.')
    dcde = int(inte)
    print(str(dcde) + '__' + (' ' * (10 - len(str(dcde) + '__'))) + '>>>', data[dcde-1])
    if loca % 1 != 0:
        print(str(dcde+1) + '__' + (' ' * (10 - len(str(dcde+1) + '__'))) + '>>>', data[dcde])
        b_ans = str(data[dcde-1]) + '+0.' + str(dec) + '(' + str(data[dcde]) + '-' + str(data[dcde-1]) + ')'
        ans = (data[dcde - 1]) + ((loca %1) * (data[dcde] - data[dcde - 1]))
        print(alpa + str(num) + (' ' * (10 - len(alpa + str(num)))) + '>>>', b_ans,'=',ans)
    else:
        print(alpa + str(num) + (' ' * (10 - len(alpa + str(num)))) + '>>>', data[int(loca-1)])



print('จำนวนช่วงแบ่ง Median:2  Quartile:4  Decile:10  Percentile:100')

#เปิดอันนี้ใส่ที่ละตัวเลข
# data = user_input()

#เป็ดอันนี้ใส่ที่เดียว(ใส่,คั่น)
data = user_input_comma()
#
#เปิดอันนี้ข้อมูลความถี่
# data = input_fff()

data.sort()
print()
print(data)
print()
print('Total data (n) >>>',len(data))
print()

while True:
    find = input('Find : ').upper()
    if find == 'END':
        break
    else:
        find_partition(data, find[0], int(find[1:len(find)]))
        print()
