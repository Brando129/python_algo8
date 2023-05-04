# Append all the odd numbers from 1 through a value given by a user into a new list

def gettin_odd(num):
    num = num+1
    new_list = []
    for i in range(1, num, 2):
        new_list.append(i)
    return new_list

print(gettin_odd(10))
