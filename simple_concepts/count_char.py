

def is_string_unique(my_string, n):
    # count how many times every string appears in the string
    # good way to check if the string is unique

    count = {}

    for i in range(n):

        if my_string[i] in count.keys():
            return False
        else:
            count[my_string[i]] = 1

    return True



str = 'csgfjrgggukjdvb,xdnvisss'

print(is_string_unique(str, 20))

