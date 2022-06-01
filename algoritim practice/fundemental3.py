
num = 246


def str_num(num):
    str_num = str(num)
    list1 = []
    for i in str_num:
        list1.append(int(i))
    answer1 = 0
    for i in range(len(list1)):
        answer1 += list1[i]
    return answer1

def sum_num(num):
    list1 = str_num(num)
    if list1 > 9:
        list1 = str_num(list1)
    return list1

print(sum_num(num))