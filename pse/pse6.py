list1 = [1] 

list2 = [0]


def merge_lists(list1, list2):
    i = len(list1)-1
    j = len(list2)-1
    k = i+j +1
    list1[len(list1):] = list2[:len(list2)]
    while k >=0:
        if i>=0 and j>=0 and list2[j] <=  list1[i]:
            list1[k] = list1[i]
            i -= 1
        elif j>=0:
            list1[k] = list2[j]
            j-=1
        k -= 1
    return list1
print(merge_lists(list1, list2))


