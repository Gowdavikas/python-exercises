def missing_num(n):

    num = set(n)
    temp = []

    for i in range(1, n[-1]):
        if i not in num:
            temp.append(i)
    return temp

list = [1,2,3,5,6,8,11,12]
print("Missed numbers in the list are : ", missing_num(list))
