
my_array = list()

for i in range(10):
    my_array.append(i)


def is_empty_member(array):

    for i in range(len(my_array)):
        if my_array[i] == None:
            return False

    return True


print(is_empty_member(my_array))








